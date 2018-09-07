from django.db import models
#from django.conf import settings

from django.utils.translation import gettext_lazy as _
from django.contrib.humanize.templatetags.humanize import naturaltime

from django.contrib.auth.models import User
from position.models import Address, Area


KIND_OF_SHARING = (
    (1,_('Lend an Item')),  #_('Lend an item for a time to somebody. (bicycle, drill,...)')
    (2,_('Share an Item')), #_('Share an item for a time with somebody. (refrigerator, car,...)')
    (3,_('Give an Item')),  #_('Give or sell an item to somebody. (shirt, book,...)')
    (4,_('Provide a Service')), #_('Provide a service for somebody. (plumbing, math lessons,...)')
    (5,_('Join an Event')), #_('Let somebody join an event (movie night, party,...)')
)

TYPE_OF_STUFF = (
    (1, _('Item')),     # Physical Object, like a Drill, Bicycle, Banana
    (2, _('Item')),
    (3, _('Item')),
    (4, _('Service')),  # A Service like fixing Toilet or painting
    (5, _('Event')),    # An Event like watching a movie, or having dinner
)

class StuffManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """

    def all_active_for_user(self, user):
        return self.filter( active=True, owner=user )

class Stuff(models.Model):
    """
    Stuff represents an item or Service in the market that can be shared, lend, sold or joined by other Users
    """

    # Owner of the Item or Service
    owner       = models.ForeignKey(User,
                help_text=_('Owner of the Item or Service'), related_name="owned_stuff", on_delete=models.PROTECT)
    # Short Description of the Item or Service
    title       = models.CharField(_('Title'),
                help_text=_('Title Description of the Item, Service or Event (max. 255 characters)'), max_length=255)
    # Long Description of the Item or Service
    description = models.TextField(_('Description'),
                help_text=_('Long Description of the Item, Service or Event (max. 2000 characters)'), null=True, blank=True, max_length=2000)

    image       = models.ImageField(_('Image'),
                upload_to='stuff/', null=True, blank=True)

    # Flags
    sharetype = models.PositiveSmallIntegerField(_('Kind of Sharing'),
                help_text=_('For which kind of sharing is this Stuff available?'), choices=KIND_OF_SHARING, default=1)

    active      = models.BooleanField(_("Active"),
                help_text=_('If the Item or Service is generally available'), default=True)
    location_independent = models.BooleanField(_("Location Independent"),
                help_text=_('If the Item or Service is not dependent on its location'),
                default=False)

    # Location of the Item or Service
    address     = models.ForeignKey(Address,
                help_text=_('Location (Address & Area) the Item or Service is located'), related_name="stuff", on_delete=models.PROTECT)

    # O    TODO [version 0.]: Availability for Events? Two DateTime Fields. Or make availability more generic so it reflects as well the availability of Items and Services...?

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = StuffManager()

    def __str__(self):
        return "%s: %s" % (self.sharetype, self.title)

    @property
    def available(self, date_from=None, date_to=None):
        """ Returns True if the Stuff is available in the specified time frame """
        if self.active == False:
            # Generally not available
            return False
        else:
            # Generally available
            # O    TODO [version 0.]: Make checks on the offers if a time frame is specified
            return True

    @property
    def stufftype(self):
        """ Returns the type of stuff based on the kind of sharing """
        return TYPE_OF_STUFF[self.sharetype]

    @property
    def location(self):
        """ Returns the Location of the Stuff Instance (City,Country)"""
        if self.location_independent:
            return _("Independent of Location")
        else:
            return self.address.area

    class Meta:
        verbose_name = _('Stuff')
        verbose_name_plural = _('Stuff')
        ordering = ['-created_at']
        # O    TODO [version 0.5]: Add Db Indexes probably to area, title,  https://docs.djangoproject.com/en/2.1/ref/models/indexes/
        # indexes = []



class SharingRequestManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class SharingRequest(models.Model):
    """ User issues a sharing request to other Users in the proximity (area):

        {callout}
        {user} requested to {sharetype} a {stufftype}
        happened in {area} {humantime} ago.

        This Request is send to all other Users observing the Location, who in turn can make a Offer. If the Sharing Request has a stuff entry, the Request is send only to the owner of that stuff
    """
    user    = models.ForeignKey(User, on_delete=models.PROTECT,
            related_name='sharing_requests', help_text=_('User who issued the sharing request') )

    area    = models.ForeignKey(Area, on_delete=models.PROTECT,
            help_text=_('Area for the sharing request'), max_length=255)

    callout = models.CharField(_('Sharing Callout'),
            help_text=_('Say what you need!'), max_length=255)

    stuff   = models.ForeignKey(Stuff,
            on_delete=models.PROTECT, null=True, blank=True,
            related_name='sharing_requests',
            help_text=_('Stuff this Sharing Request relates to. (Optional)') )

    # Search Parameters
    sharetype = models.PositiveSmallIntegerField(_('Kind of Sharing'),
                help_text=_('For which kind of sharing is this Sharing Request intended?'), choices=KIND_OF_SHARING, default=1)

    share_start = models.DateTimeField(_('Start Sharing'),
                help_text=_('When do you want to start?'), null=True, blank=True)
    share_end   = models.DateTimeField(_('End Sharing'),
                help_text=_('When do you want to end?'), null=True, blank=True)

    # Flags
    active      = models.BooleanField(_("Active"),
                help_text=_('If the sharing request is active and not yet satisfied'), default=True)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = SharingRequestManager()

    def __str__(self):
        """
        {user} requested to {sharetype}
        {callout}
        happened in {area} {humantime} ago.
        """
        sharing_request = _("%(user)s requested to %(sharetype)s.\n%(callout)s\nHappened in %(area)s %(humantime)s") % {'user': self.user.get_short_name(), 'sharetype': self.sharetype, 'callout': self.callout, 'area': self.area, 'humantime': naturaltime(self.created_at)}

        return sharing_request

    def emitting_party(self):
        """ Returns the user emitting this sharing request """
        return self.user

    def receiving_party(self):
        """ Returns the user(s) receiving this sharing request """
        if self.stuff:
            return self.stuff.user
        else:
            # O    TODO [version 0.3]: gather all user of that area minus the issuing user
            return None

    @property
    def stufftype(self):
        """ Returns the type of stuff based on the kind of sharing """
        return TYPE_OF_STUFF[self.sharetype]

    class Meta:
        verbose_name = _('Sharing Request')
        verbose_name_plural = _('Sharing Requests')
        # ASC Order: Latest first
        ordering = ['-created_at',]



class SharingOfferManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class SharingOffer(models.Model):
    """ User issues a sharing offer to other Users in the proximity (area):

        {pitch}
        {user} offered to {stuff.sharetype} a {stuff.title}
        happened in {area} {humantime} ago.

        This Offer is send to all other Users observing the Location, who in turn can accept the offer. If the Sharing Offer has a request entry, the Offer is send only to the owner of that sharing request.
    """

    request     = models.ForeignKey(SharingRequest,
                on_delete=models.PROTECT, null=True, blank=True,
                related_name='sharing_offers',
                help_text=_('Sharing Request this Sharing Offer relates to') )

    user        = models.ForeignKey(User,
                on_delete=models.PROTECT,
                related_name='sharing_offers',
                help_text=_('User emitting this Sharing Offer') )

    stuff       = models.ForeignKey(Stuff,
                on_delete=models.PROTECT,
                related_name='sharing_offers',
                help_text=_('Stuff this Sharing Offer relates to') )

    pitch       = models.CharField(_('Sharing Pitch'),
                help_text=_('Say what you can share!'), max_length=500)

    # Flags
    active      = models.BooleanField(_("Active"),
                help_text=_('If the sharing offer is active and not yet satisfied'), default=True)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = SharingRequestManager()

    def __str__(self):
        """
        {user} offered to {stuff.sharetype}.
        {stuff.title}
        Happened in {self.stuff.address.area} {humantime} ago
        """
        sharing_offer = _("%(user)s offered to %(sharetype)s.\n%(stuff)s\nHappened in %(area)s %(humantime)s") %  {'user': self.user.get_short_name(), 'sharetype': self.stuff.sharetype, 'stuff': self.stuff.title, 'area': self.stuff.address.area, 'humantime': naturaltime(self.created_at)}
        return sharing_offer

    def emitting_party(self):
        """ Returns the user emitting this sharing offer """
        return self.user

    def receiving_party(self):
        """ Returns the user(s) receiving this sharing offer """
        if self.request:
            return self.request.user
        else:
            # O    TODO [version 0.3]: gather all user of that area minus the issuing user
            return None

    class Meta:
        verbose_name = _('Sharing Offer')
        verbose_name_plural = _('Sharing Offers')
        # ASC Order: Latest first
        ordering = ['-created_at',]

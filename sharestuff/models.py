from django.db import models
from django.conf import settings

from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

TYPE_OF_SHARING = (
    ('1', _('Lend')),       # lend stuff for a given time (bicycle, guitar,...)
    ('2', _('Share')),      # share stuff for a given time (bed, refrigerator,...)
    ('3', _('Gather')),     # do stuff people can gather together (movie, dinner,...)
    ('4', _('Sell')),       # Sell stuff to another person
)

class StuffManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass

class Stuff(models.Model):
    """ Stuff represents an object in the market that is being shared """
    # O    TODO [version 0.]: Category System useful?
    # O    TODO [version 0.]: Able to offer services as well?

    # Owner of the Item or Service
    owner       = models.ForeignKey(User,
                help_text=_('Owner of the Item or Service'), related_name="owned_stuff", on_delete=models.PROTECT)

    # Short Description of the Item or Service
    title       = models.CharField(_('Title'),
                help_text=_('Short Description of the Item or Service (max. 255 characters)'), max_length=255)

    # Long Description of the Item or Service
    description = models.TextField(_('Description'),
                help_text=_('Long Description of the Item or Service (max. 2000 characters)'), null=True, blank=True, max_length=2000)

    # O    TODO [version 0.1]: image to app/media/stuff/<name>
    # O    TODO [version 0.1]: fix permission error 13 --- docker problem?
    image       = models.ImageField(_('Image'), null=True, blank=True)

    # Location of the Item or Service
    # O    TODO [version 0.5]: Make 'country' and 'city' a select field (improves search)
    country     = models.CharField(_('Country'),
                help_text=_('Country the Item or Service is available'), max_length=255, null=True, blank=True)
    city        = models.CharField(_('City'),
                help_text=_('City the Item or Service is available'), max_length=255, null=True, blank=True)
    street      = models.CharField(_('Street'),
                help_text=_('Country the Item or Service is available'), max_length=255, null=True, blank=True)
    # O    TODO [version 0.5]: Implement Long/Lat Functions
    longitude   = models.FloatField(_('Longitude'), null=True, blank=True)
    latitude    = models.FloatField(_('Latitude'), null=True, blank=True)

    # Flags
    active      = models.BooleanField(_("Active"),
                help_text=_('If the Item or Service is generally available'), default=True)
    location_independent = models.BooleanField(_("Location Independent"),
                help_text=_('If the Item or Service is not dependent on its location'), default=False)
    sharetype   = models.CharField(_('Type of Sharing'),
                help_text=_('Which kind of sharing is this Item or Service available'), max_length=255, choices=TYPE_OF_SHARING, default='1')


    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = StuffManager

    def __str__(self):
        return self.title

    @property
    def available(self, date_from=None, date_to=None):
        """ Returns True if the Stuff is available in the specified time frame """
        if self.active == False:
            # Generally not available
            return False
        else:
            # Generally available
            # O    TODO [version 0.1]: Make checks on the bookings if a time frame is specified
            return True

    @property
    def address(self):
        """ Returns the Address of the Stuff Instance """
        # OK    TODO [version 0.1]: Develop address function
        return "%s, %s, %s" % (self.street, self.city, self.country)

    @property
    def location(self):
        """ Returns the Location of the Stuff Instance (City,Country)"""
        if self.location_independent:
            return _("Independent of Location")
        else:
            return "%s (%s)" % (self.city, self.country)

    @property
    def geolocation(self):
        """ Returns the long/lat tuple of the Stuff Instance """
        # OK    TODO [version 0.1]: Develop geolocation function
        # O    TODO [version 0.5]: Make a Tuple class with a proximity function for geolocations and return these
        return (self.longitude, self.latitude)

    class Meta:
        verbose_name = _('Stuff')
        verbose_name_plural = _('Stuff')
        ordering = ['title']
        # O    TODO [version 0.5]: Add Db Indexes https://docs.djangoproject.com/en/2.1/ref/models/indexes/
        # indexes = []








BOOKING_STATES = (
    (0,_('Booking initiated')),     # The booking request/confirm/negotiate
    (1,_('Transaction initiated')), # The transaction (Item, Service, Money) swap
    (2,_('Transaction ended')),     # The transaction swap ended
    (3,_('Booking ended')),         # The booking ended
)
class BookingManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Booking(models.Model):
    """
    Model to register the time frame where an Item or Service is booked. For the Workflow Process of a Booking see BookingEvents.
    """
    stuff           = models.Foreigclass RequestManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Request(models.Model):
    """ User issues a callout to other Users in the proximity
        {User} in {Location} requested {Callout} {min} minutes ago.
        This Request is send to all other Users Observing the Location, who in turn can make a Offer.
    """
    user        = models.ForeignKey(User, on_delete=models.PROTECT,
                related_name='requests', help_text=_('User who issued the request') )

    location    = models.CharField(_('Request Location'),
                help_text=_('Country and City your request is targeted at'), max_length=255, default='1')

    callout     = models.CharField(_('Title'),
                help_text=_('What Item or Service do you request?'), max_length=255)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)

    objects = RequestManager

    def __str__(self):
        # O    TODO [version 0.2]: Use humanize for time https://docs.djangoproject.com/en/2.0/ref/contrib/humanize/#naturaltime
        return _("%s in %s requested %s (%s m ago)") % (self.user, self.location, self.callout, self.created_at)

    class Meta:
        verbose_name = _('Request')
        verbose_name_plural = _('Requests')
        # ASC Order: Latest first
        #ordering = ['booked_from', 'booked_until']




BOOKING_STATES = (
    (0,_('Booking initiated')),     # The booking request/confirm/negotiate
    (1,_('Transaction initiated')), # The transaction (Item, Service, Money) swap
    (2,_('Transaction ended')),     # The transaction swap ended
    (3,_('Booking ended')),         # The booking ended
)
class BookingManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Booking(models.Model):
    """
    Model to register the time frame where an Item or Service is booked. For the Workflow Process of a Booking see BookingEvents.
    """
    stuff           = models.ForeignKey(Stuff,
                    related_name='registered_bookings', help_text=_('Stuff the booking relates to'), null=True,  on_delete=models.SET_NULL)
    borrower        = models.ForeignKey(User,
                    help_text=_('User initiating the booking'), null=True, on_delete=models.SET_NULL)

    # OK    TODO [version 0.1]: Develop Flags
    state           = models.PositiveSmallIntegerField(_('Booking State'),
                    help_text=_('nKey(Stuff,
                    related_name='registered_bookings', help_text=_('Stuff the booking relates to'), null=True,  on_delete=models.SET_NULL)
    borrower        = models.ForeignKey(User,
                    help_text=_('User initiating the booking'), null=True, on_delete=models.SET_NULL)

    # OK    TODO [version 0.1]: Develop Flags
    state           = models.PositiveSmallIntegerField(_('Booking State'),
                    help_text=_('State of the Booking'), choices=BOOKING_STATES, default=0)

    # Timeframe of the booking
    # O    TODO [version 0.2]: Use DurationField
    booked_from     = models.DateTimeField(_('Booked From'))
    booked_until    = models.DateTimeField(_('Booked Until'))

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = BookingManager

    def __str__(self):
        return "Booking of '%s' from %s to %s" % (self.stuff.title, self.booked_from, self.booked_until)

    @property
    def lender(self):
        return self.stuff.owner

    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')
        # ASC Order: Latest first
        ordering = ['booked_from', 'booked_until']


class BookingEventManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class BookingEvent(models.Model):
    """
    """
    booking         = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)

    # O    TODO [version 0.3]: Develop Workflow Process
    # type of the Workflow

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = BookingManager

    def __str__(self):
        return "Booking of %s from %s to %s" % (self.stuff.title, self.shared_from, self.shared_until)

    class Meta:
        verbose_name = _('Booking Event')
        verbose_name_plural = _('Bookings Events')
        # ASC Order: Latest first
        ordering = ['created_at', 'updated_at']

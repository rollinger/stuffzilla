from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone

from django.contrib.auth.models import User

from position.models import Address, Area, Language



TYPE_OF_SUBSCRIPTION = (
    (0, _('No Account')),    # Fallback Account Category
    (1, _('Free Account')),  # Free account
    (2, _('Paid Account')),  # Paid account
)



class ProfileManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Profile(models.Model):
    """
    Public Profile holding additional, public information for a user, seen by other users.
    """
    owner       = models.OneToOneField(User,
                help_text=_('User Account of this Public Profile'), on_delete=models.PROTECT, related_name="public_profile", primary_key=True)
    image       = models.ImageField(_('Your Photo'),
                help_text=_('How other Users see you.'), upload_to='profile/', null=True, blank=True)
    bio         = models.TextField(_('Short Bio'),
                help_text=_('Say something about yourself.'), null=True, blank=True, max_length=1000)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = ProfileManager

    def __str__(self):
        return "%s's Profile" % (self.owner.username)

    class Meta:
        verbose_name = _('Public Profile')
        verbose_name_plural = _('Public Profiles')



class PrivateProfileManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class PrivateProfile(models.Model):
    """
    Private Profile holding additional information for a user seen only by the owner and admins
    """

    owner           = models.OneToOneField(User,
                    help_text=_('User Account of this Private Profile'), on_delete=models.PROTECT, related_name="private_profile", primary_key=True)

    main_address    = models.OneToOneField(Address,
                    help_text=_('Your Main Address'), on_delete=models.PROTECT, related_name="main_address", null=True, blank=True)

    current_area    = models.ForeignKey(Area,
                    help_text=_('Area you currently are observing'), related_name="profiles", on_delete=models.SET_NULL, null=True, blank=True)

    app_lang        = models.ForeignKey(Language,
                    help_text=_('Which language would you like to use in the App?'), related_name="public_profiles", on_delete=models.SET_NULL, null=True, blank=True)

    email           = models.EmailField(_('Email'),
                    help_text=_('Your email address to reach out to you.'))

    phone_number    = models.CharField(_('Phone Number'),
                    help_text=_('Your phone number to reach out to you.'),
                    validators=[ RegexValidator(regex=r'^\+?1?\d{9,15}$',
                    message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))], max_length=17, blank=True)

    email_reminder  = models.BooleanField(_("Email Reminder"),
                    help_text=_('If you want a notification per Email about what other people offer and search in your area'), default=True)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = PrivateProfileManager

    def __str__(self):
        return "%s's Private Profile" % (self.owner.username)

    class Meta:
        verbose_name = _('Private Profile')
        verbose_name_plural = _('Private Profiles')



class InternalProfileManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class InternalProfile(models.Model):
    """
    Internal Profile holding additional information for a user only seen by admins.
    Contains Payment information and statistics
    """

    owner       = models.OneToOneField(User,
                help_text=_('User Account of this Internal Profile'), on_delete=models.PROTECT, related_name="internal_profile", primary_key=True)

    current_subscription_type = models.PositiveSmallIntegerField(
                _('Type of current subscribtion'), help_text=_('Free or Paid Account'), choices=TYPE_OF_SUBSCRIPTION, default=1)
    subscription_from   = models.DateTimeField(
                _('Starting Date & Time of current subscription'), null=True, blank=True )
    subscription_to     = models.DateTimeField(
                _('Ending Date & Time of current subscription'), null=True, blank=True )

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = InternalProfileManager

    def __str__(self):
        return "%s's Internal Profile" % (self.owner.username)

    @property
    def is_paid_account(self):
        """ Returns True if current_subscription_type is a Paid Account """
        if self.current_subscription_type == 2:
            return True
        return False

    class Meta:
        verbose_name = _('Internal Profile')
        verbose_name_plural = _('Internal Profiles')



@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    """ When a new user is created the public, private and internal profile is created alongside and prepopulated """
    if created:
        profile = Profile(owner=instance)
        public_profile = PrivateProfile(owner=instance, email=instance.email)
        internal_profile = InternalProfile(owner=instance)
        # O    TODO [version 0.3.5]: Handle User Subscription on init (Free month)
        profile.save()
        public_profile.save()
        internal_profile.save()

# O    TODO (Feature) [version 0.??]: Modify delete, so the user gets deactivated instead of deleted

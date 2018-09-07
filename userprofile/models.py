from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils import timezone

from django.contrib.auth.models import User

from position.models import Address, Area



class ProfileManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Profile(models.Model):
    """ Profile holding additional information for a user """
    user        = models.OneToOneField(User,
                help_text=_('User Account of this Profile'), on_delete=models.PROTECT, related_name="user_profile", primary_key=True)

    image       = models.ImageField(_('Your Photo'),
                upload_to='profile/', null=True, blank=True)

    location    = models.OneToOneField(Address,
                help_text=_('Your Main Address'), on_delete=models.PROTECT, related_name="main_address", null=True, blank=True)

    language    = models.CharField(_('Application Language'),
                help_text=_('Which language would you like to use?'), choices=settings.LANGUAGES, max_length=255, default='en')

    phone_number    = models.CharField(_('Phone Number'),
        help_text=_('Your phone number to reach out to you.'),
        validators=[ RegexValidator(regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))], max_length=17, blank=True)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = ProfileManager

    def __str__(self):
        return "%s's Profile" % (self.user.username)

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')



@receiver(post_save, sender=User)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    """  """
    if created:
        profile = Profile(user=instance)
        profile.save()

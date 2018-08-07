from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import User

TYPE_OF_SHARING = (
    ('1', _('Lend')),   # lend stuff for a given time (bicycle, guitar,...)
    ('2', _('Share')),  # share stuff for a given time (bed, refrigerator,...)
    ('3', _('Join')),   # do stuff people can join (movie, dinner,...)
    ('4', _('Sell')),   # Sell stuff to another person
)

class StuffManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass

class Stuff(models.Model):
    """ Stuff represents an object in the market that is being shared """
    # Owner of the entry
    owner       = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Item Description
    title       = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), null=True, blank=True)
    image       = models.ImageField(_('Image'), null=True, blank=True)

    # Location
    country     = models.CharField(_('Country'), max_length=255, null=True, blank=True)
    city        = models.CharField(_('City'), max_length=255, null=True, blank=True)
    street      = models.CharField(_('Street'), max_length=255, null=True, blank=True)
    longitude   = models.FloatField(null=True, blank=True)
    latitude    = models.FloatField(null=True, blank=True)

    # Flags
    available   = models.BooleanField(_("Available"), default=True)
    sharetype   = models.CharField(_('Type of Sharing'), max_length=255, choices=TYPE_OF_SHARING, default='1')


    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = StuffManager

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Stuff')
        verbose_name_plural = _('Stuff')



class Booking(models.Model):
    stuff           = models.ForeignKey(Stuff, null=True, on_delete=models.SET_NULL)
    borrower        = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    shared_from     = models.DateTimeField()
    shared_until    = models.DateTimeField()

    def __str__(self):
        return "Booking of %s from %s to %s" % (self.stuff.title, self.shared_from, self.shared_until)

    class Meta:
        verbose_name = _('Booking')
        verbose_name_plural = _('Bookings')

from django.db import models

from django.utils.translation import gettext_lazy as _


class TestimonialManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    def get_random_published_testimonial(self):
        """ Returns a single published Testimonial, randomly selected """
        # DANGER: If the table gets too big this might be a performance problem.
        return Testimonial.objects.filter(published=True).order_by('?')[0]
    def get_all_published(self):
        """ Returns all published Testimonial"""
        return Testimonial.objects.filter(published=True)

class Testimonial(models.Model):
    """
    Testimonial represents a short value statement for Sharezilla
    """
    person_name     = models.CharField(_('Name of the Person'),
                    help_text=_('Name of the Person making the testimonial (max. 255 characters)'), max_length=255)
    person_image    = models.ImageField(_('Image of the Person'),
                    upload_to='testimonials/', max_length=255)
    image_licence   = models.CharField(_('Licence/Credentials for the image'),
                    help_text=_('Make sure you hold the copyrights for the image'), max_length=255)
    title           = models.CharField(_('Title of the Testimonial'),
                    help_text=_('Name of the Person making the testimonial (max. 255 characters)'), max_length=255)
    content         = models.TextField(_('Content of the Testimonial'),
                    help_text=_('The quoted part of the testimonial (max. 2000 characters)'), max_length=1000)

    published      = models.BooleanField(_("Published"),
                    help_text=_('If the testimonial is published'), default=False)

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = TestimonialManager()

    def __str__(self):
        return "%s: %s" % (self.person_name, self.title)

    class Meta:
        verbose_name = _('Testimonial')
        verbose_name_plural = _('Testimonials')
        ordering = ['-created_at']
        # O    TODO [version 0.5]: Add Db Indexes  https://docs.djangoproject.com/en/2.1/ref/models/indexes/
        # indexes = []



class FeedbackManager(models.Manager):
    """ Manager wrapping the complex retrieval operations """
    pass
class Feedback(models.Model):
    """

    """

    created_at  = models.DateTimeField(_('Created at'), auto_now_add=True)
    updated_at  = models.DateTimeField(_('Updated at'), auto_now=True)

    objects = FeedbackManager

    def __str__(self):
        return "%s: %s" % (self.person_name, self.title)

    class Meta:
        # O    TODO [version 0.]: Remove abstract when it will be developed
        abstract = True
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')
        ordering = ['-created_at']
        # O    TODO [version 0.5]: Add Db Indexes  https://docs.djangoproject.com/en/2.1/ref/models/indexes/
        # indexes = []

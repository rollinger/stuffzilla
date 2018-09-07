from modeltranslation.translator import translator, TranslationOptions
from . models import Testimonial

class TestimonialTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

translator.register(Testimonial, TestimonialTranslationOptions)

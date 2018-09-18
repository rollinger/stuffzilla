from modeltranslation.translator import translator, TranslationOptions
from . models import Language

class LanguageTranslationOptions(TranslationOptions):
    fields = ('name', 'country',)

translator.register(Language, LanguageTranslationOptions)

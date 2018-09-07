import django

from django.conf import settings

from django.middleware.locale import LocaleMiddleware
from django.utils.translation import get_language, get_language_from_path
from django.utils.cache import patch_vary_headers
from django.utils import translation

from . models import Profile

if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin as BaseMiddleware
else:
    BaseMiddleware = object

class ProfileLocaleMiddleware(BaseMiddleware):
    """
    This is a very simple middleware that parses a request
    and decides what translation object to install in the current
    thread context depending on the user's account. This allows pages
    to be dynamically translated to the language the user desires
    (if the language is available, of course).
    """

    def get_language_for_user(self, request):
        if request.user.is_authenticated():
            try:
                profile = Profile.objects.get(user=request.user)
                return profile.language
            except Profile.DoesNotExist:
                pass
        return translation.get_language_from_request(request)

    def process_request(self, request):
        translation.activate(self.get_language_for_user(request))
        request.LANGUAGE_CODE = translation.get_language()

    def process_response(self, request, response):
        patch_vary_headers(response, ("Accept-Language",))
        response["Content-Language"] = translation.get_language()
        translation.deactivate()
        return response

class CustomLocaleMiddleware(LocaleMiddleware):
    """ Sets the preferred language based on the userprofile.language setting"""

    def get_language_for_user(self, request):
        if request.user.is_authenticated():
            try:
                profile = Profile.objects.get(user=request.user)
                return profile.language
            except: #Profile.DoesNotExist
                pass
        return None
                #pass
        #return translation.get_language_from_request(request)

    """
    def process_request(self, request):
        user_lang = self.get_language_for_user(request)
        if user_lang:
            translation.activate(user_lang)
            request.LANGUAGE_CODE = translation.get_language()
        else:
            super(CustomLocaleMiddleware, self).process_request(request)


    def process_response(self, request, response):
        patch_vary_headers(response, ("Accept-Language",))
        response["Content-Language"] = translation.get_language()
        translation.deactivate()
        return response
    """

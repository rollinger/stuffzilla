from rest_framework import routers

from position.api import AreaViewSet, AddressViewSet
from market.api import StuffViewSet
from userprofile.api import PublicProfileViewSet, PrivateProfileViewSet
from feedback.api import TestimonialViewSet



# DOC:
# http://www.django-rest-framework.org/api-guide/viewsets/
# http://www.cdrf.co/

# Settings
api = routers.DefaultRouter()
api.register(r'publicprofiles', PublicProfileViewSet)
api.register(r'myprofile', PrivateProfileViewSet)

api.register(r'areas', AreaViewSet)
api.register(r'addresses', AddressViewSet)
api.register(r'stuff', StuffViewSet)
api.register(r'testimonials', TestimonialViewSet)
api.trailing_slash = '/?'

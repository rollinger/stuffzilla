from rest_framework import routers
from position.api import AreaViewSet, AddressViewSet
from market.api import StuffViewSet
from userprofile.api import UserViewSet

# Settings
api = routers.DefaultRouter()
api.register(r'users', UserViewSet)
api.register(r'areas', AreaViewSet)
api.register(r'addresses', AddressViewSet)
api.register(r'mystuff', StuffViewSet)
api.trailing_slash = '/?'

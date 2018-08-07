from rest_framework import routers
from sharestuff.api import UserViewSet, StuffViewSet

# Settings
api = routers.DefaultRouter()
api.register(r'users', UserViewSet)
api.register(r'stuff', StuffViewSet)
api.trailing_slash = '/?'

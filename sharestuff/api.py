from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from . models import Stuff


#
# USER API
#
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the User Model """
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the User Objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer

#
# STUFF API
#
class StuffSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Stuff on Sharezilla """
    class Meta:
        model = Stuff
        fields = ('title', 'image', 'description', 'owner', 'country', 'city')

class StuffViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the stuff  """
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

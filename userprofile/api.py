from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from . models import Profile

#
# USER PROFILE API
#
class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the User Model """
    user = serializers.StringRelatedField()
    class Meta:
        model = Profile
        fields = ('url', 'user', 'language',)

class UserProfileViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the User Objects """
    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer

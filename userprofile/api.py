from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User


#
# USER API
#
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the User Model """
    class Meta:
        model = User
        fields = ('url', 'username',)

class UserViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the User Objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer

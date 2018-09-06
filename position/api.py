from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from . models import Area, Address



#
# Area API
#
class AreaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Area on Sharezilla """
    class Meta:
        model = Area
        fields = ('country', 'region', 'city')

class AreaViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the stuff  """
    queryset = Area.objects.all()
    serializer_class = AreaSerializer



#
# Address API
#
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Address on Sharezilla """
    area = AreaSerializer(many=False, read_only=False)
    class Meta:
        model = Address
        fields = ('street', 'street_number', 'supplement', 'zipcode', 'area')

class AddressViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the stuff  """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

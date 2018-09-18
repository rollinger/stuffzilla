from rest_framework import routers, serializers, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter

from django.contrib.humanize.templatetags.humanize import naturaltime

#from django_filters import rest_framework as filters
#import django_filters.rest_framework

import rest_framework_filters as filters

#print(dir(filters))

from django.contrib.auth.models import User
from utils.models import Address, Area
from utils.api import AddressSerializer
from . models import Stuff



#
# STUFF API (Filters, Serializers, ViewSet)
#
class AreaFilter(filters.FilterSet):
    """ Filter on Area """
    class Meta:
        model = Area
        fields = {'name': ['exact', 'in', 'startswith'],}
            #'region': ['exact', 'in', 'startswith'],
            #'city': ['exact', 'in', 'startswith']}

class AddressFilter(filters.FilterSet):
    """ Filter on Address """
    area = filters.RelatedFilter(AreaFilter, field_name='area', queryset=Address.objects.all())
    class Meta:
        model = Address
        fields = {'street': ['exact', 'in', 'startswith'],
            'area': ['exact', 'in']}

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {'username': ['exact', 'in', 'startswith'],}

class StuffFilter(filters.FilterSet):
    """ Filter on User and Area """
    # Filter on user.username for active Users
    username = filters.RelatedFilter(UserFilter,
                field_name='username', queryset=User.objects.filter(is_active=True))
    #address = filters.RelatedFilter(AddressFilter, field_name='address', queryset=Address.objects.all())
    #area = filter.
    class Meta:
        model = Stuff
        fields = {'username': ['exact'],
            #'area': ['exact'],
            'active': ['exact'],
            'sharetype': ['exact'],
            'location_independent': ['exact'],
        }

class StuffSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Stuff on Sharezilla """
    owner = serializers.StringRelatedField()
    sharetype = serializers.CharField(source='get_sharetype_display')
    time_ago = serializers.SerializerMethodField()
    address = AddressSerializer(many=False, read_only=False)

    class Meta:
        model = Stuff
        fields = ('url', 'title', 'image', 'description', 'owner', 'sharetype', 'location_independent', 'active', 'address', 'time_ago')

    def get_time_ago(self,obj):
        return naturaltime( obj.created_at )

class StuffViewSet(viewsets.ModelViewSet):
    """ ViewSets retrieving the stuff of the user  """
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer
    # See: http://www.django-rest-framework.org/api-guide/filtering/#djangofilterbackend
    filter_backends = (SearchFilter, filters.backends.DjangoFilterBackend, OrderingFilter,)
    search_fields = ('title', 'description')
    filter_class = StuffFilter
    ordering_fields = ('created_at', 'updated_at')
    ordering = ('-created_at',)

    def get_queryset(self):
        """
        This view should return a list of all the stuff
        for the currently authenticated user.
        """
        #user = self.request.user
        #return Stuff.objects.filter(owner=user)
        return Stuff.objects.all()

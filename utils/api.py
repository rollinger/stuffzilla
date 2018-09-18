from rest_framework import routers, serializers, viewsets, mixins
# Permissions
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from . models import Area, Address, Language



#
# Language API
#
class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Language on Sharezilla """
    class Meta:
        model = Language
        fields = ('url', 'code', 'name', 'country')

class LanguageViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSets retrieving the Language for selection in the Frontend

    Permissions: CRUDL
    C,U,D,L:  disabled
    R:  retrieve (anonymous)

    Endpoints:
    /api/languages/	position.api.LanguageViewSet	               language-list
    /api/languages/\.<format>/	position.api.LanguageViewSet     language-list
    /api/languages/<pk>/	position.api.LanguageViewSet	          language-detail
    /api/languages/<pk>/\.<format>/	position.api.LanguageViewSet	language-detail

    """
    permissions = (AllowAny,)
    queryset = Language.objects.filter(supported=True)
    serializer_class = LanguageSerializer



#
# Area API
#
class AreaSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Area on Sharezilla """
    class Meta:
        model = Area
        fields = ( 'url', 'name', 'parent',)

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

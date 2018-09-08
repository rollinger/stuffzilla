from rest_framework import routers, serializers, viewsets, mixins
# Permissions
from rest_framework.permissions import AllowAny
from config.permissions import IsOwner, IsOwnerofUserObject

from django.contrib.auth.models import User
from position.api import AreaViewSet, AddressViewSet
from .models import Profile, PrivateProfile, InternalProfile
from django.contrib.humanize.templatetags.humanize import naturaltime

class PublicProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the User Model """
    owner = serializers.StringRelatedField()

    class Meta:
        model = Profile
        fields = ('url', 'owner', 'image', 'bio')


class PublicProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSets retrieving the Public User Profiles

    Permissions:
    C:  disabled
    R:  retrieve and list (anonymous)
    U:  update (owner)
    D:  disabled
    """
    permissions = (AllowAny,)
    queryset = Profile.objects.all()
    serializer_class = PublicProfileSerializer


class UserProfilePublicProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Public Profile Model """

    class Meta:
        model = Profile
        fields = ('image', 'bio')


class UserProfilePrivateProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Private Profile Model """
    current_area = serializers.StringRelatedField()
    main_address = serializers.StringRelatedField()

    class Meta:
        model = PrivateProfile
        fields = ('language', 'current_area', 'email', 'main_address', 'phone_number',
                  'email_reminder')


class UserProfileInternalProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Internal Profile Model """
    current_subscription_type = serializers.CharField(source='get_current_subscription_type_display')
    subscription_ends_in = serializers.SerializerMethodField()

    def get_subscription_ends_in(self, obj):
        return naturaltime(obj.subscription_to)

    class Meta:
        model = InternalProfile
        fields = ('current_subscription_type', 'subscription_ends_in')


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the UserProfile """
    public_profile = UserProfilePublicProfileSerializer(many=False)
    private_profile = UserProfilePrivateProfileSerializer(many=False)
    internal_profile = UserProfileInternalProfileSerializer(many=False, read_only=True)

    class Meta:
        model = User
        fields = ('username', 'public_profile', 'private_profile', 'internal_profile')
        read_only_fields = ('username', )


class PrivateProfileViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    ViewSets retrieving the full User Profile of a specific user (public & private)
    Viewset does not show up in Root View (no list action)

    Permissions:
    C:  disabled
    R:  retrieve (owner); list is disabled
    U:  update (owner)
    D:  disabled
    """
    permissions = (IsOwnerofUserObject,)
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer

from rest_framework import status, routers, serializers, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import AllowAny
from config.permissions import IsOwner, IsOwnerofUserObject

from django.contrib.auth.models import User
from position.api import AreaViewSet, AddressViewSet
from position.api import LanguageSerializer
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
    user_image = serializers.SerializerMethodField('get_image_url')

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        else:
            return None

    class Meta:
        model = Profile
        fields = ('user_image', 'bio')


class UserProfilePrivateProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for the Private Profile Model """
    current_area = serializers.StringRelatedField()
    main_address = serializers.StringRelatedField()

    class Meta:
        model = PrivateProfile
        fields = ('app_lang', 'current_area', 'email', 'main_address', 'phone_number', 'email_reminder')


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

    def update(self, instance, validated_data):
        public_profile_data = validated_data.pop('public_profile')
        private_profile_data = validated_data.pop('private_profile')

        # Get or create the profiles from the user instance and set the data
        public_profile, created  = Profile.objects.get_or_create(owner=instance)
        private_profile, created  = PrivateProfile.objects.get_or_create(owner=instance)

        # Set the values
        public_profile.bio = public_profile_data.get(
            'bio',
            public_profile.bio
        )
        # O    TODO [version 0.]: Image File upload
        private_profile.phone_number = private_profile_data.get(
            'phone_number',
            private_profile.phone_number
        )
        private_profile.email_reminder = private_profile_data.get(
            'email_reminder',
            private_profile.email_reminder
        )
        private_profile.app_lang = private_profile_data.get(
            'app_lang',
            private_profile.app_lang
        )

        # Save the profiles
        public_profile.save()
        private_profile.save()

        # Return instance
        return instance

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

    Endpoints:
    /api/myprofile/{uid}
    """
    permissions = (IsOwnerofUserObject,)
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserProfileSerializer

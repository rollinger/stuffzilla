from rest_framework import routers, serializers, viewsets, response
from rest_framework.filters import OrderingFilter, SearchFilter

from django.shortcuts import get_object_or_404

from . models import Testimonial

class TestimonialSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializers for the Testimonials on Sharezilla """
    person_image = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Testimonial
        fields = ('title', 'content', 'person_name', 'person_image', 'image_licence')

    def get_image_url(self, obj):
        return obj.person_image.url

class TestimonialViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving testimonials.
    """
    serializer_class = TestimonialSerializer
    queryset = Testimonial.objects.get_all_published()

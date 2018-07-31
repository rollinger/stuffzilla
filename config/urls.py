from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import logout

from config.api import api

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout')
]

if settings.DEBUG:
    # Media urls for development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


class ExtraContextTemplateView(TemplateView):
    """
    Hack to pass some content to Template View
    """
    def get_context_data(self, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(**kwargs)
        context['DEBUG'] = settings.DEBUG
        context['SENTRY_PUBLIC_DSN'] = settings.SENTRY_PUBLIC_DSN
        
        context['GOOGLE_ANALYTICS'] = settings.GOOGLE_ANALYTICS
        return context


# App: Vue routing
urlpatterns += [url(r'^', ExtraContextTemplateView.as_view(template_name='main.html'))]

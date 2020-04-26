from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api/', include('articles.api.urls')),

    path('mails/', include('mails.api.urls')),
    path('btypes/', include('btypes.api.urls')),
    path('priorities/', include('priorities.api.urls')),
    path('states/', include('states.api.urls')),
    path('bulletins/', include('bulletins.api.urls')),
    path('agents/', include('agents.api.urls')),

    path('admin/', admin.site.urls),
    re_path(r'^.*', TemplateView.as_view(template_name='index.html')),
]


from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('aocpo_api.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
    re_path(r'.*', TemplateView.as_view(template_name='index.html'))
]

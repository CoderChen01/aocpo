from django.contrib import admin
from django.urls import path
from AI_models_api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('AI_analysis', views.CfyAndSen.as_view() )
]

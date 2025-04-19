from django.urls import path
from . import views
from .controllers import PageController, CoreController

app_name = 'presentation'

urlpatterns = [
    path('', views.home, name='home'),
    path('api/health', CoreController.health),
    path('api/pages', PageController.pages),
    # …
]

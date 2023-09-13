from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register(r'greeting', views.GreetingsAPIModelView, basename="greetings")

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from agile.views import *
from agile import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register("cards", views.CardViewSet)
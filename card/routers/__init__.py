from rest_framework.routers import DefaultRouter
from card import views

router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register("cards", views.CardViewSet)
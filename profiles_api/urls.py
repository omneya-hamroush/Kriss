from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
router.register('product', views.ProductViewSet, base_name='product')


urlpatterns=[
path('',include(router.urls))
]

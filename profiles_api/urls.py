from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
router.register('product-viewset', views.ProductViewSet, base_name='product-viewset')


urlpatterns=[
#path('product-view/', views.ProductViewSet.as_view()),
path('',include(router.urls))
]

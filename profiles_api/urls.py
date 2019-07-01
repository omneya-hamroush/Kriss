from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
router.register('product-viewset', views.ProductViewSet, base_name='product-viewset')
router.register('shoppage-viewset', views.ShopPageViewSet, base_name= 'shoppage-viewset')
router.register('picture-viewset', views.PictureViewSet, base_name= 'picture-viewset' )
router.register('store-viewset', views.StoreViewSet, base_name= 'store-viewset')

urlpatterns=[
#path('product-view/', views.ProductViewSet.as_view()),
path('',include(router.urls))
]

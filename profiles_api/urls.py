from django.urls import path, include

from rest_framework.routers import DefaultRouter
from profiles_api import views

router= DefaultRouter()
router.register('cart-viewset', views.CartViewSet, base_name= 'cart-viewset')
router.register('product-viewset', views.ProductViewSet, base_name='product-viewset')
router.register('picture-viewset', views.PictureViewSet, base_name= 'picture-viewset' )
router.register('store-viewset', views.StoreViewSet, base_name= 'store-viewset')
router.register('contact-viewset', views.ContactUsViewSet, base_name= 'contact-viewset')
router.register('aboutus-viewset', views.AboutUsViewSet, base_name='aboutus-viewset')
router.register('cartitem-viewset', views.CartItemViewSet, base_name='cartitem-viewset')
router.register('offer-viewset', views.LatestOfferViewSet, base_name='offer-viewset')
router.register('family-viewset', views.FamilyViewSet, base_name='family-viewset')
router.register('category-viewset', views.CategoryViewSet, base_name='category-viewset')
router.register('brand-viewset', views.BrandViewSet, base_name='brand-viewset')
router.register('order-viewset', views.OrderViewSet, base_name='order-viewset')

urlpatterns=[
#path('product-view/', views.ProductViewSet.as_view()),
path('',include(router.urls))
]

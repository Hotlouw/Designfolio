from django.urls import path
from . import views
from .views import ProductListCreate,ProductRetrieveUpdateDestroy,ProductList,CartItemList,CartItemDetail
from django.conf.urls.static import static
from django.conf import settings
from .views import contact_list, aboutus_list, login_list,main_view

urlpatterns = [
    path('main/', main_view, name ='main_view'),
    path('shops/', ProductListCreate.as_view(), name='shop-list-create'),
    path('shops/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='shop-retrieve-update-destroy'),
    path('contact/',contact_list, name='contact_list'),
    path('aboutus', aboutus_list, name='aboutus_list'),
    path('login/', login_list, name='login_list'),
    path('api/products/', ProductList.as_view(), name='product-list'),
    path('api/cart/', CartItemList.as_view(), name='cart-item-list'),
    path('api/cart/<int:pk>/', CartItemDetail.as_view(), name='cart-item-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

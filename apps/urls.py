


# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('cart/', views.view_cart, name='view_cart'),
#     path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
# ]

from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('add_product/', views.add_product, name='add_product'),
    path('supper_product_list/', views.supper_product_list, name='supper_product_list'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


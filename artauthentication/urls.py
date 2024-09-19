from django.urls  import path, include
from . import views
urlpatterns=[
    path('logout',views.Logout, name='logout'),
    path('login',views.Login, name='login'),
    path('signup',views.signup, name='signup'),
    path('update_shop',views.update_shop, name='update_shop'),
    path('createshop',views.createshop, name='createshop'),
    path('createproduct',views.createproduct, name='createproduct'),
    path('shop/deleteproduct/<pk>', views.deleteproduct, name='deleteproduct'),
    path('deleteproduct/<pk>', views.deleteproduct, name='deleteproduct'),
]
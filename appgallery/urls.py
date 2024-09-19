from django.urls  import path
from . import views

urlpatterns = [
     path('',views.home, name='home'),
     path('profile',views.profile, name='profile'),
     path('search',views.search, name='search'),
     path('shop/<name>', views.shop, name='shop'),
     path('buy/<name>', views.user_shop, name='buy'),
     path('profile_update', views.update_profile, name='profile_update'),
]

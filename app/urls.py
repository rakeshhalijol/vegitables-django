from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('signin/',views.signin,name = "signin"),
    path('login/',views.login,name = "login"),
    path('logout/',views.logout,name = "logout"),
    path('show/<int:id>/',views.show,name = 'Show'),
    path('review/<int:id>/',views.review,name = 'review'),
    path('cart/<int:id>/',views.cart,name = 'cart'),
    path('confirm/',views.confirm,name = 'confirm'),
    path('shop/',views.shop,name = 'shop'),
    path('update/<int:id>/',views.update_quantity,name = 'update')
]
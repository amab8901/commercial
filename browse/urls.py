from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.order, name='order'),
    path('checkout/', views.checkout, name='checkout'),
    path('media/default.jpeg', views.media, name='media'),
    path('login_register/', views.login_register, name='login_register'),
    
    path('create-checkout-session/<pk>', views.CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', views.SuccessView.as_view(), name='success'),
]

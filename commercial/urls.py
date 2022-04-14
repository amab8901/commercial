from django.contrib import admin
from django.urls import include, path
from browse.views import (
    CreateCheckoutSessionView,
    SuccessView,
    CancelView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('browse.urls')),
    path('browse/', include('browse.urls')),
    path('home/', include('browse.urls')),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('cart/', include('browse.urls')),
    path('checkout/', include('browse.urls')),
    path('create-checkout-session/<pk>', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('payments/', include('browse.urls')),
    path('success/', SuccessView.as_view(), name='success'),
]



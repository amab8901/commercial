import stripe
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import TemplateView
from .models import Product, Order, Price


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        price = Price.objects.get(id=self.kwargs["pk"])
        YOUR_DOMAIN = "http://127.0.0.1:8000" # change in production
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price.stripe_price_id,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url)

class SuccessView(TemplateView):
    template_name = "browse/success.html"

class CancelView(TemplateView):
    template_name = "browse/cancel.html"

def base(request):
    return render(request, 'browse/base.html')

def order(request):
    order_list = Order.objects.all()
    return render(request, 'browse/cart.html', {'order_list': order})

def checkout(request):
    return render(request, 'browse/checkout.html')

def index(request):
    product_list = Product.objects.all()
    return render(request, 'browse/index.html', {'product_list': product_list})

def increase_quantity(request, id):
    return HttpResponse('quantity increased')

def login_register(request):
    return render(request, 'browse/login_registration.html')

def media(request):
    return render(request, 'browse/default-image.html')

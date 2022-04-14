import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

class Customer(models.Model):
    name = models.CharField(max_length=200, default='John Doe')
    phone = models.CharField(max_length=20, default='+46764064325f', validators=[RegexValidator('^[/+]?[0-9 ]+$')])
    email = models.EmailField(max_length=200, default='amab8901@gmail.com')
    address = models.CharField(max_length=200, default='Johannesbäcksgatan 62F', validators=[RegexValidator('^[a-öA-Ö0-9 ]+$')])
    city = models.CharField(max_length=200, default='New York', validators=[RegexValidator('^[a-öA-Ö ]+$')])
    zip = models.CharField(max_length=5, default='', validators=[RegexValidator('^[0-9]{5}$')])
    date_created = models.DateTimeField('customer created', auto_now_add=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    description = models.CharField(max_length=1000, default="")
    id = models.CharField(max_length=100, default="", primary_key=True)
    image = models.ImageField(default="default.jpeg", upload_to='')
    name = models.CharField(max_length=200)
    payment_link = models.CharField(max_length=100, default="")
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    
    def __str__(self):
        return self.name
    def decrease(self):
        quantity = quantity - 1
        return quantity
    def increase(self):
        quantity = quantity + 1
        return quantity
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stripe_price_id = models.CharField(max_length=100)
    price = models.IntegerField(default=0) # cents

    def get_display_price(self):
        return "{0:.2f}".format(self.price / 100)

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='+', default='')

    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def image(self):
        return self.product.image
    def product_name(self):
        return self.product.name

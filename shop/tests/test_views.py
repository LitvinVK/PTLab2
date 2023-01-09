from django.test import TestCase, Client
from shop.views import PurchaseCreate
from shop.models import Product, Purchase
from django.http import HttpResponse
from django.views.generic.edit import CreateView

class PurchaseCreateTestCase(TestCase, CreateView):

    model = Purchase
    fields = ['product', 'person', 'address']

    def setUp(self):
        self.client = Client()

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_form_valid(self):
        self.product_book = Product.objects.create(name="book", price="740", count="5", id="1")
        self.form = Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.")
        prods = Product.objects.get(id="1")
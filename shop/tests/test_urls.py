from django.test import SimpleTestCase
from django.urls import reverse, resolve
from shop.views import index, PurchaseCreate

class UrlTestCase(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_buy_url_is_resolved(self):
        url = reverse('buy', args=['1'])
        self.assertEquals(resolve(url).func.view_class, PurchaseCreate)
from django.test import TestCase
from rest_framework.test import APIClient

from api_v1.models import Product


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name='Product A', category_id=1)

    def test_get_all_products(self):
        response = self.client.get('/api/v1/products/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Product A')
        self.assertEqual(response.data[0]['category_id'], 1)

    def test_create_product(self):
        data = {'name': 'New Product', 'category_id': 3}
        response = self.client.post('/api/v1/products/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 2)

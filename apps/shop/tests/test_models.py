from django.test import TestCase
from ..models import Category, Product
from datetime import datetime


class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="cereals", slug="cereals")

    def test_category_creation(self):
        """
        Test that a category is created with the correct name and slug
        """
        self.assertTrue(isinstance(self.category, Category))
        self.assertEqual(self.category.__str__(), self.category.name)
        self.assertEqual(self.category.slug, "cereals")


class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="cereals", slug="cereals")
        self.product = Product.objects.create(
            name="rice",
            slug="rice",
            category=self.category,
            description="rice",
            price=100,
            available=True,
            created=datetime.now(),
            updated=datetime.now(),
        )

    def test_product_creation(self):
        """
        Test that a product is created with the correct name and slug
        """
        self.assertTrue(isinstance(self.product, Product))
        self.assertEqual(self.product.__str__(), self.product.name)
        self.assertEqual(self.product.slug, "rice")
        self.assertEqual(self.product.category, self.category)

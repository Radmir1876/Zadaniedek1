""" This module tests website app models """

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.test import TestCase
from django.utils import timezone

from website.models import (
    Category,
    Product,
    PaymentMethod,
    PurchaseOrder,
    PurchaseItem,
    PurchasePaymentMethod
)


class CategoryModelTest(TestCase):
    """ Test case for the Category model """

    description = 'Test123'
    description_update = 'Test321'

    def test_instance(self):
        """ Test category Category constructor """

        category = Category(description=self.description)
        self.assertIsInstance(category, Category)

    def test_creation(self):
        """ Test creation of Category instance in the database """

        created_category = Category.objects.create(
            description=self.description
        )
        queried_category = Category.objects.get(id=created_category.id)
        self.assertEqual(created_category, queried_category)

    def test_str(self):
        """ Test Category __str__ method """

        expected_result = 'Category - Test123'
        category = Category(description=self.description)
        self.assertEqual(str(category), expected_result)

    def test_repr(self):
        """ Test Category __repr__ method """

        expected_result = 'Category(description=Test123)'
        category = Category(description=self.description)
        self.assertEqual(repr(category), expected_result)


class ProductModelTest(TestCase):
    """ Test case for the Product model """

    category = Category.objects.create(
        description='Category'
    )
    barcode = '5901234123457'
    slug = None
    title = 'Mattress'
    description = 'Mattress'
    image = 'mattress.jpg'
    price = 800.724

    def test_instance(self):
        """ Test Product model constructor """

        product = Product(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.pk
        )
        self.assertIsInstance(product, Product)

    def test_creation(self):
        """ Test creation of Product instance in the database """

        created_product = Product.objects.create(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.id
        )
        queried_product = Product.objects.get(barcode='5901234123457')
        self.assertEqual(created_product, queried_product)

    def test_duplicate_product_creation(self):
        """ Test creation of a duplicate Product in the database """

        Product.objects.create(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category_id=self.category.id
        )
        with self.assertRaises(IntegrityError):
            Product.objects.create(
                barcode=self.barcode, slug=self.slug, title=self.title,
                description=self.description, image=self.image,
                price=self.price, category_id=self.category.id
            )

    def test_str(self):
        """ Test Product __str__ method """

        expected_result = 'Product - Mattress'
        product = Product(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category=self.category
        )
        self.assertEqual(str(product), expected_result)

    def test_repr(self):
        """ Test product __repr__ method """

        expected_result = 'Product(barcode=5901234123457,title=Mattress,' \
                          'description=Mattress,price=800.724,' \
                          'category=Category,slug=None)'
        product = Product(
            barcode=self.barcode, slug=self.slug, title=self.title,
            description=self.description, image=self.image, price=self.price,
            category=self.category
        )
        self.assertEqual(repr(product), expected_result)


class PaymentMethodTest(TestCase):
    """ Test case for the PaymentMethod model """

    description = 'Test123'

    def test_instance(self):
        """ Test PurchaseOrder model constructor """

        payment_method = PaymentMethod(description=self.description)
        self.assertIsInstance(payment_method, PaymentMethod)

    def test_creation(self):
        """ Test creation of PaymentMethod instance in the database """

        created_payment_method = PaymentMethod.objects.create(
            description=self.description
        )
        queried_payment_method = PaymentMethod.objects.get(
            id=created_payment_method.id
        )
        self.assertEqual(created_payment_method, queried_payment_method)

    def test_str(self):
        """ Test PaymentMethod __str__ method """

        expected_result = 'PaymentMethod - Test123'
        payment_method = PaymentMethod(description=self.description)
        self.assertEqual(str(payment_method), expected_result)

    def test_repr(self):
        """ Test PaymentMethod __repr__ method """

        expected_result = 'PaymentMethod(description=Test123)'
        payment_method = PaymentMethod(description=self.description)
        self.assertEqual(repr(payment_method), expected_result)


class PurchaseOrderTest(TestCase):
    """ Test case for the PurchaseOrder model """

    description_repr_method = '1 - user12'
    description_str_method = '1 - user12'

    def setUp(self):
        # create user instance
        self.user = User.objects.create(
            username='user12',
            first_name='firstname',
            last_name='lastname',
            email='user12@company.com',
            password='okabc321'
        )

    def test_instance(self):
        """ Test PurchaseOrder model constructor """

        purchase_order = PurchaseOrder(
            timestamp=timezone.now(),
            user=self.user,
            cart=False
        )
        self.assertIsInstance(purchase_order, PurchaseOrder)

    def test_creation(self):
        """ Test creation of PurchaseOrder instance in the database """

        created_purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(),
            user=self.user,
            cart=False
        )
        queried_purchase_order = PurchaseOrder.objects.get(
            id=created_purchase_order.id
        )
        self.assertEqual(created_purchase_order, queried_purchase_order)

    def test_str(self):
        """ Test PurchaseOrder __str__ method """

        expected_result = 'PurchaseOrder - 1'
        purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(),
            user=self.user,
            cart=False
        )
        self.assertEqual(str(purchase_order), expected_result)

    def test_repr(self):
        """ Test PurchaseOrder __repr__ method """

        purchase_order = PurchaseOrder.objects.create(
            timestamp='2018-10-08 13:49:00+03:00',
            user=self.user,
            cart=False
        )
        expected_result = 'PurchaseOrder(id=1,timestamp=2018-10-08 ' \
                          '13:49:00+03:00,user=user12,cart=False)'
        self.assertEqual(repr(purchase_order), expected_result)


class PurchaseItemTest(TestCase):
    """ Test case for the PurchaseItem model """

    def setUp(self):
        # create user instance
        self.user = User.objects.create(
            username='user12',
            first_name='firstname',
            last_name='lastname',
            email='user12@company.com',
            password='okabc321'
        )

        # create PurchaseOrder instance
        self.created_purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(),
            user=self.user,
            cart=False
        )

        # create Category instance
        self.category = Category.objects.create(
            description='Category'
        )

    def test_instance(self):
        """ Test PurchaseItem model constructor """

        purchase_item = PurchaseItem(
            purchase_order=self.created_purchase_order,
            quantity=1.0,
            price=1.0,
            category=self.category,
            total_price=2.0
        )
        self.assertIsInstance(purchase_item, PurchaseItem)

    def test_creation(self):
        """ Test creation of PurchaseItem instance in the database """

        created_purchase_item = PurchaseItem.objects.create(
            purchase_order=self.created_purchase_order,
            quantity=1.0,
            price=1.0,
            category=self.category,
            total_price=2.0
        )
        queried_purchase_item = PurchaseItem.objects.get(
            id=created_purchase_item.id
        )
        self.assertEqual(created_purchase_item, queried_purchase_item)

    def test_str(self):
        """ Test PurchaseItem __str__ method """

        expected_result = 'PurchaseItem 1 - order 1'
        purchase_item = PurchaseItem.objects.create(
            purchase_order=self.created_purchase_order,
            quantity=1.0,
            price=1.0,
            category=self.category,
            total_price=2.0
        )
        self.assertEqual(str(purchase_item), expected_result)

    def test_repr(self):
        """ Test PurchaseItem __repr__ method """

        expected_result = 'PurchaseItem(id=1,barcode=,purchase_order=1,' \
                          'quantity=1.0,total_price=2.0)'
        purchase_item = PurchaseItem.objects.create(
            purchase_order=self.created_purchase_order,
            quantity=1.0,
            price=1.0,
            category=self.category,
            total_price=2.0
        )
        self.assertEqual(repr(purchase_item), expected_result)


class PurchasePaymentMethodTest(TestCase):
    """ Test case for the PurchasePaymentMethod model """

    def setUp(self):
        self.description = 'Cash'

        # create user instance
        self.user = User.objects.create(
            username='user12',
            first_name='firstname',
            last_name='lastname',
            email='user12@company.com',
            password='okabc321'
        )

        # create PurchaseOrder instance
        self.purchase_order = PurchaseOrder.objects.create(
            timestamp=timezone.now(),
            user=self.user,
            cart=False
        )

        # create PaymentMethod
        self.payment_method = PaymentMethod.objects.create(
            description=self.description
        )

    def test_instance(self):
        """ Test PurchasePaymentMethod model constructor """

        created_purchase_payment_method = PurchasePaymentMethod(
            purchase_order=self.purchase_order,
            payment_method=self.payment_method,
            value=2.0
        )
        self.assertIsInstance(
            created_purchase_payment_method, PurchasePaymentMethod
        )

    def test_creation(self):
        """ Test creation of PurchasePaymentMethod instance in the database """

        created_purchase_payment_method = PurchasePaymentMethod.objects.create(
            purchase_order=self.purchase_order,
            payment_method=self.payment_method,
            value=2.0
        )
        queried_purchase_payment_method = PurchasePaymentMethod.objects.get(
            id=created_purchase_payment_method.id
        )
        self.assertEqual(
            created_purchase_payment_method, queried_purchase_payment_method
        )

    def test_str(self):
        """ Test PurchasePaymentMethod __str__ method """

        expected_result = 'PurchasePaymentMethod 1 - order 1'
        purchase_payment_method = PurchasePaymentMethod.objects.create(
            purchase_order=self.purchase_order,
            payment_method=self.payment_method,
            value=2.0
        )
        self.assertEqual(str(purchase_payment_method), expected_result)

    def test_repr(self):
        """ Test PurchasePaymentMethod __repr__ method """

        expected_result = 'PurchasePaymentMethod(id=1,purchase_order=1,' \
                          'payment_method=Cash,value=2.0)'
        purchase_payment_method = PurchasePaymentMethod.objects.create(
            purchase_order=self.purchase_order,
            payment_method=self.payment_method,
            value=2.0
        )
        self.assertEqual(repr(purchase_payment_method), expected_result)

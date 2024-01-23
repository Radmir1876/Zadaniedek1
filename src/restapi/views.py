
from rest_framework.generics import CreateAPIView

from website.models import (
    Category,
    Product,
    PaymentMethod,
    PurchaseOrder,
    PurchaseItem
)
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    PaymentMethodSerializer,
    PurchaseOrderSerializer,
    PurchaseItemSerializer
)


class CategoryCreateView(CreateAPIView):
    """ Создать представление для объектов категории """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'description'


class ProductCreateView(CreateAPIView):
    """ Создать представление для объектов продукта """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'barcode'


class PaymentMethodCreateView(CreateAPIView):
    """ Создать представление для объектов PaymentMethod """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    lookup_field = 'description'


class PurchaseOrderCreateView(CreateAPIView):
    """ Создать представление для объектов PurchaseOrder """

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'id'


class PurchaseItemCreateView(CreateAPIView):
    """ Создать представление для объектов PurchaseItem """

    queryset = PurchaseItem.objects.all()
    serializer_class = PurchaseItemSerializer
    lookup_field = 'id'

from rest_framework import serializers

from website.models import (
    Category,
    Product,
    PaymentMethod,
    PurchaseOrder,
    PurchaseItem
)


class CategorySerializer(serializers.ModelSerializer):
    """ Сериализатор для модели категории """

    class Meta:
        """ Мета-класс CategorySerializer """

        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели продукта """

    class Meta:
        """ Мета-класс ProductSerializer """

        model = Product
        exclude = ('slug', )


class PaymentMethodSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели PaymentMethod """

    class Meta:
        """Мета-класс PaymentMethodSerializer """

        model = PaymentMethod
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели заказа на покупку """

    class Meta:
        """ Мета-класс PurchaseOrderSerializer """

        model = PurchaseOrder
        fields = '__all__'


class PurchaseItemSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели PurchaseItem """

    class Meta:
        """ Мета-класс PurchaseItemSerializer """

        model = PurchaseItem
        fields = '__all__'

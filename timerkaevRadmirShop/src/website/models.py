
from django.conf import settings
from django.db.models.signals import pre_save
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy

from .utils import unique_slug_generator


class Category(models.Model):
    """ Категории товаров """

    description = models.CharField(
        max_length=50, verbose_name=gettext_lazy('Description')
    )

    class Meta:
        """ Метакласс категории """

        verbose_name = gettext_lazy('Category')
        verbose_name_plural = gettext_lazy('Categories')

    def __str__(self):
        return 'Category - {}'.format(self.description)

    def __repr__(self):
        return ('Category(description={})').format(self.description)


class ProductBase(models.Model):
    """ Класс, представляющий абстракцию как для Product, так и для PurchaseItem.
     Он содержит общие поля между двумя моделями """

    barcode = models.CharField(
        primary_key=True, max_length=20,
        verbose_name=gettext_lazy('Barcode')
    )
    title = models.TextField(verbose_name=gettext_lazy('Title'))
    description = models.TextField(verbose_name=gettext_lazy('Description'))
    image = models.ImageField(verbose_name=gettext_lazy('Image'))
    price = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name=gettext_lazy('Price')
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Category')
    )

    class Meta:
        """ Метакласс ProductBase """

        abstract = True


class Product(ProductBase):

    class Meta:
        """ Метакласс продукта """

        verbose_name = gettext_lazy('Product')
        verbose_name_plural = gettext_lazy('Products')

    barcode = models.CharField(
        primary_key=True, max_length=20, verbose_name=gettext_lazy('Barcode')
    )
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        """ Возвращает всю конечную точку продукта (конечная точка сведений
о продукте + поле slug).
        """
        return reverse('website:product-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return 'Product - {}'.format(self.title)

    def __repr__(self):
        return (
            'Product(barcode={},title={},description={},'
            'price={},category={},slug={})'.format(
                self.barcode,
                self.title,
                self.description,
                self.price,
                self.category.description,
                self.slug
            )
        )


def pre_save_product_receiver(sender, instance, *args, **kwargs):
    """ Генерирует поле slug перед сохранением экземпляра продукта """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_product_receiver, sender=Product)


class PaymentMethod(models.Model):


    description = models.CharField(
        unique=True, max_length=50, verbose_name=gettext_lazy('Description')
    )

    class Meta:


        verbose_name = gettext_lazy('PaymentMethod')
        verbose_name_plural = gettext_lazy('PaymentMethods')

    def __str__(self):
        return 'PaymentMethod - {}'.format(self.description)

    def __repr__(self):
        return ('PaymentMethod(description={})').format(self.description)


class PurchaseOrder(models.Model):


    timestamp = models.DateTimeField(verbose_name=gettext_lazy('Timestamp'))
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('User')
    )
    cart = models.BooleanField(verbose_name=gettext_lazy('Cart'))

    class Meta:
        """ PurchaseOrder's Meta class """

        verbose_name = gettext_lazy('PurchaseOrder')
        verbose_name_plural = gettext_lazy('PurchaseOrders')

    def __str__(self):
        return 'PurchaseOrder - {}'.format(self.id)

    def __repr__(self):
        return ('PurchaseOrder(id={},timestamp={},user={},cart={})').format(
            self.id,
            self.timestamp,
            self.user,
            self.cart
        )


class PurchaseItem(ProductBase):
    """ The products of a specific PurchaseOrder """

    id = models.AutoField(primary_key=True)
    barcode = models.CharField(
        max_length=20, verbose_name=gettext_lazy('Barcode')
    )
    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE,
        verbose_name=gettext_lazy('PurchaseOrder')
    )
    quantity = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name=gettext_lazy('Quantity')
    )
    total_price = models.DecimalField(
        max_digits=8, decimal_places=3,
        verbose_name=gettext_lazy('TotalPrice')
    )
    slug = None  # this class doesn't use this attribute

    class Meta:
        """ PurchaseItem's Meta class """

        verbose_name = gettext_lazy('PurchaseItem')
        verbose_name_plural = gettext_lazy('PurchaseItems')

    def __str__(self):
        return 'PurchaseItem {} - order {}'.format(
            self.id, self.purchase_order.id
        )

    def __repr__(self):
        return (
            'PurchaseItem(id={},barcode={},purchase_order={},'
            'quantity={},total_price={})'.format(
                self.id,
                self.barcode,
                self.purchase_order.id,
                self.quantity,
                self.total_price
            )
        )


class PurchasePaymentMethod(models.Model):
    """ The payment methods chosen by the user/customer for a specific
    purchase order
    """

    purchase_order = models.ForeignKey(
        PurchaseOrder, on_delete=models.CASCADE,
        verbose_name=gettext_lazy('PurchaseOrder')
    )
    payment_method = models.ForeignKey(
        PaymentMethod, on_delete=models.PROTECT,
        verbose_name=gettext_lazy('PaymentMethod')
    )
    value = models.DecimalField(
        max_digits=8, decimal_places=3, verbose_name=gettext_lazy('Value')
    )

    class Meta:
        """ PurchasePaymentMethod's Meta class """

        verbose_name = gettext_lazy('PurchasePaymentMethod')
        verbose_name_plural = gettext_lazy('PurchasePaymentMethods')

    def __str__(self):
        return 'PurchasePaymentMethod {} - order {}'.format(
            self.id, self.purchase_order.id
        )

    def __repr__(self):
        return (
            'PurchasePaymentMethod(id={},purchase_order={},'
            'payment_method={},value={})'.format(
                self.id,
                self.purchase_order.id,
                self.payment_method.description,
                self.value
            )
        )

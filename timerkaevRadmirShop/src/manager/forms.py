""" Manager app forms module """

from django import forms

from website.models import Category, Product


class CategoryEditForm(forms.ModelForm):
    """ ModelForm for the Category model administration """

    class Meta:
        """ CategoryEditForm's Meta class """

        model = Category
        fields = ['description']


class ProductEditForm(forms.ModelForm):
    """ Модельная форма для администрирования модели продукта """

    class Meta:
        """ Мета-класс ProductEditForm """

        model = Product
        fields = [
            'barcode', 'title', 'description',
            'image', 'price', 'category'
        ]

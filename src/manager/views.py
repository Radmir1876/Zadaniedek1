""" Manager app views module """

from django.shortcuts import get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, TemplateView, \
    DeleteView

from website.models import Category, Product
from .forms import CategoryEditForm, ProductEditForm


class IndexView(TemplateView):
    """ Просмотр приложения Manager для главной страницы """

    template_name = 'index.html'


class CategoriesManagementView(ListView):
    """ Просмотр списка для администрирования модели категории"""

    template_name = 'categories_management.html'
    context_object_name = 'categories'

    def get_queryset(self):
        """ Возвращает список экземпляров категории """

        queryset = Category.objects.all()
        return queryset

class CategoryEditView(UpdateView):
    """ Просмотр для редактирования экземпляра определенной категории """

    template_name = 'category_edit.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('manager:categories')

    def form_valid(self, form):
        """ Проверьте, действительна ли форма, а затем сохраните ее """

        form.save()
        return super(CategoryEditView, self).form_valid(form)

    def get_object(self, queryset=None):
        """ Возвращает экземпляр категории на основе заданного идентификатора """

        id = self.kwargs.get('id', None)
        instance = get_object_or_404(Category, id=id)
        return instance


class CategoryDeleteView(DeleteView):
    """ Просмотр для удаления экземпляра определенной категории """

    template_name = 'confirm_delete.html'
    model = Category
    success_url = reverse_lazy('manager:categories')


class ProductsManagementView(ListView):
    """ Просмотр списка для администрирования модели продукта """

    template_name = 'products_management.html'
    context_object_name = 'products'

    def get_queryset(self):
        """ Возвращает список экземпляров продукта """

        queryset = Product.objects.all()
        return queryset


class ProductEditView(UpdateView):
    """ Просмотр для редактирования конкретного экземпляра продукта """

    template_name = 'product_edit.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('manager:products')

    def form_valid(self, form):
        """ Проверьте, действительна ли форма, а затем сохраните ее """

        form.save()
        return super(ProductEditView, self).form_valid(form)

    def get_object(self, queryset=None):
        """ Возвращает экземпляр категории, основанный на заданном слое """

        slug = self.kwargs.get('slug', None)
        instance = get_object_or_404(Product, slug=slug)
        return instance


class ProductDeleteView(DeleteView):
    """ Просмотр для удаления конкретного экземпляра продукта """

    template_name = 'confirm_delete.html'
    model = Product
    success_url = reverse_lazy('manager:products')

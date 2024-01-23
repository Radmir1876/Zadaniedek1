
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    """ Форма для заполнения регистрационных полей пользователей """

    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.'
    )
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.'
    )
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.'
    )

    class Meta:
        """ Мета-класс формы регистрации """

        model = User
        fields = (
            'username', 'first_name', 'last_name',
            'email', 'password1', 'password2',
        )
#class SignUpForm(UserCreationForm)::
#Этот класс наследуется от UserCreationForm, который является встроенным классом Django для создания формы
#регистрации пользователя.
#class Meta:: Это вложенный класс, который определяет метаданные для формы

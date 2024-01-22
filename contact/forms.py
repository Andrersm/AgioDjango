from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from contact.models import Contact




class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={'accept': 'image/*'}), required=False
                )
 
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name


class RegisterForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'first_name', 'last_name',
                   'password1', 'password2')
        error_messages = {
            'username': {
                'unique': 'Esse nome de usuário já existe',
                'required': 'Esse campo é obrigatório'
            },
            'email': {
                'unique': 'Esse e-mail já existe',
                'required': 'Esse campo é obrigatório'
            },
            'password1': {
                'required': 'Esse campo é obrigatório'
            },
            'password2': {
                'required': 'Esse campo é obrigatório'
            }
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email == '':
            self.add_error('email', ValidationError('Esse campo é obrigatório'))
        if User.objects.filter(email=email).exists():
            self.add_error('email', ValidationError('Esse e-mail já existe'))

        return email

    def clean_is_staff(self):
        return False

    def clean_is_superuser(self):
        return False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'O nome deve contar mais de 2 caracteres'
        }
    )
    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Required.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Use the same password as before.',
        required=False,
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não batem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )

        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(errors)
                )

        return password1
    

class LoanForm(forms.ModelForm):

    total_amount = forms.DecimalField(
        max_digits=10, decimal_places=2,
        required=True,
        min_value=1,
        label='Valor do emprestimo',
        widget=forms.NumberInput(
            attrs={'class':'form-control'}
        )
    )
    total_installments = forms.IntegerField(
        required=True,
        min_value=1,
        label='Total de parcelas',
        widget=forms.NumberInput(
            attrs={'class':'form-control'}
        )
    )
    owner = forms.ModelChoiceField(
        queryset=Contact.objects.all(),
        required=True,
        label='Dono do emprestimo',
        help_text='Obrigatorio',
        widget=forms.Select(
            attrs={'class':'form-control'}
        )
    )
    def __init__(self, user, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)
        self.fields['owner'].queryset = models.Contact.objects.filter(owner=user)
    class Meta:
        model = models.Loan
        fields = ('total_amount', 'total_installments', 'owner', 'fees', 'days', 'loan_date')
        widgets = {'owner': forms.Select(attrs={'class':'form-control'})}

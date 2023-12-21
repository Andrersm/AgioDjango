from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)

# Depois
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)


class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Usuarios'
        verbose_name = 'Usuario'

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              blank=True, null=True)
    

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Loan(models.Model):
    class Meta:
        verbose_name_plural = 'Emprestimos'
        verbose_name = 'Emprestimo'
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_date = models.DateField(default=timezone.now)
    total_installments = models.IntegerField()
    owner = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return f'{self.owner}'
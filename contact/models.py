from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User






class Contact(models.Model):
    class Meta:
        verbose_name_plural = 'Usuarios'
        verbose_name = 'Usuario'
    
    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, blank=True,
                                  verbose_name='Sobrenome')
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=254, verbose_name='Email')
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, verbose_name='Descrição')
    show = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, verbose_name='Imagem')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    


class Loan(models.Model):
    class Meta:
        verbose_name_plural = 'Emprstimos'
        verbose_name = 'Emprestimo'
    total_amount = models.DecimalField(max_digits=10, decimal_places=2,
                                       verbose_name='Valor')
    loan_date = models.DateField(default=timezone.now)
    total_installments = models.IntegerField(verbose_name='Parcelas')
    owner = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True,
                              verbose_name='Dono do emprestimo')
    fees = models.DecimalField(max_digits=10, decimal_places=0, default=0,
                               verbose_name='Taxa de juros')
    days = models.IntegerField(default=0, verbose_name='Dias')

    def __str__(self) -> str:
        return f'{self.owner}'

   
class Parcelas(models.Model):
    class Meta:
        verbose_name_plural = 'Parcelas'
        verbose_name = 'Parcela'
    amount_per_installment = models.DecimalField(max_digits=10,
                            decimal_places=2, null=True)
    paid = models.BooleanField(default=False,)
    owner = models.ForeignKey(Loan, on_delete=models.SET_NULL, null=True)
    owner_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    installment_date = models.DateField(default=timezone.now)
    def __str__(self) -> str:
        return f'{self.owner}'
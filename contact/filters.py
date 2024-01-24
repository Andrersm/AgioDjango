import django_filters
from contact.models import Parcelas

class ParcelasFilter(django_filters.FilterSet):
    intervalo_de_datas = django_filters.DateFromToRangeFilter(field_name='installment_date', label='Intervalo de datas')
    class Meta:
        model = Parcelas
        fields = ['intervalo_de_datas',]
    

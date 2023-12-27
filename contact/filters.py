import django_filters
from contact.models import Parcelas

class ParcelasFilter(django_filters.FilterSet):
    campo_de_filtro = django_filters.DateFromToRangeFilter()
    class Meta:
        model = Parcelas
        fields = ['installment_date']

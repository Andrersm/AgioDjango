from django.contrib import admin
from .models import Contact,Loan, Parcelas
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'phone', 'owner',
    ordering = 'id',
    #list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_display_links = 'id', 'phone',

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = 'id','owner', 'total_amount', 'loan_date',
    ordering = 'id',
    list_display_links = 'owner',

@admin.register(Parcelas)
class ParcelasAdmin(admin.ModelAdmin):
    list_display = 'id', 'paid', 'owner', 'installment_date' 
    ordering = 'installment_date',
    list_display_links = 'id',
    search_fields = 'installment_date',
    list_filter = 'installment_date',

    
   
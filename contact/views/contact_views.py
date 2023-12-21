from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact, Loan
from django.db.models import Q
from django.core.paginator import Paginator

import re


def replace_all(text: str):
    text = re.sub(r'[.,;:?!-/()]', '', text)
    return text


def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
        }
    return render(request, 'contact/index.html', context)

def contact(request, contact_id):
    single_contact = get_object_or_404(Contact, pk=contact_id)
    loans = Loan.objects.filter(owner=single_contact)
    contact_site = f'{single_contact.first_name}  {single_contact.last_name} - '

    context = {
        'contact': single_contact,
        'loans': loans,
        'site_title': contact_site
        }
    return render(request, 'contact/contact.html', context)

def search(request):
    search_value1 = request.GET.get('q', '').strip()
    search_value = replace_all(search_value1)

    if search_value == '':
        return redirect('contact:index')
    contacts = Contact.objects.filter(show=True)\
        .filter(Q(first_name__icontains=search_value) |
                Q(last_name__icontains=search_value) |
                Q(email__icontains=search_value) |
                Q(phone__icontains=search_value))\
        .order_by('-id')\
    
    paginator = Paginator(contacts, 10) 

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'search - ',
        'search_value': search_value,
        }
    return render(request, 'contact/index.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from contact.forms import ContactForm, LoanForm
from django.urls import reverse
from contact.models import Contact, Loan
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato salvo com sucesso!')
            return redirect('contact:index',)

        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
            'form': ContactForm(),
            'form_action': form_action,
        }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        context = {
            'form': form,
            'form_action': form_action,
        }

        if form.is_valid():
            form.save()
            messages.success(request, 'Contato atualizado com sucesso!')
            return redirect('contact:update', contact_id=contact.pk)

        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
            'form': ContactForm(instance=contact),
            'form_action': form_action,
        }

    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        messages.success(request, 'Contato excluído com sucesso!')
        return redirect('contact:index')

    return render(
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation,
        }
    )

@login_required(login_url='contact:login')
def loancreate(request):
    form_action = reverse('contact:create_loan')

    if request.method == 'POST':
        form = LoanForm(request.user, request.POST, request.FILES)  
        if form.is_valid():
            loan = form.save(commit=False)
            loan.save()
            messages.success(request, 'Empréstimo criado com sucesso!')
            return redirect('contact:index')
    else:
        form = LoanForm(user=request.user) 

    context = {
        'form': form,
        'form_action': form_action,
    }

    return render(request, 'contact/create_loan.html', context)
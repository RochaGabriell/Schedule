from typing import Any, Dict
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from contact.models import Contact
"""
def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .all().order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'site_title': 'Contatos -', 'object_list': page_obj}

    return render(request, 'contact/index.html', context, status=200)
"""


class ContactView(ListView):
    model = Contact
    template_name = 'contact/index.html'
    paginate_by = 10
    status = 200

    def get_queryset(self):
        queryset = Contact.objects.filter(show=True).all().order_by('-id')
        return queryset


"""
def contact(request, id):
    # sigle_contact = Contact.objects.filter(id=id).first()
    sigle_contact = get_object_or_404(Contact.objects.filter(id=id, show=True))
    title = f'{sigle_contact.first_name} {sigle_contact.last_name} - '
    context = {'site_title':  title, 'object': sigle_contact}
    return render(request, 'contact/contact.html', context, status=200)
"""


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact.html'
    status = 200

    def get_queryset(self):
        queryset = Contact.objects.filter(show=True).all()
        return queryset


"""
def search(request):
    query = request.GET.get('q', '').strip()

    if query == '':
        return redirect('contact:list_contact')  # 302

    sigle_contact = Contact.objects\
        .filter(show=True)\
        .filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )\
        .all().order_by('-id')

    paginator = Paginator(sigle_contact, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'title': 'Search Contact', 'object_list': page_obj, 'query': query}

    return render(request, 'contact/index.html', context, status=200)
"""


class SearchView(ListView):
    model = Contact
    template_name = 'contact/index.html'
    paginate_by = 10
    ordering = ['-id']
    status = 200

    def get_queryset(self):
        query = self.request.GET.get('q', '').strip()

        if query == '':
            return redirect('contact:list_contact')  # 302
        
        queryset = Contact.objects\
            .filter(show=True)\
            .filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )\
            .all().order_by('-id')

        return queryset
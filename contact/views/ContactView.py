from typing import Any
from django.db import models
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from contact.models import Contact
"""
def index(request):
    contacts = Contact.objects\
        .filter(show=True)\
        .all().order_by('-id')[:10]

    context = {'site_title': 'Contatos -', 'object_list': contacts}

    return render(request, 'contact/index.html', context, status=200)
"""


class ContactView(ListView):
    model = Contact
    template_name = 'contact/index.html'
    paginate_by = 10
    ordering = ['-id']
    status = 200

    def get_queryset(self):
        return Contact.objects.filter(show=True).all()

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        return context


"""


def contact(request, id):
    # sigle_contact = Contact.objects.filter(id=id).first()
    sigle_contact = get_object_or_404(Contact.objects.filter(id=id, show=True))
    context = {'site_title': f'{sigle_contact.first_name} {sigle_contact.last_name} - ', 'object': sigle_contact}
    return render(request, 'contact/contact.html', context, status=200)
"""


class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact.html'
    status = 200

    def get_queryset(self):
        return Contact.objects.filter(show=True).all()

    def get_context_data(self, **kwargs):
        context = super(ContactDetailView, self).get_context_data(**kwargs)
        return context


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
        .all().order_by('-id')[:10]

    context = {'title': 'Search Contact', 'object_list': sigle_contact}

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
            return redirect('contact:list_contact') # 302

        return Contact.objects\
            .filter(show=True)\
            .filter(
                Q(first_name__icontains=query) |
                Q(last_name__icontains=query)
            )\
            .all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        return context
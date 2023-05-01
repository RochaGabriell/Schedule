from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from contact.models import Contact
from contact.forms import ContactForm

"""
def ContactCreateView(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {'form': form}

        if form.is_valid():
            form.save()
            return redirect('contact:create_contact')

        return render(request, 'contact/create.html', context)

    context = {'form': ContactForm()}

    return render(request, 'contact/create.html', context)
"""

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create.html'
    success_url = reverse_lazy('contact:list_contact')
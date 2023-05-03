from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse

from contact.models import Contact
from contact.forms import ContactForm


def ContactCreateView(request):

    form_action = reverse('contact:create_contact')

    if request.method == 'POST':
        form = ContactForm(request.POST)

        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update_contact', pk=contact.pk)

        return render(request, 'contact/create.html', context)

    context = {'form': ContactForm(), 'form_action': form_action}

    return render(request, 'contact/create.html', context)


"""
class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create.html'
    
    def get_success_url(self):
        return reverse('contact:update_contact', args=(self.object.pk, ))
"""


def ContactUpdateView(request, pk):
    contact = get_object_or_404(Contact, pk=pk, show=True)
    form_action = reverse('contact:update_contact', args=(pk, ))

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)

        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            contact = form.save()
            return redirect('contact:update_contact', pk=contact.pk)

        return render(request, 'contact/create.html', context)

    context = {'form': ContactForm(instance=contact), 'form_action': form_action}

    return render(request, 'contact/create.html', context)


"""
class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/create.html'
    success_url = reverse_lazy('contact:update_contact')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Contact, pk=pk, show=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_action'] = reverse('contact:update_contact', args=(self.object.pk, ))
        return context
"""

def ContactDeleteView(request, pk):
    contact = get_object_or_404(Contact, pk=pk, show=True)

    if request.method == 'POST':
        contact.show = False
        contact.save()
        return redirect('contact:list_contact')

    return render(request, 'contact/index.html')
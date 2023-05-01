from django.urls import path
# from .views import index, contact, search
from .views import ContactView, ContactDetailView, SearchView

app_name = 'contact'

urlpatterns = [
    # path('', index, name='list_contact'),
    # path('<int:id>/', contact, name='contact'),
    # path('search/', search, name='search'),
    path('', ContactView.as_view(), name='list_contact'),
    path('search/', SearchView.as_view(), name='search'),

    # Contact CRUD
    path('contact/<int:pk>/detail/', ContactDetailView.as_view(), name='contact'),
    path('contact/create/', ContactDetailView.as_view(), name='create_contact'),
    path('contact/<int:pk>/update/', ContactDetailView.as_view(), name='update_contact'),
    path('contact/<int:pk>/delete/', ContactDetailView.as_view(), name='delete_contact'),
]
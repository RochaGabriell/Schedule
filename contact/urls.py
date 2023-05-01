from django.urls import path
# from .views import index, contact, search
from .views import ContactView, ContactDetailView, SearchView

app_name = 'contact'

urlpatterns = [
    path('', ContactView.as_view(), name='list_contact'),
    # path('', index, name='list_contact'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact'),
    # path('<int:id>/', contact, name='contact'),
    path('search/', SearchView.as_view(), name='search'),
    # path('search/', search, name='search'),
]
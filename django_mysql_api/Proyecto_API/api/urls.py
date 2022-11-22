from django.urls import path 
from .views import CompanyView

urlpatterns = [
    path('company', CompanyView.as_view(), name= 'companies_list'),
    path('company/<int:id>', CompanyView.as_view(), name= 'companies_process')

]
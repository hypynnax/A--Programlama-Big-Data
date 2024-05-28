from . import views
from django.urls import path

app_name = 'BigData'

urlpatterns = [
    path('generatedData/', views.generatedData, name='generatedData'),
    path('generatedData/<str:code>/<str:category>', views.generatedDataCountry, name='generatedDataCountry'),
    path('generatedData/<str:category>', views.generatedDataCountries, name='generatedDataCountries'),
]
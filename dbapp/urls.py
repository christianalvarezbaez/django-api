# myapp/urls.py
from django.urls import path
from .views import (
    time_series,
    pie_gender,
    boxes_gender,
    top_clients,
    age_range,
    age_histogram,
)

urlpatterns = [
   path('time_series/', time_series, name='time_series'),
   path('pie_gender/', pie_gender, name='pie_gender'),
   path('boxes_gender/', boxes_gender, name='boxes_gender'),
   path('top_clients/', top_clients, name='top_clients'),
   path('age_range/', age_range, name='age_range'),
   path('age_histogram/', age_histogram, name='age_histogram'),
]


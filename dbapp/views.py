# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.db.models.functions import Coalesce
from dbapp.models import TimeSeriesMaterializedView, PieGenderMaterializedView, BoxesGenderMaterializedView, TopClientsMaterializedView, AgeRangeMaterializedView, AgeHistogramMaterializedView
from django.db.models.functions import TruncDate
from django.db.models import Case, When, Value,  Sum, FloatField
from django.db import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.cache import cache_page
from dbapp.serializers import TimeSeriesSerializer, PieGenderSerializer, BoxesGenderSerializer, TopClientsSerializer, AgeRangeSerializer, AgeHistogramSerializer 

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def time_series(request):
    result_data = TimeSeriesMaterializedView.objects.all()
    serializer = TimeSeriesSerializer(result_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def pie_gender(request):
    result_data = PieGenderMaterializedView.objects.all()
    serializer = PieGenderSerializer(result_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def boxes_gender(request):
    result_data = BoxesGenderMaterializedView.objects.all()
    serializer = BoxesGenderSerializer(result_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def top_clients(request):
    result_data = TopClientsMaterializedView.objects.all()
    serializer = TopClientsSerializer(result_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def age_range(request):
    result_data = AgeRangeMaterializedView.objects.all()    
    serializer = AgeRangeSerializer(result_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@cache_page(60 * 15)  # Cache for 15 minutes
def age_histogram(request):
    result_data = AgeHistogramMaterializedView.objects.all()    
    serializer = AgeHistogramSerializer(result_data, many = True)
    return Response(serializer.data)



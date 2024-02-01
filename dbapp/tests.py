from django.test import TestCase

# Create your tests here.
from django.db.models import Sum, ExpressionWrapper, FloatField
from django.db.models.functions import Coalesce
from dbapp.models import Transactions, Clients
from django.db.models.functions import TruncDate
from django.db.models import Case, When, Value, IntegerField, Sum
from django.db import models



#SELECT DATE(time_stamp) AS date,SUM(amount) FROM transactions GROUP BY date ORDER BY date DESC LIMIT 7
result = Transactions.objects.annotate(date=TruncDate('time_stamp')) \
    .values('date') \
    .annotate(amount_sum=Sum('amount')) \
    .order_by('-date')[:7]

#SELECT gender, SUM(amount) FROM clients JOIN transactions ON clients.id_client = transactions.id_client GROUP BY gender ORDER BY sum(amount) DESC' 
Clients.objects.values('gender').annotate(amount_sum=Sum('transactions__amount')).order_by('-amount_sum')
Transactions.objects.values('id_client__gender').annotate(amount_sum=Sum('amount')).order_by('-amount_sum')

# SELECT gender, amount FROM transactions JOIN clients ON clients.id_client = transactions.id_client
#Estos dos hacen lo mismo
Transactions.objects.values('id_client__gender','amount')
Clients.objects.values('gender','transactions__amount')


#SELECT clients.id_client, name, SUM(amount) AS amount FROM clients JOIN transactions ON clients.id_client = transactions.id_client GROUP BY clients.id_client, name ORDER BY sum(amount) DESC LIMIT 10'
top_clients = Clients.objects.annotate(
    total_amount=ExpressionWrapper(
        Coalesce(Sum('transactions__amount'), 0),output_field=FloatField())
        ).order_by('-total_amount'
                  ).values('id_client', 'name', 'total_amount')[:10]


#Top ages with transactions

age_ranges = [
    (18, 25, '18-25'),
    (25, 30, '25-30'),
    (30, 35, '30-35'),
    (35, 40, '35-40'),
    (40, 45, '40-45'),
    (45, 50, '45-50'),
    (50, 55, '50-55'),
    (55, 60, '55-60'),
    (60, 65, '60-65'),
]

age_case = Case(
    *[When(age__range=(start, end), then=Value(age_range)) for start, end, age_range in age_ranges],
    default=Value('>65'),
    output_field=models.CharField()  # Adjust the output_field based on your actual field type
)
result = Clients.objects.annotate(
    age_range=age_case
).values('age_range').annotate(
    total_amount=Sum('transactions__amount')
).order_by('-total_amount')

#SELECT age, SUM(amount) amount FROM clients JOIN transactions ON clients.id_client = transactions.id_client GROUP BY age ORDER BY age ASC
result = Clients.objects.values('age').annotate(
    total_amount = Sum('transactions__amount')
    ).order_by('-total_amount').values('age','total_amount')
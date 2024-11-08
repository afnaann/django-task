from orm_series.models import Restaurant,Rating,Sales,User
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    # print(Restaurant.objects.count())
    # print(Rating.objects.count())
    # print(Sales.objects.count())
    
    
    pprint(connection.queries)
    
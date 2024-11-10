from orm_series.models import Restaurant,Rating,Sales, Staff,User
from django.utils import timezone
from django.db import connection
from pprint import pprint

def run():
    # add, count, all, remove, set, clear, create, filter
    
    # x = staff.restaurants.set(Restaurant.objects.filter(name__istartswith='c'))
     
    # print(Restaurant.objects.count())
    # print(Rating.objects.count())
    # print(Sales.objects.count())

    # print(restaurant)
    # pprint(restaurant.values())
    # pprint(restaurant.values_list())
    
    restaurants = Restaurant.objects.values('name')
    
    pprint(restaurants)
    

    # print(x)
    pprint(connection.queries)
    
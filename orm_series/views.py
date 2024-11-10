from django.shortcuts import render

from orm_series.models import Restaurant,Rating

def home(request):
    restaurants = Restaurant.objects.filter(rating__rating=5).prefetch_related('rating_set','sales_set')
    # rest = Restaurant.objects.prefetch_related('rating_set')
    # rate = Rating.objects.all()
    context = {
        'restaurants':restaurants
    }
    
    return render(request, 'home.html',context)



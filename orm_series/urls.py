
from django.urls import path
from orm_series import views


urlpatterns = [
    path('',views.home)
]

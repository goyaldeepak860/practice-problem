from django.urls import path
from . import views
# from .views import HomePageView, CarpartView, CarwheelView, SingleView, SinglPartView, CustomerView, ThanksView, CustomerUpdateView  # new
# from .views import CustomerListView, SingleCustView, CustDeleteView, DropPartView
urlpatterns = [
    path('movielist/', views.jointables, name='tablesjoin'),
    path('movielist2/', views.jointhreetables, name='jointhreetables'),
]
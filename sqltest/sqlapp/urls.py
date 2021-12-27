from django.urls import path
from . import views
# from .views import HomePageView, CarpartView, CarwheelView, SingleView, SinglPartView, CustomerView, ThanksView, CustomerUpdateView  # new
# from .views import CustomerListView, SingleCustView, CustDeleteView, DropPartView
urlpatterns = [
    path('movielist/', views.jointables, name='tablesjoin'),
    path('movielist2/', views.jointhreetables, name='jointhreetables'),
    path('movielist3/', views.jointhreetables_manytomany, name='jointhreetablesmanytomany'),
    path('movielist4/', views.aggre_hav, name='aggre_hav'),
    path('movielist5/', views.jointhreetables_manytomanynew, name='jointhreetables_manytomanynew')
    
]
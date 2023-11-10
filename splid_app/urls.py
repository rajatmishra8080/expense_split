from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('addcontact/',views.addcontact,name='addcontact'),
    path('overview/',views.overview,name='overview'),
    path('expense/',views.expense,name='expense'),
    path('settleup/',views.settle_up_report,name='settleup'),
    path('reset-records/', views.reset_records, name='reset-records'),
    path('error/',views.error,name='error'),
    path('simplify/',views.simplify_expenses,name='simplify'),
    
]
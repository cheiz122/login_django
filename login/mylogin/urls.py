from django.urls import path
from . import views
urlpatterns = [ 
    
    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('home/add_record',views.add_name,name='add_record')
    
    
              
              
 ]
   

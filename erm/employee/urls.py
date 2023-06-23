from django.contrib import admin
from django.urls import path
from employee.views import *

urlpatterns = [
    path('',index, name='index'),
    path('registration',registration,name='registration'),
    path('manager_login',manager_login, name='manager_login'),
    path('manager_home',manager_home, name='manager_home'),
    path('profile',profile, name='profile'),
    path('logout',Logout, name='logout'),
    path('addemployee', addemployee, name='addemployee'),
    path('admin_login',admin_login, name='admin_login'),
    path('change_password',change_password, name='change_password'),
    path('view_employee',view_employee, name='view_employee'),
    path('delete/<int:id>/',delete, name='delete'),
    path('update/<int:id>/',update, name='update'),
    path('do_emp_update/<int:id>/', do_emp_update, name='do_emp_update'),
    path('employee_login',employee_login, name='employee_login'),
    path('others_login',others_login, name='others_login'),
    path('admin_home',admin_home, name='admin_home'),
    path('admin_changepassword',admin_changepassword, name='admin_changepassword'),
    path('admin_logout',admin_logout, name='admin_logout'),
    path('admin_viewmanagers',admin_viewmanagers, name='admin_viewmanagers'),
    
        
]
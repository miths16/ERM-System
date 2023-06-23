
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        cd = request.POST['corpid']
        em = request.POST['emailid']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name=fn, last_name=ln, username= em, password=pwd)
            ManagerDetail.objects.create(user = user, corpid=cd)
            error = "no"
            
        except:
            error = "yes"
        
    return render(request, 'registration.html', locals())

def manager_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        
        user = authenticate(username=u, password=p)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'manager_login.html', locals())

def employee_login(request):
    return render(request, 'employee_login.html')

def others_login(request):
    return render(request, 'others_login.html')

def manager_home(request):
    if not request.user.is_authenticated:
        return redirect('manager_login')
    return render (request, 'manager_home.html')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('manager_login')
    error = ""
    user=request.user
    manager=ManagerDetail.objects.get(user=user)
    if request.method == "POST":
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        cid = request.POST['corpid']
        dept = request.POST['department']
        ct = request.POST['contact']
        jd = request.POST['jdate']
        gender = request.POST['gender']
        
        manager.user.first_name=fname
        manager.user.last_name=lname
        manager.corpid=cid
        manager.department=dept
        manager.contact=ct
        manager.gender=gender
        manager.joiningdate=jd
        
        try:
            manager.save()
            manager.user.save()
            error = "no"
            
        except:
            error = "yes"
    return render(request, 'profile.html', locals())

def Logout(request):
    logout(request)
    return redirect ('index')

def addemployee(request):
    if not request.user.is_authenticated:
        return redirect('manager_login')
    error = ""
    
    if request.method == "POST":
        fullname = request.POST['fullname']
        empid = request.POST['empid']
        emailid = request.POST['emailid']
        mobile = request.POST['mobile']
        department = request.POST['department']
        designation = request.POST['designation']
        joiningdate = request.POST['joiningdate']
        gender = request.POST['gender']
        
        
        try:
            employee = EmployeeData.objects.create(fullname=fullname, emp_id=empid, emailid=emailid, mobile=mobile, department=department, designation=designation, gender=gender, joiningdate=joiningdate,)
            employee.save()
            error = "no"
            
        except:
            error = "yes"
            
    return render(request, 'addemployee.html', locals())

def admin_login (request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render (request, 'admin_login.html')

def change_password(request):
    if not request.user.is_authenticated:
        return redirect('manager_login')
    
    error=""
    user=request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        print(error)
        
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
                
            else:
                error="not"
                
        except:
            error="yes"
    return render(request, 'change_password.html',locals())

def view_employee(request):
    if not request.user.is_authenticated:
        return redirect('manager_login')
    context = {'view_employee': EmployeeData.objects.all()}
    return render(request, 'view_employee.html', context)

def delete(request, id):
    employee = EmployeeData.objects.get(pk=id)
    employee.delete()
    return redirect('view_employee') 

def update(request, id):
    employee = EmployeeData.objects.get(pk=id)
    return render(request, 'emp_update.html',{'employee':employee})

# def update(request, id):
#     return redirect('addemployee', id=id)


def do_emp_update(request,id):
    if request.method == 'POST':
        fullname=request.POST.get('fullname')
        emp_id=request.POST.get('emp_id')
        emailid=request.POST.get('emailid')
        mobile=request.POST.get('mobile')
        department=request.POST.get('department')
        designation=request.POST.get('designation')
        joiningdate=request.POST.get('joiningdate')
        gender=request.POST.get('gender')
        
        employee=EmployeeData.objects.get(pk=id)
        
        employee.fullname=fullname
        employee.emp_id=emp_id
        employee.emailid=emailid
        employee.mobile=mobile
        employee.department=department
        employee.designation=designation
        employee.joiningdate=joiningdate
        employee.gender=gender
        
        employee.save()
        
        
        print(fullname)
    return redirect('view_employee')

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['pwd']
        
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    return render(request, 'admin_login.html', locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render (request, 'admin_home.html')

def admin_changepassword(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    error=""
    user=request.user
    if request.method == "POST":
        c = request.POST['currentpassword']
        n = request.POST['newpassword']
        
        print(error)
        
        try:
            if user.check_password(c):
                user.set_password(n)
                user.save()
                error="no"
                
            else:
                error="not"
                
        except:
            error="yes"
            
    context = {
        'error': error,
        'user': user,
    }
    return render(request, 'admin_changepassword.html',context)

def admin_logout(request):
    return redirect('admin_login')

def admin_viewmanagers(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    context = {
        'managers': ManagerDetail.objects.all(),
        'current_user': request.user
    }
    
    return render(request, 'admin_viewmanagers.html', context)



    
    
    


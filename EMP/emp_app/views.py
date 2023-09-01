from django.shortcuts import render,redirect
from emp_app.models import Employee

# Create your views here.
def index(request):
    # fetch employee
    employess = Employee.objects.all()
    return render(request, "home.html", {"employees": employess})

def add_emp(request):
    if request.method == "POST" :
        # get data from the request
        employee_name = request.POST.get("employee_name")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        is_working = request.POST.get("is_working")
        department = request.POST.get("department")
        if is_working is None:
            is_working = False
        else:
            is_working = True
        # create model object and set the data
        newEmployee = Employee(employee_name=employee_name, employee_address=employee_address, employee_phone=employee_phone, department=department, is_working=is_working)
        
        # save the object
        newEmployee.save()

        return redirect("/")
    return render(request, "add_emp.html")

def del_emp(request, emp_id):
    emp = Employee.objects.get(pk=emp_id)
    emp.delete()
    return redirect("/")

def update_emp(request, emp_id):
    if request.method == "POST":
        employee_name = request.POST.get("employee_name")
        employee_phone = request.POST.get("employee_phone")
        employee_address = request.POST.get("employee_address")
        is_working = request.POST.get("is_working")
        department = request.POST.get("department")
        if is_working is None:
            is_working = False
        else:
            is_working = True
        emp = Employee.objects.get(pk=emp_id)
        emp.employee_name = employee_name
        emp.employee_phone = employee_phone
        emp.employee_address = employee_address
        emp.is_working = is_working
        emp.department = department
        emp.save()

        return redirect("/")
    emp = Employee.objects.get(pk=emp_id)
    return render(request, "update_emp.html", {"emp": emp})

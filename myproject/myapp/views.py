from django.shortcuts import render 
from .models import EmployeeModel  
from .forms import EmployeeForm


# Create your views here.
def insert_employee(request):
    context ={}# dictionary for initial data with field names as keys
    ob_form = EmployeeForm(request.POST or None)
    if ob_form.is_valid():
        ob_form.save()
        return HttpResponse("Data Saved")
    context['form']= ob_form
    return render(request, "insert_employee.html", context)  


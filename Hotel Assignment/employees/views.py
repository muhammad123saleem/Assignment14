from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . forms import CreateEmployee
from . models import Employee

# Create your views here.

def index_view(request):
    employees = Employee.objects.all() 
    return render(request, 'employees/index_view.html',{'employees':employees})

def create_view(request):
    if request.method == 'POST':
        form = CreateEmployee(request.POST, request.FILES)
        if form.is_valid():
            newEmployee = form.save()
            messages.success(request, 'Employee create successfully!')
            return redirect('employees:index_view')
    else:
        form = CreateEmployee()
    return render(request,'employees/create_view.html',{'form':form})
def update_view(request , pk):
    instance = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = CreateEmployee(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data updated successfully!')
            return redirect('employees:index_view')
    else:
        form = CreateEmployee(instance=instance)
    return render(request, 'employees/update_view.html', {'form': form})

def delete_view(request,pk):
    instance = get_object_or_404(Employee,pk=pk)
    instance.delete()
    messages.success(request, 'Data deleted successfully!')
    return redirect('employees:index_view')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

@login_required
def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/accounts/login/')
    # get all employees and pass as 'data' because your template uses data
    data = Employee.objects.all().order_by('-id')
    return render(request, 'home.html', {'data': data})
@login_required
def add(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')   # or redirect('/' ) depending on url names
    else:
        form = EmployeeForm()
    return render(request, 'add.html', {'form': form})

@login_required
def edit(request, id):
    emp = get_object_or_404(Employee, id=id)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm(instance=emp)

    return render(request, 'edit.html', {'form': form})

@login_required
def delete(request, id):
    emp = get_object_or_404(Employee, id=id)
    emp.delete()
    return redirect('home')
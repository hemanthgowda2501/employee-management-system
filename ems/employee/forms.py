from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name','emp_id','email','phone','department','salary','joining_date']
        widgets = {
            'joining_date': forms.DateInput(attrs={'type':'date'}),
        }

    def clean_salary(self):
        s = self.cleaned_data.get('salary')
        if s is not None and s < 0:
            raise forms.ValidationError("Salary must be positive")
        return s
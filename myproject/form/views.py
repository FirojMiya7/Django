from django.shortcuts import redirect, render

from .models import Student
# Create your views here.

def home(request):
    students = Student.objects.all()
    # Left student html ko var ho right side ko student chai database dekhi aayeko data ho.
    return render(request, 'form/home.html', {'students': students})
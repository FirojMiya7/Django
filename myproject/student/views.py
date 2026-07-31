from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.

from .forms import StudentForm
from .models import Student


def student_list(request):
	students = Student.objects.order_by('first_name', 'last_name')
	return render(request, 'student/student_list.html', {'students': students})


def student_detail(request, pk):
	student = get_object_or_404(Student, pk=pk)
	return render(request, 'student/student_detail.html', {'student': student})


def student_create(request):
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('student:list')
	else:
		form = StudentForm()

	return render(request, 'student/student_form.html', {
		'form': form,
		'title': 'Create Student',
	})


def student_update(request, pk):
	student = get_object_or_404(Student, pk=pk)

	if request.method == 'POST':
		form = StudentForm(request.POST, instance=student)
		if form.is_valid():
			form.save()
			return redirect('student:detail', pk=student.pk)
	else:
		form = StudentForm(instance=student)

	return render(request, 'student/student_form.html', {
		'form': form,
		'student': student,
		'title': 'Update Student',
	})


def student_delete(request, pk):
	student = get_object_or_404(Student, pk=pk)

	if request.method == 'POST':
		student.delete()
		return redirect('student:list')

	return render(request, 'student/student_confirm_delete.html', {'student': student})
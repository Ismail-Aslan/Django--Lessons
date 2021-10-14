from student.models import Student
from .forms import StudentForm
from django.shortcuts import redirect, render
from django.contrib import messages



def index(request):
    return render(request, 'student/index.html')


def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid(): # eğer formda zorunlu kısımlar düzgün doldurulmuşsa
            form.save()
            messages.success(request, "Student added successfully")
            return redirect('student') # formu kaydettikten sonra urlsde name='student' demiştik oraya yönlendirdi
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
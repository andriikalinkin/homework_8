from django.http import HttpResponse
from django.shortcuts import render

from .forms import StudentForm
from .models import Student


# Create your views here.
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Students page</h1>")

    form = StudentForm()  # if request.method == "GET"
    return render(request, "student_add.html", {"form": form})


def students(request):
    all_students = Student.objects.all()
    return render(request, "students.html", {"all_students": all_students})

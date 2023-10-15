from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import StudentForm
from .models import Student


# Create your views here.
def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            student_create = Student.objects.create(
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                phone_number=request.POST["phone_number"],
            )
            student_create.save()
            return redirect("/students/")

    form = StudentForm()  # if request.method == "GET"
    return render(request, "student_add.html", {"form": form})


def students(request):
    all_students = Student.objects.all()
    return render(request, "students.html", {"all_students": all_students})

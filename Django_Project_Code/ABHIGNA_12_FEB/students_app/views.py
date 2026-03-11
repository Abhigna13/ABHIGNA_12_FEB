from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('students_app:dashboard')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'students_app/login.html')


def dashboard(request):
    students = Student.objects.all()
    context = {
        'total_students': students.count(),
        'male_students': students.filter(gender='Male').count(),
        'female_students': students.filter(gender='Female').count(),
    }
    return render(request, 'students_app/dashboard.html', context)


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students_app:student_list')
    else:
        form = StudentForm()
    return render(request, 'students_app/student_form.html', {'form': form, 'title': 'Add Student'})


def student_list(request):
    search_query = request.GET.get('search', '')
    students = Student.objects.all()
    if search_query:
        students = students.filter(
            Q(name__icontains=search_query) | 
            Q(branch__icontains=search_query) |
            Q(phone__icontains=search_query) |

        )
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'students_app/student_list.html', {'students': students, 'search_query': search_query})


def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students_app:student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students_app/student_form.html', {'form': form, 'title': 'Edit Student'})


def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('students_app:student_list')
    return render(request, 'students_app/delete_student.html', {'student': student})
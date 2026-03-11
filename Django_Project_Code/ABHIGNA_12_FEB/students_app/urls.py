from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'students_app'

urlpatterns = [
    # Login page
    path('', views.login_view, name='login'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Students CRUD
    path('list/', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),

    # Logout
    path('logout/', LogoutView.as_view(next_page='students_app:login'), name='logout'),
]
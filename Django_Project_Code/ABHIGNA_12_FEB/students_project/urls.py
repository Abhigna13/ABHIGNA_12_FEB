from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # VERY IMPORTANT
    path('',include('students_app.urls')),

]
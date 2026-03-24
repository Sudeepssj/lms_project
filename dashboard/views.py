from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from accounts.models import User
from courses.models import Course, Enrollment   # ✅ ADD THIS

@login_required(login_url='/accounts/login/')
def dashboard_view(request):
    user = request.user

    # ADMIN
    if user.is_superuser or user.role == 'admin':

        total_students = User.objects.filter(role='student').count()
        total_instructors = User.objects.filter(role='instructor').count()

        courses = Course.objects.all()

        return render(request, 'admin/dashboard.html', {
            'total_students': total_students,
            'total_instructors': total_instructors,
            'courses': courses
        })

    # INSTRUCTOR
    elif user.role == 'instructor':
        courses = Course.objects.filter(instructor=user)
        return render(request, 'instructor/dashboard.html', {
            'courses': courses
        })

    # STUDENT
    else:
        courses = Course.objects.all()  # all available courses
        enrollments = Enrollment.objects.filter(student=user)  # 👈 important

        return render(request, 'student/dashboard.html', {
            'courses': courses,
            'enrollments': enrollments
        })
    

from django.contrib.auth.decorators import login_required

@login_required
def admin_profile(request):
    return render(request, 'admin/profile.html', {
        'user': request.user
    })

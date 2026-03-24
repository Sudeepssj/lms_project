from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import *

# DASHBOARD (own courses)
@login_required
def instructor_dashboard(request):
    courses = Course.objects.filter(instructor=request.user)
    return render(request, 'instructor/dashboard.html', {
        'courses': courses
    })

# ADD COURSE
@login_required
def add_course(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        Course.objects.create(
            title=title,
            description=description,
            instructor=request.user
        )
        return redirect('/courses/instructor/')

    return render(request, 'instructor/add_course.html')

# EDIT COURSE
@login_required
def edit_course(request, id):
    course = get_object_or_404(Course, id=id, instructor=request.user)

    if request.method == 'POST':
        course.title = request.POST['title']
        course.description = request.POST['description']
        course.save()
        return redirect('/courses/instructor/')

    return render(request, 'instructor/edit_course.html', {
        'course': course
    })

# DELETE COURSE
@login_required
def delete_course(request, id):
    try:
        course = Course.objects.get(id=id, instructor=request.user)
        course.delete()
    except:
        pass

    return redirect('/courses/instructor/')


from django.contrib.auth.decorators import login_required

@login_required
def instructor_profile(request):
    return render(request, 'instructor/profile.html', {
        'user': request.user
    })




@login_required
def enroll_course(request, id):
    course = Course.objects.get(id=id)

    Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    return redirect('/')

from django.contrib.auth.decorators import login_required

@login_required
def student_profile(request):
    return render(request, 'student/profile.html', {
        'user': request.user
    })
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Course
# Create your views here.


def courses_page(request):
    range_values = range(1, 6)  # Example range values for the rating stars
    courses = Course.objects.all()

    return render(request, 'courses_microservice/courses.html', {
        'courses': courses,
        'range_values': range_values,
    })


def create_course_page(request):
    return render(request, 'courses_microservice/create-course.html')


def edit_course_page(request):
    return render(request, 'courses_microservice/edit-course.html')


def course_details_page(request, slug):

    # Fetch course details from the database using the course_id
    try:
        course = Course.objects.get(slug=slug)
    except Course.DoesNotExist:
        return HttpResponse("Course not found", status=404)

    return render(request, "courses_microservice/course-details.html", {
        "course": course,
    })

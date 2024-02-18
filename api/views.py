from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .services import getUsers, createUser, createCourse, getACourse, getCourses
from .serializers import CourseSerializer


def dummy_view(request):
    getUsers()
    return HttpResponse("This is a dummy response!")

@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    createUser()
    return HttpResponse("This is create user!")

@csrf_exempt
@require_http_methods(["GET", "POST"])
def courses(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        serializer = CourseSerializer(data=data)
        is_valid = serializer.is_valid()
        if not is_valid:
            print(serializer.errors)
            return JsonResponse(serializer.errors, status=400)
        else:
            validated_data = serializer.validated_data
            
            # Pass the validated data to your service function
            # Assuming `createCourse` is defined to accept a dictionary of course data
            course = createCourse(validated_data)
            
            # You might want to return some information about the newly created course
            # For example, returning a success message with course ID (if applicable)
            return JsonResponse({'message': 'Course created successfully', 'courseId': course.id}, status=201)
    elif request.method == 'GET':
        courses = getCourses()
        print(courses)
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse({"courses": serializer.data})

@csrf_exempt
@require_http_methods(["GET"])
def getCourse(request, course_id):
    print(course_id)
    course = getACourse(course_id)
    if course is None:
        return JsonResponse({"error": "Course not found"}, status=404)
    serializer = CourseSerializer(course)
    return JsonResponse(serializer.data)
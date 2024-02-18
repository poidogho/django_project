from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json
from .services import createUser, createCourse, getACourse, getCourses, create_course_videos, get_course_videos, get_user_videos
from .serializers import CourseSerializer, VideoSerializer


def dummy_view(request):
    user_videos = get_user_videos(1)
    return JsonResponse({"user_videos": list(user_videos)})

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
        serializer = CourseSerializer(courses, many=True)
        return JsonResponse({"courses": serializer.data})

@csrf_exempt
@require_http_methods(["GET"])
def getCourse(request, course_id):
    course = getACourse(course_id)
    if course is None:
        return JsonResponse({"error": "Course not found"}, status=404)
    serializer = CourseSerializer(course)
    return JsonResponse(serializer.data)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def course_videos(request, course_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        serializer = VideoSerializer(data=data, many=True)
        for item in data:
            item['course_id'] = course_id
        
        if serializer.is_valid():
            valid_data = serializer.validated_data
            create_course_videos(valid_data)
            return JsonResponse({"success": "Videos add to course"})
        else:
            # Return validation errors
            return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 5))
        videos = get_course_videos(course_id, offset, limit)
        response = VideoSerializer(videos, many=True)
        return JsonResponse({"videos": response.data})


    return JsonResponse({"videos": "videos"})
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Courses, Video

def createUser():
    user_data = {
        "email": "johndoe@example.com",
        "firstName": "John",
        "lastName": "Doe",
        "password": "SecurePassword123",
        "avatar": "",  # Optional
        "tokens": [],  # Default is an empty list
        "auto": False,  # Default value
    }

    # Create a new user instance
    new_user = User.objects.create_user(
        email=user_data["email"],
        firstName=user_data["firstName"],
        password=user_data["password"],  # Ensure this is hashed appropriately by Django
        lastName=user_data["lastName"],
        avatar=user_data["avatar"],
        tokens=user_data["tokens"],
        auto=user_data["auto"]
    )

    print(f"User {new_user.email} created successfully!")
def getUsers():
    users = User.objects.all()
    print(users)

def createCourse(course):
    new_course = Courses.objects.create(**course)
    return new_course

def getACourse(id):
    try:
        course = Courses.objects.get(pk=id)
        return course
    except ObjectDoesNotExist:
        return None

def getCourses():
    courses = Courses.objects.all()
    return courses

def create_course_videos(videos_data):
    video_objects = [Video(**video) for video in videos_data]
    Video.objects.bulk_create(video_objects)
    return video_objects

def get_course_videos(course_id, offset, limit):
    videos = Video.objects.filter(course_id=course_id)[offset:offset + limit]
    return videos
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Courses, Video
from django.db.models import F

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
        password=user_data["password"],  
        lastName=user_data["lastName"],
        avatar=user_data["avatar"],
        tokens=user_data["tokens"],
        auto=user_data["auto"]
    )

    print(f"User {new_user.email} created successfully!")
def getUsers():
    users = User.objects.all()
    print(users)

def get_user_videos(user_id = 1):
    # select u.firstname , ac."name" , av.topic 
    # from users u 
    # left join api_courses ac 
    #     on u.id = ac.user_id
    # left join api_video av 
    #     on ac.id = av.course_id 
    # where u.id = 1;
    queryset = User.objects.filter(id=user_id).values(
    firstname=F('firstName'),
    course_name=F('courses__name'),
    video_topic=F('courses__video__topic')
    ).distinct()

    return queryset

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

def check_temp(num):
    if num >= 70:
        return "HOT"
    elif num <= 69 or num >=40:
        return "WARM"
    else:
        return "COLD"

def dictt_comp():
    # pseudocode = {key: expression for (key: value) in iterable}
    cities_in_f = {"new york" : 32, "boston": 75, "Los angeles": 100, "chicago": 50}

    # convert to celcius
    cities_in_c = {key: (round ((value - 32)/ (5/9))) for (key, value) in cities_in_f.items()}
    waether = {"new york" : "snowing", "boston": "sunny", "Los angeles": "sunny", "chicago": "cloudy"}
    sunny_cities = {key: value for (key, value) in waether.items if value == "sunny"} 
    waether_desc = {key: ("warm" if value >= 40 else "cold") for (key, value) in cities_in_f.items()}
    waether_desc2 = {key: check_temp(value) for (key, value) in cities_in_f.items()}

def list_comp():
    # squares = []
    # for i in range(1, 11):
    #     squares.append(i * i)
    # pseudocode = [expression for item in iterable if consition] or 
    # [expression (if else) for item in iterable]

    squares = [i*i for i in range(1, 11)]
    student_scores = [100, 90, 80, 70, 60, 50, 40, 30, 0]
    # using lambda
    passed_students_lam = list(filter(lambda x: x >= 60, student_scores))
    passed_students = [student for student in student_scores if student >= 60]
    passed_desc = [student if student >= 60 else "failed" for student in student_scores]
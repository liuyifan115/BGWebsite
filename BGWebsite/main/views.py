from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse
import json
import uuid
from pathlib import Path
from dateutil import parser
from main.models import Activity
from user.views import __get_current_user

BASE_DIR = Path(__file__).resolve().parent.parent

user_activity = Activity()
photo_path = []
video_path = []

def post_basic_info(request):
    global user_activity
    print(__get_current_user())
    # if __get_current_user() == "":
    #     return JsonResponse({"success": "0", "error": "You are not logged in"})
    data = json.loads(request.body)
    print(data)
    user_activity.username = __get_current_user()
    user_activity.title = data.get("theme")
    user_activity.isTemp = True
    user_activity.startDate = parser.isoparse(data.get("cycle")[0])
    user_activity.endDate = parser.isoparse(data.get("cycle")[1])
    user_activity.coordinate = data.get("address")
    user_activity.participant = data.get("persons")
    user_activity.description = data.get("tags")

    return JsonResponse({"success": "1", "message": "upload success"})

def post_detail(request):
    global user_activity
    # if __get_current_user() == "":
    #     return JsonResponse({"success": "0", "error": "You are not logged in"})
    data = json.loads(request.body)
    print(data)
    user_activity.detail_title = data.get("title")
    user_activity.detail_text = data.get("mainText")
    return JsonResponse({"success": "1", "message": "upload success"})

def post_photo(request):
    global user_activity
    uploaded_file = request.FILES.get("file")
    new_filename = f"{uuid.uuid4()}_{uploaded_file.name}"
    save_path = "upload/" + new_filename
    with default_storage.open(save_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    photo_path.append(save_path)
    return JsonResponse({"success": "1", "message": "upload success"})

def post_video(request):
    global user_activity
    uploaded_file = request.FILES.get("file")
    new_filename = f"{uuid.uuid4()}_{uploaded_file.name}"
    save_path = "upload/" + new_filename
    with default_storage.open(save_path, 'wb+') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    video_path.append(save_path)
    return JsonResponse({"success": "1", "message": "upload success"})

def post_over(request):
    global user_activity
    if json.loads(request.body).get("over"):
        user_activity.photo_path = str(photo_path)
        user_activity.video_path = str(video_path)
        user_activity.isTemp = False
        user_activity.save()
        return JsonResponse({"success": "1", "message": "upload success"})

def get_basic_info(request):
    # username = __get_current_user()
    username = "wcz"
    if not Activity.objects.filter(username=username).exists():
        return JsonResponse({"success": "0", "message": "user not found"})
    activities = list(Activity.objects.filter(username=username))
    data = []
    i = 0
    for activity in activities:
        data.append({
            "key": str(i),
            "name": activity.title,
            "persons": activity.participant,
            "time": activity.startDate,
            "time_end": activity.endDate,
            "address": activity.coordinate,
            "tags": activity.description,
            "detail_title": activity.detail_title,
            "detail_text": activity.detail_text,
            "photo": activity.photo_path,
            "video": activity.video_path,
        })
        i += 1
    return JsonResponse({"success": "1", "data": data})
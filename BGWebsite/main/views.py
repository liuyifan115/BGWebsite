from django.core.files.storage import default_storage
from django.http import HttpResponse, JsonResponse, FileResponse
import json
import uuid
from pathlib import Path
from dateutil import parser
from main.models import Activity
from user.views import __get_current_user
import os
import copy

BASE_DIR = Path(__file__).resolve().parent.parent

user_activity = Activity()
user_activity_empty = Activity()
photo_path = []
video_path = []

def post_basic_info(request):
    global user_activity
    if __get_current_user() == "":
        return JsonResponse({"success": "0", "error": "You are not logged in"})
    data = json.loads(request.body)
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
    if __get_current_user() == "":
        return JsonResponse({"success": "0", "error": "You are not logged in"})
    data = json.loads(request.body)
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
    global user_activity, photo_path, video_path
    if json.loads(request.body).get("over"):
        user_activity.photo_path = str(photo_path)
        photo_path.clear()
        user_activity.video_path = str(video_path)
        video_path.clear()
        user_activity.isTemp = False
        user_activity.username = __get_current_user()
        user_activity_6666 = copy.deepcopy(user_activity)
        user_activity = copy.deepcopy(user_activity_empty)
        user_activity_6666.save()
        return JsonResponse({"success": "1", "message": "upload success"})

def get_basic_info(request):
    username = __get_current_user()
    if not Activity.objects.filter(username=username).exists():
        return JsonResponse({"success": "0", "message": "user not found"})
    activities = list(Activity.objects.filter(username=username))
    data = []
    i = 0
    for activity in activities:
        data.append({
            "key": str(i),
            "id": activity.id,
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

def get_my_info(request):
    username = __get_current_user()

    id = int(request.GET.get("id"))
    activities = list(Activity.objects.filter(username=username))
    data = []
    i = 0
    for activity in activities:
        if activity.id == id:
            data.append({
                "key": str(i),
                "id": activity.id,
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
            return JsonResponse({"success": "1", "data": data})
        i += 1

def get_file(request):
    file_path = request.GET.get("path")
    if not os.path.exists(file_path) or not os.path.isfile(file_path):
        return JsonResponse({"success": "0", "message": "file not found"})
    response = FileResponse(open(file_path, 'rb'))
    import mimetypes
    guessed_type, _ = mimetypes.guess_type(file_path)
    if guessed_type:
        response['Content-Type'] = guessed_type
    return response
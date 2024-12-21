from django.http import HttpResponse, JsonResponse
import json
from dateutil import parser

from main.models import Activity, ActivityDetail, Photo, Video
from user.views import __get_current_user

user_activity = Activity

user_activity_detail = ActivityDetail
user_activity_detail.activity = Activity

user_photo = Photo
user_photo.activity_detail = ActivityDetail

user_video = Video
user_video.activity_detail = ActivityDetail

def post_basic_info(request):
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
    # if __get_current_user() == "":
    #     return JsonResponse({"success": "0", "error": "You are not logged in"})
    data = json.loads(request.body)
    print(data)
    user_activity_detail.title = data.get("title")
    user_activity_detail.text = data.get("mainText")
    return JsonResponse({"success": "1", "message": "upload success"})


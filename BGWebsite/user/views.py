import json
import hashlib
from django.http import HttpResponse, JsonResponse

from user.models import User


currentUser = ""

def user_register(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)

            username = data.get("username")
            password = data.get("password")
            print(username, password)

            if not username or not password:
                return JsonResponse({"success": "0", "message": "username and password are required"})

            if User.objects.filter(username=username).exists():
                return JsonResponse({"success": "0", "message": "user already exists"})

            user = User(username=username, password=hashlib.md5(password.encode()).hexdigest())
            user.save()

            return JsonResponse({"success": "1", "message": "register success"})
        except:
            return JsonResponse({"success": "0", "message": str(Exception)})
    return JsonResponse({"success": "0", "message": "POST only"})

def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            print(data)

            username = data.get("username")
            password = hashlib.md5(data.get("password").encode()).hexdigest()
            print(username, password)

            if not username or not password:
                return JsonResponse({"success": "0", "message": "username and password are required"})

            if not User.objects.filter(username=username).exists():
                return JsonResponse({"success": "0", "message": "user not exists"})

            if User.objects.get(username=username).password != password:
                return JsonResponse({"success": "0", "message": "password is wrong"})

            global currentUser
            currentUser = username
            return JsonResponse({"success": "1", "message": "login success"})
        except:
            return JsonResponse({"success": "0", "message": str(Exception)})
    return JsonResponse({"success": "0", "message": "POST only"})

def current_user(request):
    return JsonResponse({"success": "1", "current_user": currentUser})

def __get_current_user():
    return currentUser
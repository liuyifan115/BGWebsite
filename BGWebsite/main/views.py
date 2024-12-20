from django.http import HttpResponse, JsonResponse

def index(request):
    if request.method == "POST":
        reponse_data = {
            "data": [
                {
                    "key": "1",
                    "name": "敦煌研究",
                    "persons": request.POST.get("name"),
                    "time": "2018-02-01",
                    "age": 21,
                    "address": "敦煌",
                    "tags": "研究敦煌",
                },
                {
                    "key": "2",
                    "name": "Jim Green",
                    "persons": "刘一凡",
                    "age": 42,
                    "address": "London No. 1 Lake Park",
                    "tags": ["loser"],
                },
                {
                    "key": "3",
                    "name": "Joe Black",
                    "age": 32,
                    "address": "Sidney No. 1 Lake Park",
                    "tags": ["cool", "teacher"],
                },
            ]

        }
        return JsonResponse(reponse_data)

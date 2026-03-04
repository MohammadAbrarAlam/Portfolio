from django.http import JsonResponse
import requests
import json

def chat(request):

    if request.method == "POST":
        message = json.loads(request.body).get("message")

        response = requests.post(
            "http://localhost:5678/webhook/portfolio-chat",
            json={"message": message}
        )

        return JsonResponse(response.json())
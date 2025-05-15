from django.shortcuts import render

# Create your views here.
# chatgptapp/views.py

import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def chat_bot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get("message")

            if not message:
                return JsonResponse({"error": "message is required"}, status=400)

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": message}]
            )

            reply = response.choices[0].message["content"]
            return JsonResponse({"reply": reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POST request required"}, status=400)


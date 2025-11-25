from django.shortcuts import render

from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "status": "success",
        "message": "Django Backend is running using CICD ... ✅"
    })


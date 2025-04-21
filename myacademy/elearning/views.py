from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def index(request):
    return render(request, "elearning/index.html")


def proxy_courses(request, subpath=None, *args, **kwargs):
    url = f"http://localhost:8001{request.path}"
    try:
        # Προσπάθεια να γίνει η κλήση στον server 8001
        response = requests.get(url, timeout=5)  # Timeout 5 δευτερόλεπτα
        return HttpResponse(response.content, status=response.status_code)
    except requests.exceptions.RequestException:
        context = {"microservice_name": "Courses"}
        # Αν ο server είναι εκτός λειτουργίας, επιστρέφουμε μήνυμα
        return render(request, "elearning/service_unavailable.html", context, status=503)


@csrf_exempt
def proxy_users(request, subpath=None):
    url = f"http://localhost:8002/{request.path}"

    # Εξαγωγή του Authorization header
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        return JsonResponse({"error": "Authorization token is missing or invalid."}, status=401)

    token = auth_header.split(" ")[1]  # Παίρνουμε το token μετά το "Bearer"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    try:
        response = requests.get(
            "http://localhost:8002/users/token/", headers=headers)

        return JsonResponse(response.json(), status=response.status_code)
        # Προσπάθεια να γίνει η κλήση στον server 8002

    except requests.exceptions.RequestException:
        context = {"microservice_name": "users"}
        # Αν ο server είναι εκτός λειτουργίας, επιστρέφουμε μήνυμα
        return render(request, "elearning/service_unavailable.html", context, status=503)


""" @csrf_exempt
def proxy_users(request, subpath=None):
    url = f"http://localhost:8002/{request.path}"
    try:
        # Προσπάθεια να γίνει η κλήση στον server 8002
        response = requests.get(url, timeout=5)  # Timeout 5 δευτερόλεπτα
        return HttpResponse(response.content, status=response.status_code)
    except requests.exceptions.RequestException:
        context = {"microservice_name": "users"}
        # Αν ο server είναι εκτός λειτουργίας, επιστρέφουμε μήνυμα
        return render(request, "elearning/service_unavailable.html", context, status=503) """


def proxy_payment(request, subpath=None):
    url = f"http://localhost:8003/{request.path}"
    try:
        # Προσπάθεια να γίνει η κλήση στον server 8003
        response = requests.get(url, timeout=5)  # Timeout 5 δευτερόλεπτα
        return HttpResponse(response.content, status=response.status_code)
    except requests.exceptions.RequestException:
        context = {"microservice_name": "payment"}
        # Αν ο server είναι εκτός λειτουργίας, επιστρέφουμε μήνυμα
        return render(request, "elearning/service_unavailable.html", context, status=503)

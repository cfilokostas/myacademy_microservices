from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login
# Create your views here.
# afto agnoei ta csrf
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer


class MyTokenView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        pass
        print("User is already authenticated")
        # Αν ο χρήστης είναι ήδη συνδεδεμένος, ανακατεύθυνση στην αρχική σελίδα
        # return redirect("http://127.0.0.1:8000/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Σύνδεση του χρήστη
            pass
            # Ανακατεύθυνση στην αρχική σελίδα μετά τη σύνδεση
           # return redirect("http://127.0.0.1:8000/")
        else:
            # Επιστροφή μηνύματος σφάλματος αν τα στοιχεία είναι λάθος
            context = {
                'message': 'Αποτυχία σύνδεσης: Λανθασμένα στοιχεία χρήστη.'
            }
            return render(request, "users_microservice/login.html", context)

    return render(request, "users_microservice/login.html")


def register_page(request):
    return render(request, "users_microservice/register.html")


@csrf_exempt
def register_student_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        # Έλεγχος αν οι κωδικοί πρόσβασης ταιριάζουν
        if password != password_confirm:
            return HttpResponse("Οι κωδικοί πρόσβασης δεν ταιριάζουν.", status=400)

        # Δημιουργία χρήστη με is_student=True
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=make_password(password),
            is_student=True
        )
        return redirect("/users/login/")  # Ανακατεύθυνση στη σελίδα σύνδεσης

    return render(request, "users_microservice/register-student.html")


@csrf_exempt
def register_teacher_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        # Έλεγχος αν οι κωδικοί πρόσβασης ταιριάζουν
        if password != password_confirm:
            return HttpResponse("Οι κωδικοί πρόσβασης δεν ταιριάζουν.", status=400)

        # Έλεγχος αν το username υπάρχει ήδη
        if User.objects.filter(username=username).exists():
            return HttpResponse("Το όνομα χρήστη υπάρχει ήδη. Δοκιμάστε άλλο.", status=400)

        # Δημιουργία χρήστη με is_teacher=True
        try:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=make_password(password),
                is_teacher=True
            )
            # Ανακατεύθυνση στη σελίδα σύνδεσης
            return redirect("/users/login/")
        except Exception as e:
            print("Error creating user:", e)  # Debug: Εμφάνιση σφάλματος
            return HttpResponse("Σφάλμα κατά τη δημιουργία του χρήστη.", status=500)

    return render(request, "users_microservice/register-teacher.html")


def edit_profile_page(request):
    return render(request, "users_microservice/edit-profile.html")


def control_panel_page(request):
    return render(request, "users_microservice/control-panel.html")

from django.shortcuts import render,redirect,get_object_or_404
from.models import Student

# Create your views here.
#   DISPLAY STUDENT DETAIL
def student_detail(request):
    student=Student.objects.all()  # select * from student
    return render(request,'app1/student.html',{'student':student})

# start CRUD method
#1. ADD/CREATE METHOD
def add_student(request):
    if request.method == "POST":
        student_id = request.POST.get("student_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        course = request.POST.get("course")
        phone_number = request.POST.get("phone_number")
        address = request.POST.get("address")
       # educational_institution = request.POST.get("educational_institution")

        profile_image = request.FILES.get('profile_image')  # ⭐ Yaha se utha rahe hain
        Student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            course=course,
            phone_number=phone_number,
            address=address,
            #educational_institution= educational_institution,

            profile_image = profile_image  # ⭐ Ab yaha assign kar diya
        )
        #return redirect("/app1/student/")
        return redirect("/")

    return render(request, "app1/add_student.html")


# 2 UPDATE METHOD
def update_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == "POST":
        student.student_id = request.POST.get("student_id")
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.course = request.POST.get("course")
        student.phone_number = request.POST.get("phone_number")
        student.address = request.POST.get("address")
        #student.educational_institution = request.POST.get("educational_institution")

        # 👇 Yeh line add karo image update ke liye
        if 'profile_image' in request.FILES:
            student.profile_image = request.FILES['profile_image']
        student.save()
        #return redirect("/app1/student/")  # Redirect back to the student list
        return redirect("/")

    return render(request, 'app1/update_student.html', {"student": student})

# 3 DELETE METHOD

def delete_student(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)

    if request.method == "POST":
        student.delete()
        #return redirect('/app1/student/')  # Redirect to student list after deletion
        return redirect('/')  # Redirect to student list after deletion

    return render(request, 'app1/delete_student.html', {'student': student})

# 4 SEARCH METHOD

def search_student(request):
    """Strict search: Requires exact full name match (case-sensitive)."""
    student = request.GET.get('q', '').strip()  # Remove extra spaces

    if student:
        student = Student.objects.filter(name__icontains=student)  # Case-sensitive exact match
    else:
        student = Student.objects.all()  # Return an empty queryset if no input

    return render(request, 'app1/student.html', {'student': student})



# View individual detail for all  student

def student_view(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    return render(request, 'app1/individual_student_view.html', {'student': student})



# Register, Login, Logout

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# ✅ Register View
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "User registered successfully!")
        return redirect('login')

    return render(request, 'app1/register.html')

# ✅ Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
           # return redirect("/app1/student/")
            return redirect("/")
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")

    return render(request, "app1/login.html")


# ✅ Logout View
def logout_view(request):
    logout(request)
    #return redirect("/app1/student/")
    return redirect("/")

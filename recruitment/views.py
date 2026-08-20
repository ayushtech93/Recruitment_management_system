from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from .models import HRProfile, Student, Application, Interview,InterviewReview,StudentVisit

# Create your views here.
def login_page(request):

    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        User=authenticate(
            request,
            username=username,
            password=password,
        )

        if User is not None:
            login(request,User)
            return redirect('hr_dashboard')

        messages.error(request,"Invalid username or password.")

    return render(request,"template/login_page.html")


def hr_dashboard(request):
    total_students = Student.objects.count()
    total_applications = Application.objects.filter(status='New').count
    total_interviews = Application.objects.filter(status='Interview').count()
    # total_interviews = Interview.objects.filter(status='Interview').count()

    total_selected = Application.objects.filter(status="Selected").count()
    recent_applications = Application.objects.filter(status='New').select_related("student").order_by("-applied_date")[:5]
    upcoming_interview = Application.objects.filter(status='Interview').select_related("student").order_by("-applied_date")[:5]

    all_data={
        "total_students": total_students,
        "total_applications": total_applications,
        "total_interviews": total_interviews,
        "total_selected": total_selected,
        "recent_applications":recent_applications,
        'upcoming_interview':upcoming_interview,
    }


    return render(request,"hr_dashboard.html",all_data)


def student_application(request):

    if request.method=="POST":
        student = Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            mobile=request.POST.get("mobile"),
            college=request.POST.get("college"),
            course=request.POST.get("course"),
            passing_year=request.POST.get("passing_year"),
            skills=request.POST.get("skills"),
            experience=request.POST.get("experience"),
            resume=request.FILES.get("resume")
        )

        Application.objects.create(
            student=student,
            applied_position=request.POST.get("applied_position"),
            message=request.POST.get("message")
        )

        messages.success(
            request,
            "Your application has been submitted successfully!"
        )
        return redirect ("success")
    
    return render(request,'student_application.html')



def success(request):
    return render(request,'success.html')


def application(request):
    apply=Application.objects.count()
    applications = Application.objects.select_related("student").order_by("-applied_date")

    return render(request,"application.html",{"applications": applications,
                                              "apply":apply,})


def application_details(request,id):
        application = Application.objects.select_related("student").get(id=id)

        return render(
            request,
            "application_details.html",
            {
                "applications": application
            }
        )

def shortlist_candidate(request,id):
    application = Application.objects.get(id=id)

    application.status='Interview'

    application.save()

    return redirect(interview)



def interview(request):

    return render(request,'interview.html')


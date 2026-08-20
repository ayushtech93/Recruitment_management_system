from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('hr_dashboard/',views.hr_dashboard,name='hr_dashboard'),
    path('student_application/',views.student_application,name='student_application'),
    path('success/',views.success,name='success'),
    path('application/',views.application,name='application'),
    path('application_details/<int:id>/',views.application_details,name='application_details'),
    path('shortlist_candidate/<int:id>/',views.shortlist_candidate,name='shortlist_candidate'),
    path('interview',views.interview,name='interview')
]

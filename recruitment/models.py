from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class HRProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=100, blank=True)
    designation = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Student(models.Model):
    EXPERIENCE_CHOICES = [
        ('Fresher', 'Fresher'),
        ('Experienced', 'Experienced'),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    college = models.CharField(max_length=200)
    course = models.CharField(max_length=100)
    passing_year = models.PositiveIntegerField()
    skills = models.TextField()
    experience = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default='Fresher'
    )
    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Application(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Shortlisted', 'Shortlisted'),
        ('Interview', 'Interview'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applied_position = models.CharField(max_length=150)
    message = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )
    applied_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.applied_position}"


class Interview(models.Model):
    TYPE_CHOICES = [
        ('Online', 'Online'),
        ('Offline', 'Offline'),
    ]

    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    application = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name='interviews'
    )
    interviewer = models.ForeignKey(
        HRProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    interview_date = models.DateField()
    interview_time = models.TimeField()
    interview_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )
    location_or_link = models.CharField(
        max_length=300,
        blank=True
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Scheduled'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.application.student.name} - {self.interview_date}"


class InterviewReview(models.Model):
    DECISION_CHOICES = [
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
        ('On Hold', 'On Hold'),
        ('Next Round', 'Next Round'),
    ]

    interview = models.OneToOneField(
        Interview,
        on_delete=models.CASCADE,
        related_name='review'
    )
    technical_skills = models.PositiveIntegerField(default=0)
    communication = models.PositiveIntegerField(default=0)
    problem_solving = models.PositiveIntegerField(default=0)
    overall_rating = models.PositiveIntegerField(default=0)
    review = models.TextField()
    final_decision = models.CharField(
        max_length=20,
        choices=DECISION_CHOICES
    )
    reviewed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review - {self.interview.application.student.name}"


class StudentVisit(models.Model):
    PURPOSE_CHOICES = [
        ('Interview', 'Interview'),
        ('Document Verification', 'Document Verification'),
        ('Meeting', 'Meeting'),
        ('Other', 'Other'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='visits'
    )
    visited_hr = models.ForeignKey(
        HRProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    visit_date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField(
        null=True,
        blank=True
    )
    purpose = models.CharField(
        max_length=50,
        choices=PURPOSE_CHOICES
    )
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.name} - {self.visit_date}"
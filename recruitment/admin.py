from django.contrib import admin
from .models import HRProfile,Student,Application,Interview,InterviewReview,StudentVisit

class HRProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'phone',
        'department',
        'designation',
        'is_active',
        'created_at',
    )
    search_fields = (
        'user__username',
        'user__first_name',
        'user__last_name',
        'user__email',
    )
    list_filter = ('is_active', 'department')

class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'mobile',
        'college',
        'course',
        'passing_year',
        'experience',
        'created_at',
    )
    search_fields = (
        'name',
        'email',
        'mobile',
        'college',
    )
    list_filter = (
        'course',
        'experience',
        'passing_year',
    )

class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'applied_position',
        'status',
        'applied_date',
    )
    search_fields = (
        'student__name',
        'student__email',
        'applied_position',
    )
    list_filter = (
        'status',
        'applied_position',
    )


class InterviewAdmin(admin.ModelAdmin):
    list_display = (
        'application',
        'interviewer',
        'interview_date',
        'interview_time',
        'interview_type',
        'status',
    )
    search_fields = (
        'application__student__name',
        'interviewer__user__username',
    )
    list_filter = (
        'status',
        'interview_type',
        'interview_date',
    )

class InterviewReviewAdmin(admin.ModelAdmin):
    list_display = (
        'interview',
        'technical_skills',
        'communication',
        'problem_solving',
        'overall_rating',
        'final_decision',
        'reviewed_at',
    )
    list_filter = (
        'final_decision',
        'overall_rating',
    )

class StudentVisitAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'visited_hr',
        'visit_date',
        'check_in',
        'check_out',
        'purpose',
    )
    search_fields = (
        'student__name',
        'visited_hr__user__username',
    )
    list_filter = (
        'purpose',
        'visit_date',
    )


admin.site.register(HRProfile,HRProfileAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Application,ApplicationAdmin)
admin.site.register(Interview,InterviewAdmin)
admin.site.register(InterviewReview,InterviewReviewAdmin)
admin.site.register(StudentVisit,StudentVisitAdmin)


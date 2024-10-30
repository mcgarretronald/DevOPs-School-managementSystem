
from django.urls import path

from .views import StudentListViews
from .views import ClassListViews
from .views import ClassPeriodListViews
from .views import CoursesListViews
from .views import TeacherListViews
from .views import StudentDetailView
from .views import ClassDetailView
from .views import TeacherDetailView
from .views import CoursesDetailView
from .views import ClassPeriodDetailView
from .views import WeeklyTimetable


urlpatterns = [
path("students/", StudentListViews.as_view(), name="student_list_view"),
path("classes/", ClassListViews.as_view(), name="class_list_view"),
path("periods/", ClassPeriodListViews.as_view(), name="classPeriod_list_view"),
path("courses/", CoursesListViews.as_view(), name="course_list_view"),
path("teachers/", TeacherListViews.as_view(), name="teacher_list_view"),
path("students/<int:id>/", StudentDetailView.as_view(), name="student_detail_view"),
path("classes/<int:id>/", ClassDetailView.as_view(), name="class_detail_view"),
path("teachers/<int:id>/", TeacherDetailView.as_view(), name="teacher_detail_view"),
path("courses/<int:id>/", CoursesDetailView.as_view(), name="course_detail_view"),
path("class_period/<int:id>/", ClassPeriodDetailView.as_view(), name="class_period_detail_view"),
path('Weekly_timetable/', WeeklyTimetable.as_view(), name='weekly_timetable'),
]


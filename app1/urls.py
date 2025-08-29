
from django.urls import path
from.import views




urlpatterns = [
    #path('student/',views.student_detail, name='display'),
    path('',views.student_detail, name='display'),
    path('add_student/',views.add_student, name='add_student'),
    path('update_student/<int:student_id>/',views.update_student, name='update_student'),
    path('delete_student/<int:student_id>/',views.delete_student, name='delete_student'),
    path('search_student/',views.search_student, name='search_student'),
    path('student_view/<str:student_id>/', views.student_view, name='student_view'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]






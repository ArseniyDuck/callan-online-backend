from django.urls import path
from .views import *

app_name = "app"
urlpatterns = [
   path('vocabulary/', Vocabulary.as_view()),

   path('homework/', HomeWork.as_view()),
   path('have_homework/', HaveHomework.as_view()),

   path('lesson/<int:number>/', LessonView.as_view()),
   path('lesson_list/', LessonsList.as_view()),
]
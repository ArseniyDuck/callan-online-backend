from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Lesson, HomeWorkTask
from .serializers import SVocabularyLesson, SHomeWorkTask, SLesson, SLessonList


class Vocabulary(APIView):
   def get(self, request):
      lessons = Lesson.objects.all()
      serializer = SVocabularyLesson(lessons, many=True)
      return Response(serializer.data)


class HomeWork(APIView):
   def get(self, request):
      tasks = HomeWorkTask.objects.order_by('-deadline')
      serializer = SHomeWorkTask(tasks, many=True)
      return Response(serializer.data)


class HaveHomework(APIView):
   def get(self, request):
      have_homework = any([not task.calculate_is_completed() for task in HomeWorkTask.objects.all()])
      return Response({'have_homework': have_homework})

   
class LessonsList(APIView):
   def get(self, request):
      lesson = Lesson.objects.all()
      serializer = SLessonList(lesson, many=True)
      return Response(serializer.data)


class LessonView(APIView):
   def get(self, request, number):
      try:
         lesson = Lesson.objects.get(number=number)
         serializer = SLesson(lesson)
         return Response(serializer.data)
      except Lesson.DoesNotExist:
         return HttpResponse(status=404)
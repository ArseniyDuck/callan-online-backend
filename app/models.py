import datetime
from django.utils import timezone
from django.db import models


class Lesson(models.Model):
   """
   Lesson is a structured Callan book's lesson content
   with groups of new words, rules, questions etc.
   """
   number = models.SmallIntegerField()
   audio = models.FileField(upload_to='lessons_audio/', null=True)

   def __str__(self):
      return str(self.number)


class CurrentLesson(models.Model):
   lesson = models.OneToOneField(to=Lesson, on_delete=models.CASCADE, related_name='current_lesson')

   def __str__(self):
      return str(self.lesson.number)
      

class GroupOfWords(models.Model):
   """
   Question is type of content in Callan book's lesson.
   Columns count is required to build responsive grid.
   It may contain theme word (instance of ThemeWord)
   """
   columns_count = models.SmallIntegerField()
   page = models.SmallIntegerField(blank=True, null=True)
   lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='groups_of_words_set')
   content_id = models.SmallIntegerField(default=0)

   class Meta:
      verbose_name_plural = "groups of words"

   def __str__(self):
      return str(self.lesson.number) + '-' + str(self.content_id)


class Word(models.Model):
   """
   Word is a word from Callan book's vocabulary.
   Also instance of GroupOfWords contains Words.
   """
   english_text = models.CharField(max_length=60)
   translation_text = models.CharField(max_length=60)
   page = models.SmallIntegerField(default=0)
   lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='words_set')
   group_of_words = models.ForeignKey(to=GroupOfWords, on_delete=models.CASCADE, related_name='words_set', blank=True, null=True)

   def __str__(self):
      return self.english_text


class ThemeWord(models.Model):
   """
   ThemeWord is optional underlined word in GroupOfWords.
   """
   text = models.CharField(max_length=120)
   group_of_words = models.ForeignKey(to=GroupOfWords, on_delete=models.CASCADE, related_name='theme_words_set')

   def __str__(self):
      return self.text


class Question(models.Model):
   """
   Question is most popular type of content in
   Callan book's lesson.
   """
   question_text = models.TextField()
   answer_text = models.TextField()
   page = models.SmallIntegerField(blank=True, null=True)
   lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='questions_set')
   content_id = models.SmallIntegerField(default=0)

   def __str__(self):
      return self.question_text


class Rule(models.Model):
   """
   Rule is type of content in Callan book's lesson.
   It can be ordered or not. If Rule is ordered, it has index number and margin-left.
   """
   text = models.TextField()
   index_number = models.SmallIntegerField(blank=True, null=True)
   page = models.SmallIntegerField(blank=True, null=True)
   lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='rules_set')
   content_id = models.SmallIntegerField(default=0)

   def __str__(self):
      return self.text


class Idiom(models.Model):
   """
   Idiom is type of content in Callan book's lesson.
   It may not be included in the lesson.
   """
   number = models.SmallIntegerField(unique=True)
   idiom_text = models.CharField(max_length=120)
   explaining_text = models.CharField(max_length=120)
   example_text = models.CharField(max_length=120)
   page = models.SmallIntegerField(blank=True, null=True)
   lesson = models.ForeignKey(to=Lesson, on_delete=models.CASCADE, related_name='idioms_set', null=True)
   content_id = models.SmallIntegerField(default=0)

   def __str__(self):
      return self.idiom_text

   
class Dictation(models.Model):
   """
   Dictation is type of content in Callan book's lesson.
   It has number(id) and may not be included in the lesson.
   """
   number = models.SmallIntegerField(unique=True)
   text = models.TextField()
   lesson = models.OneToOneField(to=Lesson, on_delete=models.CASCADE, related_name='dictation_set')

   def __str__(self):
      return str(self.number)

   
class HomeWorkTask(models.Model):
   """
   HomeWorkTask is the homework that Lisa gave us for the next lesson.
   """
   theme = models.CharField(max_length=60)
   text = models.CharField(max_length=240)
   deadline = models.DateTimeField()

   def calculate_is_completed(self):
      return self.deadline < timezone.now()

   def calculate_timedelta(self):
      def add_zero(number):
         if number / 10 <= 1:
            return '0' + str(number)
         return str(number)

      if not self.calculate_is_completed():
         td =  self.deadline - timezone.now()
         d = td.days
         h = td.seconds // 3600
         s = (td.seconds // 60) % 60
         string = f'{add_zero(h)}:{add_zero(s)}'
         if (d > 0):
            string = f'{d} days, ' + string
         return string

   def get_deadline(self):
      dd = str(self.deadline)
      return '.'.join(dd.split(' ')[0].split('-'))

   def __str__(self):
      return self.get_deadline()
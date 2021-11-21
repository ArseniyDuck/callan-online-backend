from django.contrib import admin
from .models import Lesson, GroupOfWords, Word, ThemeWord, Question, Rule, Idiom, Dictation, HomeWorkTask, CurrentLesson


# Lesson
class DictationInline(admin.StackedInline):
   model = Dictation

class LessonAdmin(admin.ModelAdmin):
   fields = ('number', 'audio')
   inlines = [DictationInline]
admin.site.register(Lesson, LessonAdmin)


# Question
class QuestionAdmin(admin.ModelAdmin):
   fields = ('question_text', 'answer_text', ('lesson', 'content_id'), 'page')
   list_display = ('lesson', 'question_text')
   list_display_links = ('question_text', )
admin.site.register(Question, QuestionAdmin)


# Rule
class RuleAdmin(admin.ModelAdmin):
   fields = ('text', ('lesson', 'content_id'), 'index_number', 'page')
   list_display = ('lesson', 'text')
   list_display_links = ('text', )
admin.site.register(Rule, RuleAdmin)


# GroupOfWords
class WordInline(admin.TabularInline):
   model = Word
   extra = 1

class ThemeWordInline(admin.TabularInline):
   model = ThemeWord
   extra = 1

class GroupOfWordsAdmin(admin.ModelAdmin):
   fields = ('columns_count', ('lesson', 'content_id'), 'page')
   list_display = ('lesson', 'content_id', 'columns_count')
   list_display_links = ('lesson', 'content_id')
   inlines = [ThemeWordInline, WordInline]
admin.site.register(GroupOfWords, GroupOfWordsAdmin)


# Idiom
class IdiomAdmin(admin.ModelAdmin):
   list_display = ('number', 'idiom_text', 'lesson')
   list_display_links = ('number', 'idiom_text')
admin.site.register(Idiom, IdiomAdmin)


# HomeWorkTask
class HomeTaskAdmin(admin.ModelAdmin):
   list_display = ('deadline', 'theme')
admin.site.register(HomeWorkTask, HomeTaskAdmin)


# Word
class WordAdmin(admin.ModelAdmin):
   fields = (('english_text', 'translation_text'), 'page', ('lesson', 'group_of_words'))
   list_display = ('english_text', 'translation_text', 'lesson')
admin.site.register(Word, WordAdmin)


# CurrentLesson
class CurrentLessonAdmin(admin.ModelAdmin):
   list_display = ('lesson', )
   list_editable = ('lesson', )
   list_display_links = None
   radio_fields = {'lesson': admin.HORIZONTAL}
   def has_add_permission(self, request):
      num_objects = self.model.objects.count()
      if num_objects >= 1:
         return False
      else:
         return True
admin.site.register(CurrentLesson, CurrentLessonAdmin)


# Dictation
admin.site.register(Dictation)
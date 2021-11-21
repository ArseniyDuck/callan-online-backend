import math
from rest_framework import serializers
from .models import Lesson, GroupOfWords, Word, Question, Rule, Idiom, Dictation, HomeWorkTask


class SVocabularyWord(serializers.ModelSerializer):
   class Meta:
      model = Word
      fields = ['id', 'english_text', 'translation_text', 'page']


class SLessonWord(serializers.ModelSerializer):
   class Meta:
      model = Word
      fields = ['id', 'english_text', 'translation_text']


class SQuestion(serializers.ModelSerializer):
   class Meta:
      model = Question
      exclude = ['lesson', ]


class SRule(serializers.ModelSerializer):
   class Meta:
      model = Rule
      exclude = ['lesson', ]


class SIdiom(serializers.ModelSerializer):
   class Meta:
      model = Idiom
      exclude = ['lesson', ]


class SDictation(serializers.ModelSerializer):
   class Meta:
      model = Dictation
      exclude = ['lesson', ]


class SVocabularyLesson(serializers.ModelSerializer):
   words = SVocabularyWord(source='words_set', many=True)

   class Meta:
      model = Lesson
      depth = 3
      fields = ['number', 'words']


class SHomeWorkTask(serializers.ModelSerializer):
   deadline = serializers.CharField(source='get_deadline')
   is_completed = serializers.BooleanField(source='calculate_is_completed')
   time_left = serializers.CharField(source='calculate_timedelta')
   
   class Meta:
      model = HomeWorkTask
      fields = ['id', 'theme', 'text', 'deadline', 'is_completed', 'time_left']


class SGroupsOfWords(serializers.ModelSerializer):
   words = SLessonWord(source='words_set', many=True)
   
   class Meta:
      model = GroupOfWords
      depth = 1
      fields = ['id', 'content_id', 'columns_count', 'page', 'words', 'theme_words_set']


class SLesson(serializers.ModelSerializer):
   questions = SQuestion(source='questions_set', many=True)
   rules = SRule(source='rules_set', many=True)
   groups_of_words = SGroupsOfWords(source='groups_of_words_set', many=True)
   idioms = SIdiom(source='idioms_set', many=True)
   dictation = SDictation(source='dictation_set')

   def to_representation(self, instance):
      initial_representation = super().to_representation(instance)
      custom_representation_data = []

      # Question
      for question in initial_representation['questions']:
         custom_representation_data.append({
            'content_type': 'Question',
            'content': question
         })

      # Rule
      for rule in initial_representation['rules']:
         custom_representation_data.append({
            'content_type': 'Rule',
            'content': rule
         })
      # GroupOfWords
      for group_of_words in initial_representation['groups_of_words']:
         custom_representation_data.append({
            'content_type': 'GroupOfWords',
            'content': group_of_words
         })

      # Idiom
      for idiom in initial_representation['idioms']:
         custom_representation_data.append({
            'content_type': 'Idiom',
            'content': idiom
         })

      # Dictation
      custom_representation_data.append({
         'content_type': 'Dictation',
         'content': initial_representation['dictation']
      })

      def sort_data(elem):
         if elem['content_type'] != 'Dictation':
            return elem['content']['content_id']
         return math.inf
      
      custom_representation_data.sort(key=sort_data)

      return {
         'number': initial_representation['number'],
         'data': custom_representation_data,
         'audio': initial_representation['audio']
      }

   class Meta:
      model = Lesson
      depth = 1
      fields = ['number', 'questions', 'rules', 'idioms', 'dictation', 'groups_of_words', 'audio']


class SLessonList(serializers.ModelSerializer):
   def to_representation(self, instance):
      initial_representation =  super().to_representation(instance)
      return {
         'number': initial_representation['number'],
         'is_current': bool(initial_representation['current_lesson'])
      }
   
   class Meta:
      model = Lesson
      fields = ['number', 'current_lesson']
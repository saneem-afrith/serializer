from rest_framework import serializers
from Repository.models import Questions

class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    language = serializers.ChoiceField(choices=Questions.LANGUAGE_CHOICES, default='python')
    difficulty_level = serializers.ChoiceField(choices=Questions.DIFFICULTY_LEVEL, default='easy')
    notes = serializers.CharField()
    topic = serializers.CharField()
    published_date = serializers.DateTimeField(read_only=True)
    sample_input = serializers.CharField()
    sample_output = serializers.CharField()
    is_active = serializers.BooleanField()

class SubmissionSerializer(serializers.Serializer):
    answer = serializers.CharField()
    question_id = serializers.IntegerField()
    points = serializers.IntegerField(read_only=True)
    owner = serializers.CharField()
    submission_date = serializers.DateTimeField(read_only=True)
    remarks = serializers.CharField(read_only=True)
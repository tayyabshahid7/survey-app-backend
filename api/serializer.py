from rest_framework import serializers
from api.models import *


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ("id", "question", "text")


class QuestionSerializer(serializers.ModelSerializer):
    choices = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("id", "question_title", "choices")


class AnswerSerializer(serializers.ModelSerializer):
    option = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Answer
        fields = ("survey", "user_email", "option")


class SurveySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    response_count = serializers.SerializerMethodField()

    class Meta:
        model = Survey
        fields = ("id", "title", "is_active", "questions", "response_count")

    def get_response_count(self, obj):
        return len(obj.answer_set.all().filter(survey_id=obj.id).values('user_email').distinct())

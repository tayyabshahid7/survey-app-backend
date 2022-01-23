from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api.filters import SurveyFilter
from api.models import *
from api.serializer import SurveySerializer, AnswerSerializer, QuestionSerializer
from rest_framework.response import Response


class SurveyViewSet(ModelViewSet):
    serializer_class = SurveySerializer
    queryset = Survey.objects.filter(is_active=True)
    filterset_class = SurveyFilter


class AnswerView(APIView):

    def post(self, request):
        data = request.data

        if_exist = Answer.objects.filter(survey_id=data['survey'], user_email=data['email'])
        if len(if_exist) == 0:
            for option in data['option']:
                answer = Answer.objects.create(user_email=data['email'], survey_id=data['survey'], option_id=option)

            return Response({
                "success": True,
                "response": "Survey submitted successfully!"
            })
        else:
            raise ValidationError({
                "success": False,
                "error": "You have already used this email to submit a survey"
            })


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

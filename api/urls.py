from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import SurveyViewSet, AnswerView

router = DefaultRouter()
router.register('survey', SurveyViewSet, basename='survey')

urlpatterns = [
    path("", include(router.urls)),
    path("answer/", AnswerView.as_view()),
]

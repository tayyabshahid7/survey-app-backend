from django.contrib import admin
from nested_admin.nested import NestedTabularInline, NestedStackedInline, NestedModelAdmin
from api.models import *
from django import forms


class OptionAdmin(NestedStackedInline):
    model = Option
    extra = 1


class QuestionAdmin(NestedTabularInline):
    model = Question
    extra = 1
    inlines = [OptionAdmin]


class SurveyAdminForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'

    def clean(self):
        qs = Question.objects.all()
        if len(qs.all()) < 11:
            super(SurveyAdminForm, self).clean()
        else:
            raise forms.ValidationError("You can only upto 10 questions per survey!")


class SurveyAdmin(NestedModelAdmin):
    form = SurveyAdminForm
    list_display = ('title', 'is_active',)
    inlines = [QuestionAdmin]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(Answer)

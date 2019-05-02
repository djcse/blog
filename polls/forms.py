from django import forms
from .models import Question, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text','pub_date','question_type','number_of_choices']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

# class MusicianForm(forms.ModelForm):
#
#     musician = forms.CharField()
#
#     def __init__(self, *args, **kwargs):
#         super(MusicianForm, self).__init__(*args, **kwargs)
#         self.fields['musician'] = forms.MultipleChoiceField(
#         widget=forms.CheckboxSelectMultiple, choices=(((choice.id), choice) for choice in Musician.objects.all()))
#
# class Meta:
#     model = Album
#     fields = ('name','release_date','num_stars')


class ChoiceFill(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ChoiceFill, self).__init__(*args, **kwargs)
        n = args[1]['nchoice']
        print(">>>>>>>>",n)
        for i in range(n):
            self.fields['choice' + str(i)] = forms.CharField()
        print("<><><>><><><>><>><><><><><><>")
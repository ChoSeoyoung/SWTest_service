from django import forms
from questions.models import Question

CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'subject', 'content', 'ans1', 'ans2', 'ans3', 'ans4', 'ans']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'subject' : forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'ans1' : forms.TextInput(attrs={'class': 'form-control'}),
            'ans2': forms.TextInput(attrs={'class': 'form-control'}),
            'ans3': forms.TextInput(attrs={'class': 'form-control'}),
            'ans4': forms.TextInput(attrs={'class': 'form-control'}),
            'ans': forms.TextInput(attrs={'class': 'form-control'}),
        }


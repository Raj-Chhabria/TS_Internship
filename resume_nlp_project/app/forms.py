from django import forms

class Skill(forms.Form):
    skills = forms.CharField(max_length=500)
    resume_text = forms.TextInput()



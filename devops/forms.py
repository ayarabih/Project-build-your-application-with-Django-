from django import forms
from devops.models import Student, Track

class studentform( forms.ModelForm):
    class Meta:
        model =  Student
        fields = ('fname','lname', 'age', 'student_track')
        # fields = '__all__'

class trackform(forms.ModelForm):
    class Meta:
        model = Track
        fields = ('name',)


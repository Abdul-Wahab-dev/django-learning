from django import forms
from .models import Course
# class Courseregistration(forms.Form):
#     name = forms.CharField()
#     description = forms.CharField(widget=forms.Textarea())
    
#     def clean(self):
#         # clean_data = super().clean()
#         # print(clean_data,'clean_data')
#         valname = self.cleaned_data['name']
#         if len(valname) < 4:
#             raise forms.ValidationError("Name should be greater than 4 character")
#         else: return self.cleaned_data

class CourseRegistration(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        # fields = '__all__'
        labels = {"name":"Enter name", "description":"Enter Description"}
        
        
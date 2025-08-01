from django import forms 
from .models import EnquiryForm

class UserEnquiryForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    # message = forms.CharField(widget=forms.Textarea(attrs='rows':8, 'cols':40))

class UserEnquiryModelForm(forms.ModelForm):
    class Meta:
        model = EnquiryForm 
        fields = ['name','email','subject','message']
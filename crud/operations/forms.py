from django import forms 
from .models import details

class detailsregister(forms.ModelForm):
    
    class Meta:
        model = details
        fields = ['name','email','password']
        widgets  =  {
            'name':forms.TextInput(attrs = {'class':'form-control'}),
            'email':forms.EmailInput(attrs = {'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs = {'class':'form-control'})
        }

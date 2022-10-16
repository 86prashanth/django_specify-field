from django import forms
# create your  forms here...
class Student(forms.Form):
    name=forms.CharField(error_messages={'required':'Enter your name'})
    agree=forms.BooleanField(label="I agree",label_suffix="")
    roll=forms.IntegerField(min_value=5,max_value=50) 
    email=forms.EmailField()
    price=forms.DecimalField(min_value=5,max_value=50,max_digits=4,decimal_places=1)
    rate=forms.FloatField()
    comment=forms.SlugField()
    website=forms.URLField(min_length=5,max_length=50)
    description=forms.CharField(widget=forms.Textarea)
    feedback=forms.CharField(min_length=5,max_length=50,widget=forms.TextInput(attrs={'class':'somecss1','id':'uniqueid'}))
    notes=forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':50}))
    password=forms.CharField(widget=forms.PasswordInput) 


class Specify(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data=super().clean()
        name=self.cleaned_data['name']
        email=self.cleaned_data['email']
        if len(name)<4:
            raise forms.ValidationError('name should be more than or equal 4')
        if len(email)<13:
            raise forms.ValidationError('email should be more than or equal 13')
    
                         
    
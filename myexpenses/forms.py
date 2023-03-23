from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,UserExpenses

from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control input"
            }
        )
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control input"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control input"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control input"
            }
        )
    )
    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_member')


class UserExpensesForm (ModelForm):
    Date_of_Expense=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model=UserExpenses
        fields =['Name','Date_of_Expense','Category','Description','Amount']
        

    def __init__(self,*args,**kwargs):
        super(UserExpensesForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class CategoryForm(ModelForm):
    class Meta:
        model=UserExpenses
        fields=['Category']
    
    def __init__(self,*args,**kwargs):
        super(CategoryForm, self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

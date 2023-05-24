from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from core.models import (Vendors,User,Product,Wallet)

class VendorSignUpForm(UserCreationForm):
    #interests = forms.ModelMultipleChoiceField(
        #queryset=Subject.objects.all(),
        #widget=forms.CheckboxSelectMultiple,
        #required=True
    #)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_vendor = True
        user.save()
        #student = Student.objects.create(user=user)
        #student.interests.add(*self.cleaned_data.get('interests'))
        return user
class CustomerSignUpForm(UserCreationForm):
    #interests = forms.ModelMultipleChoiceField(
        #queryset=Subject.objects.all(),
        #widget=forms.CheckboxSelectMultiple,
        #required=True
    #)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        #student = Student.objects.create(user=user)
        #student.interests.add(*self.cleaned_data.get('interests'))
        return user
        
    

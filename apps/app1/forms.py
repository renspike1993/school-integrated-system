from django import forms
from .models import Student,Folder



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets = {
            'folder': forms.Select(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 w-full'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 w-full'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 w-full'
            }),
            'middle_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 w-full'
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 w-full'
            }),
            'gender': forms.Select(attrs={
                'class': 'border border-gray-300 rounded-md px-3 py-2 w-full'
            }),
        }

class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['folder_name', 'folder_capacity', 'floor_number']
        widgets = {
            'folder_name': forms.TextInput(attrs={'class': 'form-control'}),
            'folder_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'floor_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from . import models
from ckeditor.widgets import CKEditorWidget


class ContactForm(forms.Form):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id' : 'name',
        'type' : 'text',
        'size': "200",
        'placeholder': "Your Name",
        }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'type' : 'email',
        'placeholder': "Enter Email",
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
    'class': "form-control", 
    'cols': "6",
    'placeholder': 'Leave a message here'
        }))
    






categories = models.JobCategory.objects.all()

categories_list = []
for c in categories:
    categories_list.append((str(c), str(c)))

categories_tuple = tuple(categories_list)

job_categories = models.JobCategory(categories_tuple)

class JobPostForm(forms.Form):

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "200",
        'placeholder': "Job Title",
        }))
    
    job_type = forms.ChoiceField(
        choices=models.job_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "Job Type",
    }))



    work_type = forms.ChoiceField(
        choices=models.work_type,
        widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "work Type",
    }))

    
    job_location = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "200",
        'placeholder': "Job Location",
        }))
    
    

    job_salary = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'type' : 'number',
        'placeholder': "Job Salary",
        'min' : '8',
        'max' : '12',
        }))
    
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        # 'type' : 'image',
        # 'placeholder': "Image",
    }))


    job_description = forms.CharField(widget=forms.Textarea(attrs={
    'class' : 'ckeditor',
    'required' : True,
    'cols' : 6,
    'id' : 'job_description'
        }))
    
    
    responsibility = forms.CharField(widget=forms.Textarea(attrs={
    'class' : 'ckeditor',
    'required' : True,
    'cols' : 6,
    'id' : 'responsibility'
        }))

    qualifications = forms.CharField(widget=forms.Textarea(attrs={
    'class' : 'ckeditor',
    'required' : True,
    'cols' : 6,
    'id' : 'qualifications'
        }))

    company_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "200",
        'placeholder': "Company Name",
        }))
    

    company_link = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'form-control',
        'type' : 'url',
        'placeholder': "Company Link",
    }))
    

    about_company = forms.CharField(widget=forms.Textarea(attrs={
    'class' : 'ckeditor',
    'required' : True,
    'cols': 6,
    'id' : 'about_company'
        }))
    

    categories = models.JobCategory.objects.all()

    categories_list = []
    for c in categories:
        categories_list.append((str(c), str(c)))

    categories_tuple = tuple(categories_list)

    job_categories = models.JobCategory(categories_tuple)

    job_category = forms.ChoiceField(widget=forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "Job Category",
    }))



    job_category = forms.ChoiceField(
        choices = categories_tuple,
        widget = forms.Select(attrs={
        'class': 'form-control',
        'type' : 'radio',
        'placeholder': "Job Category",
    }))

    
    

    # class Meta:
    #     model = models.NewJob
    #     fields = '__all__'
    #     expect = ('date')



class CommentForm(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "200",
        'placeholder': "Enter Your Name",
        }))

        job = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "200",
        'placeholder': "Enter Your Job",
        }))

        message = forms.CharField(widget=forms.Textarea(attrs={
        'class': "form-control", 
        'cols': "6",
        'placeholder': 'Leave A Comment Here'
            }))

        image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
            'class': 'form-control bg-white',
        }))



class EmployeeDetailForm(forms.Form):
        name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "200",
        'placeholder': "Your Name",
        }))

        email = forms.EmailField(widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'type' : 'email',
            'placeholder': "Your Email",
            }))


        linkedin_link = forms.URLField(widget=forms.URLInput(attrs={
            'class': 'form-control',
            'type' : 'url',
            'placeholder': "LikedIn Link",
        }))


        address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control bg-white',
        'type' : 'text',
        'size': "300",
        'placeholder': "Your Address",
        }))


        phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'type' : 'text',
        'size': "13",
        'placeholder': "Your Correct Phone Number",
        }))


        cv = forms.FileField(widget=forms.FileInput(attrs={
            'class': 'form-control bg-white',
            'required' : False,
        }))



        cl = forms.FileField(widget=forms.FileInput(attrs={
            'class': 'form-control bg-white',
            'required' : False,
        }))
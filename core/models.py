from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class JobCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


job_type = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
)

work_type = (
    ('Remote', 'Remote'),
    ('Hybrid', ' Hybrid'),
    ('On-Stie', 'On-Stie')
)

class Job(models.Model):
    title = models.CharField(max_length=200)
    job_type = models.CharField(max_length=15, choices=job_type, default='Full Time')
    work_type = models.CharField(max_length=15, choices=work_type, default='Remote')
    job_location = models.CharField(max_length=200)

    job_salary = models.IntegerField(default=10, validators=[MaxValueValidator(20), MinValueValidator(8)])
    # start_salary_range = models.IntegerField(default=10, validators=[MaxValueValidator(20), MinValueValidator(8)])
    # end_salary_range = models.IntegerField(default=10, validators=[MaxValueValidator(20), MinValueValidator(8)])


    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='newjob_images/', default='job_default_img.jpg')

    job_description = RichTextField()    # Added newly
    responsibility = RichTextField()     # Added newly
    qualifications = RichTextField()     # Added newly

    company_name = models.CharField(max_length=200)
    company_link = models.URLField(null=True, blank=True) 

    about_company = RichTextField()     # Added newly

    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Employee_Detail(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    linkedin_link = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=300)
    phone = models.CharField(max_length=13)
    cv = models.FileField(upload_to='cv/')
    cl = models.FileField(upload_to='cl/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name









class Comment(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    message = models.TextField()
    image = models.ImageField(upload_to='comments_images/', default='avatar.png', null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



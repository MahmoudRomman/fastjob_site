from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models
import random



def index(request):
    categories = models.JobCategory.objects.all()
    jobs = models.Job.objects.all()

    comments = models.Comment.objects.all()

    randomlist = []
    for i in range(0, 100):
        n = random.randint(0, len(comments)-1 )
        if len(randomlist) < 4:
            if n not in randomlist:
                randomlist.append(n)



    comment_1 = comments[randomlist[0]]
    comment_2 = comments[randomlist[1]]
    comment_3 = comments[randomlist[2]]
    comment_4 = comments[randomlist[3]]




    jobs_data = {}
    for cat in categories:
        # print(cat.id)
        job_count = models.Job.objects.filter(job_category = cat.id)
        job_name = models.JobCategory.objects.get(id = cat.id)
        jobs_data[str(job_name.name)] = len(job_count)




    print("*" * 100)
    print(jobs_data)

    context = {
        'categories' : categories,
        'jobs' : jobs,
        'jobs_data' : jobs_data,
        'comment_1' : comment_1,
        'comment_2' : comment_2,
        'comment_3' : comment_3,
        'comment_4' : comment_4,
    }
    return render(request, 'core/index.html', context)



def contact(request):
    form = forms.ContactForm()

    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            
            contact = models.Contact.objects.create(
                name = name,
                email = email,
                message = message,
            )

            contact.save()
            
            messages.success(request, "Your Message Sent Successfully!")
            return redirect("index")
            

    context = {
        'form' : form,
    }


    return render(request, 'core/contact.html', context)



def job_list(request):

    jobs = models.Job.objects.all()


    context = {
        'jobs' : jobs,
    }
    return render(request, 'core/job-list.html', context)



def job_post(request):

    # form = forms.JobPostForm()
    form = forms.JobPostForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            title = form.cleaned_data.get("title")
            job_type = form.cleaned_data.get("job_type")
            work_type = form.cleaned_data.get("work_type")
            job_location = form.cleaned_data.get("job_location")
            job_salary = form.cleaned_data.get("job_salary")
            image = form.cleaned_data.get("image")

            job_description = form.cleaned_data.get("job_description")
            responsibility = form.cleaned_data.get("responsibility")
            qualifications = form.cleaned_data.get("qualifications")

            company_name = form.cleaned_data.get("company_name")
            company_link = form.cleaned_data.get("company_link")

            about_company = form.cleaned_data.get("about_company")

            job_category = form.cleaned_data.get("job_category")

            
            # Converting job_category to a type to suatie the job_category type inclded in the NewJob model 
            job_category =  models.JobCategory.objects.filter(name=job_category)
            job_category = job_category[0]

            new_job = models.Job.objects.create(
                title = title,
                job_type = job_type,
                work_type = work_type,
                job_location = job_location,
                job_salary = job_salary,
                image = image,

                job_description = job_description,
                responsibility = responsibility,
                qualifications = qualifications,

                company_name = company_name,
                company_link = company_link,

                about_company = about_company,

                job_category = job_category
                )

            new_job.save()
            messages.success(request, "Your New Job Saved Successfully!")
            return redirect("index")



    context = {
        'form' : form,
    }
    return render(request, 'core/job-post.html', context)



def job_detail(request, pk):

    job = models.Job.objects.get(id=pk)
    form = forms.EmployeeDetailForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            linkedin_link = form.cleaned_data.get("linkedin_link")
            address = form.cleaned_data.get("address")
            phone = form.cleaned_data.get("phone")
            cv = form.cleaned_data.get("cv")
            cl = form.cleaned_data.get("lv")


            employee_detail = models.Employee_Detail.objects.create(
                name = name,
                email = email,
                linkedin_link = linkedin_link,
                address = address,
                phone = phone,
                cv = cv,
                cl = cl,
                )

            employee_detail.save()
            messages.success(request, "Your Application Sent Successfully!")
            return redirect("job_detail", pk)

    context = {
        'job' : job,
        'form' : form,
    }
    return render(request, 'core/job-detail.html', context)


def testimonial(request):

    form = forms.CommentForm(request.POST or None, request.FILES or None)
    comments = models.Comment.objects.all()

    randomlist = []
    for i in range(0, 100):
        n = random.randint(0, len(comments)-1 )
        if len(randomlist) < 4:
            if n not in randomlist:
                randomlist.append(n)



    comment_1 = comments[randomlist[0]]
    comment_2 = comments[randomlist[1]]
    comment_3 = comments[randomlist[2]]
    comment_4 = comments[randomlist[3]]

    
    if request.method == "POST":
        form = forms.CommentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            job = form.cleaned_data.get("job")
            message = form.cleaned_data.get("message")
            image = form.cleaned_data.get("image")
            

            comment = models.Comment.objects.create(
                name = name,
                job = job,
                message = message,
                image = image
                )

            comment.save()
            messages.success(request, "Your Comment Added Successfully!")
            return redirect("index")



    context = {
        'form' : form,
        'comment_1' : comment_1,
        'comment_2' : comment_2,
        'comment_3' : comment_3,
        'comment_4' : comment_4,

    }
    return render(request, 'core/testimonial.html', context)



def about(request):
    return render(request, 'core/about.html')
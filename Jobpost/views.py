from django.shortcuts import render,redirect
from django.template import Context,RequestContext
from django.contrib import messages

from Jobpost.models import Job
from Jobpost.forms import CreateJob

from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def JobUpload(request):
    if request.method == 'POST':
        form = CreateJob(request.POST,request.FILES)
        if form.is_valid():
             f = form.save()
             msg_plain = render_to_string('Jobpost/jobemail.txt',{'f': f})
             msg_html = render_to_string('Jobpost/jobemail.html',{'f': f })
             send_mail('Thank you for posting on Hemotely.',msg_plain,settings.EMAIL_HOST_USER,[f.companyEmail],fail_silently = False, html_message=msg_html)
             return redirect('/')
    else:
        form = CreateJob()
        jobs = Job.objects.all()[:6]
        context_instance = RequestContext(request,{'context_name':'jobupload',})
    return render(request,'Jobpost/job_post.html',{'context_instance': context_instance,'form':form,'jobs':jobs})

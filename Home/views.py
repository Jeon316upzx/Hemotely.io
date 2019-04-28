from django.shortcuts import redirect,render
from django.template import Context,RequestContext
from django.contrib import messages
from Jobpost.models import Job
from django.db.models import Q




def home(request):
    myjob =Job.objects.all().order_by('postedDate')
    query = request.GET.get("q")
    if query:
        myjob = myjob.filter(
        Q(position__icontains=query)        |
        Q(companyName__icontains=query)     |
        Q(location__icontains=query)        |
        Q(category__icontains=query)
        ).distinct()
    context_instance = RequestContext(request,{'context_name':'home',})

    return render(request,'Home/index.html',{'context_instance': context_instance,'myjob': myjob})

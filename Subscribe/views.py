from django.shortcuts import render,redirect
from Subscribe import forms
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def Sub(request):
    if request.method =='POST':
        form = forms.Subscribe_form(request.POST)
        if form.is_valid():
            s = form.save()
            msg_plain = render_to_string('Subscribe/welcome.txt',{'s': s})
            msg_html = render_to_string('Subscribe/welcome.html',{'s': s})
            send_mail('Welcome to Hemotely.',msg_plain,'DonotReply<Do_not_Reply@Hemotely.com.ng>',[s.Email],fail_silently = False, html_message=msg_html)
            messages.info(request,s.Email)
            return redirect('/subscribe')
    else:
        form = forms.Subscribe_form()
    return render(request,'Subscribe/subscribe.html',{'form': form})

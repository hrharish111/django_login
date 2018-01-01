from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .forms import SignupForm,ViewSlot
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from django.utils.http import  urlsafe_base64_decode,urlsafe_base64_encode
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.views import login
from .models import NewSpace,NewSlot
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request,"login_app/base.html")

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)

            message = render_to_string('login_app/account_activation.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your blog account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject,message, to=[to_email])
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration.')
            # return render(request, 'acc_active_sent.html')
    else:
        form = SignupForm()
    return render(request, 'login_app/signup.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    print("thhisnis th user",urlsafe_base64_decode(uidb64))
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

def loginuser(request):
    if request.user.is_authenticated():
        return  HttpResponse("already_loged in")
    else:
        return login(request)

@login_required(login_url = '/')
def slot_viewer(request):
    if request.method == "POST":
        form =ViewSlot(request.POST)
        if form.is_valid():
            form_cleandata = request.POST.get('slot_name')
            data_response = get_object_or_404(NewSpace,pk =form_cleandata)

            return render(request,'login_app/slot_viewer.html',{'form':form,'data_response': data_response})
    else:
        form =ViewSlot()
    return render(request,"login_app/slot_viewer.html",{"form":form})
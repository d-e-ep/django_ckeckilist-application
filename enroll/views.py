from django.shortcuts import render
from .forms import CandidatesEnrollment
from .models import user

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = CandidatesEnrollment(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['first_name']
            ln = fm.cleaned_data['last_name']
            em = fm.cleaned_data['email']
            mn = fm.cleaned_data['mobile_no']
            pw = fm.cleaned_data['password']
            reg = user(first_name=nm, last_name=ln, email=em, mobile_no=mn, password=pw)
            reg.save()
            fm = CandidatesEnrollment()
    else:
        fm = CandidatesEnrollment()
    cand =user.objects.all()
    return render(request , 'enroll/addandshow.html', {'form':fm,'cnd':cand})
    
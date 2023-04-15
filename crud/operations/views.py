from django.shortcuts import render,HttpResponseRedirect
from .forms import detailsregister
from .models import details
# Create your views here.
# add and retrive here
def home(request):
    if request.method  =='POST':
        fm  = detailsregister(request.POST) 
        if fm.is_valid():
            # fm.save() this method is used when to save all data
            nm  = fm.cleaned_data['name']
            em  = fm.cleaned_data['email']
            pw  = fm.cleaned_data['password']
            reg  = details(name = nm,email = em,password = pw)
            reg.save()
            fm  =  detailsregister()
    else:
        fm  =  detailsregister()
    det = details.objects.all()
    return render(request,'operations/home.html',{'form':fm,'details':det})
def update(request):
    return render(request,'operations/updatescreen.html')

# deletion will be performed here
def delete_data(request,id):
    if request.method =='POST':
        pid = details.objects.get(pk=id) 
        pid.delete()
        return HttpResponseRedirect('/home/')


# updation here

def update_data(request,id):
    if request.method =='POST':
        pid = details.objects.get(pk=id)
        fm = detailsregister(request.POST,instance=pid)
        if fm.is_valid():
            fm.save()
    else:
            pid = details.objects.get(pk=id)
            fm = detailsregister(instance=pid)
    return render(request,'operations/updatescreen.html',{'form':fm})

from django.shortcuts import render
from .forms import Student,Specify
from django.http import HttpResponseRedirect

# Create your views here.
def success(request):
    return render(request,'app/success.html')

def showfromdata(request):
    if request.method=='POST':
        fm=Student(request.POST)
        if fm.is_valid():
            print('form is validated')
            name=fm.cleaned_data['name']
            agree=fm.cleaned_data['agree']
            password=fm.cleaned_data['password']
            email=fm.cleaned_data['email']
            roll=fm.cleaned_data['roll']
            price=fm.cleaned_data['price']
            rate=fm.cleaned_data['rate']
            comment=fm.cleaned_data['comment']
            website=fm.cleaned_data['website']
            description=fm.cleaned_data['description']
            feedback=fm.cleaned_data['feedback']
            notes=fm.cleaned_data['notes']
            print('name',name)
            print('agree',agree)
            print('password',password)
            print('email',email)
            print('roll',roll)
            print('price',price)
            print('rate',rate)
            print('comment',comment)
            print('website',website)
            print('description',description)
            print('feedback',feedback)
            print('notes',notes)
            fm=Student()
            return HttpResponseRedirect('success')
    else:
        fm=Student()
    return render(request,'app/home.html',{'form':fm})


def collect(request):
    if request.method=='POST':
        fm=Specify(request.POST)
        if fm.is_valid():
         print('form is validated')
         name=fm.cleaned_data['name']
         email=fm.cleaned_data['email']
         password=fm.cleaned_data['password']
         print('name:',name)
         print('email',email)
         print('password',password)
         fm=Specify()
         return HttpResponseRedirect('success')
    else:
        fm=Specify()
    return render(request,'app/specify.html',{'form':fm})

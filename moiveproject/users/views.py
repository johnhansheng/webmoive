#from django.shortcuts import render
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout

def signup(request):
    if request.method=='POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password1=form.cleaned_data.get(password1)
            user=authenticate(username=usernam,password=raw_password1)
            auth_login(request,user)
            return  redirect('home')
        else:
            print(form.errors)

    else:
        form=SignUpForm()
    return render(request,'registration/signup.html',{'form':form})





# Create your views here.

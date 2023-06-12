from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import profile
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        userlogin=auth.authenticate(username=username,password=password)

        if userlogin is not None:
            auth.login(request,userlogin)
            return redirect('explore')
        else:
            messages.info(request,'Username Or Password is Incorrect')
            return redirect('login')

    return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        password=request.POST['password']
        retypepassword=request.POST['retypepassword']
        if password==retypepassword:
             if User.objects.filter(username=username).exists():
                 messages.info(request,'Username already used')
                 return redirect('register')
             else:
                 user=User.objects.create_user(username=username,email=None,password=password)
                 user.save()
                 details=profile(followers=[],following=[],userinfo=user)
                 details.save()
                 return redirect('login')
        else:
            messages.info(request,'Password is not same')
            return redirect('register')  
    else:    
        return render(request,'register.html')
def home(request):
    curuser=request.user
    profileobj=profile.objects.get(userinfo=User.objects.get(username=curuser))
    #user2=profileobj.userinfo.username
    nfers=len(profileobj.followers)
    nfing=len(profileobj.following)
    curuser=str(curuser)
    pf=profile.objects.get(userinfo=User.objects.get(username=curuser))
    users=User.objects.filter(is_staff=False)    
    return render(request,'home.html',{'nfing':nfing,'nfers':nfers,'curuser':curuser,'pf':pf,'users':users})

#def listofusers(request):
    curuser=request.user
    curuser=str(curuser)
    pf=profile.objects.get(userinfo=User.objects.get(username=curuser))
    users=User.objects.filter(is_staff=False)
    print(type(curuser))
    return render(request,'home.html',{'users':users,'cur':curuser,'pf':pf})
def follow(request):
    curuser=request.user
    pf=profile.objects.get(userinfo=User.objects.get(username=curuser))
    if request.method== 'POST':
        uf=request.POST['u_username']
        pf2=profile.objects.get(userinfo=User.objects.get(username=uf))
        pf.following.append(uf)
        pf.save()
        pf2.followers.append(str(curuser))
        pf2.save()
    return redirect('home')
def unfollow(request):
    curuser=request.user
    pf=profile.objects.get(userinfo=User.objects.get(username=curuser))
    if request.method== 'POST':
        uf=request.POST['u_username']
        pf2=profile.objects.get(userinfo=User.objects.get(username=uf))
        pf.following.remove(uf)
        pf.save()
        pf2.followers.remove(str(curuser))
        pf2.save()
    return redirect('home')
def fers(request):
    return render(request,'fers.html')
def fings(request):
    return render(request,'fings.html')
def explore(request):
    curuser=request.user
    pf=profile.objects.get(userinfo=User.objects.get(username=curuser))
    pf.followingtweet={}
    for p in pf.following:
        pf.followingtweet[p]=[]
        for tweet in profile.objects.get(userinfo=User.objects.get(username=p)).tweet:
            pf.followingtweet[p].append(tweet)
            profile.objects.get(userinfo=User.objects.get(username=p)).tweet_time
            pf.save()
    return render(request,'explore.html',{'curuser':str(curuser),'pf':pf})
def addtweet(request):
    curuser=request.user
    tweetinput=request.POST.get('tweetinput')
    pf=profile.objects.get(userinfo=User.objects.get(username=curuser))
    pf.tweet.append(tweetinput)
    pf.tweet_time.append(datetime.now())
    pf.save()       
    return redirect('explore')
def pagevisit(request):
    curuser=request.GET.get('data')
    if User.objects.filter(username=curuser).exists():
      profileobj=profile.objects.get(userinfo=User.objects.get(username=curuser))
      nfers=len(profileobj.followers)
      nfing=len(profileobj.following)
      return render(request,'pagevisit.html',{'curuser':curuser,'pf':profileobj,'nfing':nfing,'nfers':nfers})
    messages.info(request,'No User Found')
    return redirect('explore')      



from django.shortcuts import render,redirect,get_object_or_404
from.models import posts,comment,likebutton
from django.http import HttpResponse
from django.contrib.auth.models import User
from.forms import renew
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    user=request.user
    post = posts.objects.all().order_by('-date_posted')
    users = User.objects.all()
    context ={
        'posts':post,
        'all_users':users
    }
    return render(request,'twitter/home.html',context)

def interest(request):
    if request.method=='POST':
        stuff=request.POST['soft']
        grab=get_object_or_404(posts,id=stuff)
        user = request.user
        if user in grab.liked.all():
            grab.liked.remove(user)
        else:
           grab.liked.add(user)
    return redirect('/')

def userpost(request,**kwargs):
    grab =get_object_or_404(User,username=kwargs.get('username'))
    post = posts.objects.filter(author=grab).order_by('-date_posted')
    context = {
    'posts': post,
    }
    return render(request,'twitter/userposts.html',context)


def add(request):
    if request.method == 'POST':
        collect = request.POST['stuff']
        collects = request.POST['stiff']

        store = posts(author=request.user,content = collect,tagline=collects)
        store.save()
        return redirect('/')
    else:
        return render(request,'twitter/new.html')
def update(request,id):
    grab = get_object_or_404(posts,id=id)
    if request.method == 'POST':
        if request.user == grab.author:
            form =renew(request.POST,instance=grab)
            if form.is_valid():
                form.save()
                messages.success(request,'Updated successfully')
                return redirect('detail' +  grab )
        else:
            messages.error(request,'You are not the author of this post')
            return redirect('detail' + grab)
    else:
        return HttpResponse('invalid action')
def about(request):
    return render(request,'twitter/about.html')


def detail(request,id):
    grab = get_object_or_404(posts,id=id)
    filt = comment.objects.filter(post=grab).order_by('-date_posted')
    context ={
        'post':grab,
        'comments':filt
    }
    return render(request,'twitter/detail.html',context)
def Comment(request,id):
    if request.method == 'POST':
        user = request.user
        word = request.POST['text']
        post = get_object_or_404(posts,id=id)
        store = comment(post=post,author=user,content=word)
        store.save()
        return redirect('/')
    else:
        return HttpResponse('Invalid action')

def remove(request,id):
    grab=get_object_or_404(posts,id=id)
    if request.user == grab.author:
        grab.delete()
        messages.success(request,'Deleted successfully')
        return redirect('/')
    else:
        messages.error(request,'Invalid user')
    return render(request,'twitter/delete.html',{'post':grab})



def search(request):
    if request.method == 'GET':
        grab = request.GET.get('search')
        user = User.objects.all()
        if grab:
            store = Q(Q(content__icontains=grab))
            save = posts.objects.filter(store)
            return render(request,'twitter/search.html',{'store':save})
        return render(request, 'twitter/search.html', {})
    else:
        return HttpResponse('Invalid action')
def commentpost(request,id):
    grab = get_object_or_404(posts,id=id)
    com = comment.objects.filter(post=grab).order_by('-date_posted')
    context = {
        'post':grab,
        'posts':com
    }
    return render(request,'twitter/comments.html',context)
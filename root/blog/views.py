from django.shortcuts import render, render_to_response, RequestContext
#import pdb
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm

from django.core.context_processors import csrf

# Create your views here.

from .models import Post, Contact, About, Gallery, Slidshow
from .forms import ContactForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse

from django.template import Context, loader


def index(request):
    """ Home page """
    # this is use for coockies ###
    language = 'en-gb'# this variable will store what in the coockies
    session_language = 'en-gb' # this variable will store what is our session

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    args = {}
    args.update(csrf(request))
    args['index'] = Post.objects.all()
    args['language'] = language
    args['session_language'] = session_language
    ##########

    posts = Post.objects.filter(published=True).order_by('-created')[:7]

    paginator = Paginator(posts, 2)

    page_num = request.GET.get('page', 1)
    page = paginator.page(page_num)

    try:
        page = paginator.page(page_num)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        page = paginator.page(1)

    ctx = {'page':page, 'language': language }
    slidshows = Slidshow.objects.all().order_by('-created')

    return render_to_response('index.html', locals(), context_instance=RequestContext(request))

# working with the cookie
def language(request, language='en-gb'):
    response = HttpResponse('setting language to %s' % language)

    response.set_cookie('lang', language)
    request.session['lang'] = language
    return response

def post(request, id):
    """ Post """
    post = Post.objects.get(id=id)
    return render_to_response('post.html', locals(), context_instance=RequestContext(request))

def like_post(request, id):
    if id:
        post = Post.objects.get(id=id)
        count = post.like
        count += 1
        post.like = count
        post.save()
    return HttpResponseRedirect('/post/%s' % id)




def category(request):
    """ Category """
    posts = Post.objects.all().order_by('-created')
    return render_to_response('category.html', locals(), context_instance=RequestContext(request))


def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response('tagpage.html', {'posts':posts, 'tag':tag })


def about(request):
    abouts = About.objects.all().order_by('-created')
    return render_to_response('about.html', locals(), context_instance=RequestContext(request))


def service(request):
    #posts = Post.objects.all().order_by('-created')
    return render_to_response('service.html', locals(), context_instance=RequestContext(request))

def gallery(request):
    galleries = Gallery.objects.all()
    return render_to_response('gallery.html', {'galleries' : galleries}, context_instance=RequestContext(request))

def slidshow(request):
    slidshows = Slidshow.objects.all().order_by('-id')
    return render_to_response('slidshow.html', {'slidshows' : slidshows}, context_instance=RequestContext(request))

def contact(request):
    """ Contact Form """
    success = False
    name = ''
    email = ''
    message = ''
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST or None)
        
        if contact_form.is_valid():
            success = True
            name    = contact_form.cleaned_data['name']
            email   = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
        
    else:
        contact_form = ContactForm()
        
    ctx = {'contact_form': contact_form, 'name': name, 'email':email, 'message':message, 'success':success }
        
    return render_to_response('contact.html', ctx, context_instance=RequestContext(request))

## LOGIN

def login(request):
    c ={}
    c.update(csrf(request))
    return render_to_response('login.html', c, context_instance=RequestContext(request))

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('loggedin')
    else:
        return HttpResponseRedirect('invalid')

def loggedin(request):
    return  render_to_response('loggedin.html', {'full_name': request.user.username} )

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = MyRegistrationForm()
    print args
    return  render_to_response('register.html', args)

def register_success(request):
    return render_to_response('register_success.html')

def search_titles(request):
    if request.method == "POST":
        search_text = request.Post['search_text']
    else:
        search_text = ''

    posts = Post.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html', {'posts': posts })
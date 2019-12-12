from django.shortcuts import render
from django.views import View
from .forms import RegisterForm, SearchForm, LoginForm, ReviewForm, NewsletterForm
from .models import Review, AppUser, Subscription
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import cloudinary
import base64

# We will map urls pattern to this view function in 'urls.py' module(file)


def all_review (request):
    review = Review.objects.all().order_by('-date_created')
    page = request.GET.get('page', 1)
    paginator = Paginator(review, 9)
    try:
        review = paginator.page(page)
    except PageNotAnInteger:
        review = paginator.page(1)
    except EmptyPage:
        review = paginator.page(paginator.num_pages)
    return render(request, 'main/review-all.html', {'review': review})

def error_404_view(request, exception):
    data = {"name": "127.0.0.1:8000"}
    return render(request,'main/404.html', data)


def reset_password(request):
    return render(request, 'password_reset/base.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    recent_review = Review.objects.filter().order_by('-date_created')[:9]
    page = request.GET.get('page', 1)
    paginator = Paginator(recent_review, 9)
    try:
        review = paginator.page(page)
    except PageNotAnInteger:
        review = paginator.page(1)
    except EmptyPage:
        review = paginator.page(paginator.num_pages)
    form = SearchForm()
    news = NewsletterForm()
    return render(request, 'main/home.html', 
                  {'form':form, 'news':news, 'review':recent_review,})

def subscribe(request):
    if request.method == 'POST':
        message = ''
        news = NewsletterForm(request.POST)
        if news.is_valid():
            email = news.cleaned_data.get('email')
            try:
                Subscription.objects.create(email=email)
                message = "You have subscribed to our newsletter"
            except:
                pass
        recent_review = Review.objects.filter().order_by('-date_created')[:9]
        page = request.GET.get('page', 1)
        paginator = Paginator(recent_review, 9)
        try:
            review = paginator.page(page)
        except PageNotAnInteger:
            review = paginator.page(1)
        except EmptyPage:
            review = paginator.page(paginator.num_pages)
        form = SearchForm()
        return render(request, 'main/home.html', 
                {'form':form, 'news':news,'review':recent_review, 'message':message})


def about(request):
    return render(request, 'main/about.html')


class Register(View):
    form_class = RegisterForm
    template_name = 'main/sign-up.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            register_form = form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            register_form.set_password(password)
            register_form.save()
            new_user = authenticate(username=username,
                                    password=password,
                                    )
            login(request, new_user)

            return redirect('/review/')

        return render(request, self.template_name, {'form': form})


class Authentication(View):
    form_class = LoginForm
    template_name =  'main/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print(request.META['HTTP_REFERER'])
            return redirect('/write-review/')
        else:
            return render(request, self.template_name, {'message': 'Wrong username or password', 'form':form})


def searchReview(request):
    if request.method == 'GET':
        location = request.GET['location']
        address = request.GET['address']
        state = request.GET['state']

        try:
            if (location != ''):

                review = Review.objects.filter(Q(location__icontains=location) |
                                                     Q(street_name__icontains=address) |
                                                     Q(state__icontains=state)).order_by('-date_created')
                if not review:
                    review = Review.objects.filter(location__icontains=location).order_by('-date_created')
                else:
                    review = review
                context = {'review':review}
                page = request.GET.get('page', 1)
                paginator = Paginator(review, 9)
                try:
                    review = paginator.page(page)
                except PageNotAnInteger:
                    review = paginator.page(1)
                except EmptyPage:
                    review = paginator.page(paginator.num_pages)
            else:
                review = Review.objects.filter(state__icontains=state, location__icontains=location).order_by('-date_created')
                news = NewsletterForm()
                context = {'review':review, 'news': news}
                page = request.GET.get('page', 1)
                paginator = Paginator(review, 16)
                try:
                    review = paginator.page(page)
                except PageNotAnInteger:
                    review = paginator.page(1)
                except EmptyPage:
                    review = paginator.page(paginator.num_pages)
            return render(request, 'main/review-all.html', context)
        except Review.DoesNotExist:
            return render(request, 'main/error.html') 
        
@login_required(login_url='/signin/')
def writeReview(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        default_url = 'https://res.cloudinary.com/dkozdkklg/image/upload/v1575174676/tom-thain-_0URG2ZegMc-unsplash_dmgaje.jpg'
        if form.is_valid():
            review = form.save(commit=False)
            if request.FILES.get('image1'):
                image1 = cloudinary.uploader.upload(request.FILES.get('image1'))
                img1 = image1['url']
            else:
                img1 = default_url
            if request.FILES.get('image2'):
                image2 = cloudinary.uploader.upload(request.FILES.get('image2'))
                img2 = image2['url']
            else:
                img2 = default_url
            if request.FILES.get('image3'):
                image3 = cloudinary.uploader.upload(request.FILES.get('image3'))
                img3 = image3['url']
            else:
                img3 = default_url
            if request.FILES.get('image4'):
                image4 = cloudinary.uploader.upload(request.FILES.get('image4'))
                img4 = image4['url']
            else:
                img4 = default_url
            new_list = [img1, img2, img3, img4]
            review.images.extend(new_list)
            review.owner = request.user
            form.save()

        return redirect('/review/')

    else:
        form = ReviewForm()
        news = NewsletterForm()
        return render(request, 'main/new-review.html', {'form': form, 'news':news})


def detailReview(request, review_id):
    review = Review.objects.get(review_id=review_id)
    similar_review = Review.objects.filter(location__icontains=review.location).order_by('-date_created')[:3]
    user = AppUser.objects.get(username=review.owner.username)
    context = {'review': review, 'similar_review':similar_review, 'user':user}
    return render(request, 'main/single-review.html',context)

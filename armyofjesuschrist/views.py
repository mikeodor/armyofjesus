from django.shortcuts import render, get_object_or_404,redirect
from .models import (UpcomingEvent, NextBigEvent, slide, LatestSermon,
                     donation, address, phone_number, Email, Ministries, pastors, video, CustomerInfo,prayer,breadcrumb)
from django.views.generic import ListView, MonthArchiveView, DetailView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from django.core.mail import send_mail


def index(request):
    events = UpcomingEvent.objects.all().order_by('month')
    nextevent = NextBigEvent.objects.all()
    slideshow = slide.objects.all()
    latestSermon = LatestSermon.objects.all().order_by('-date')[:3]
    Donation = donation.objects.all()
    email = Email.objects.all()
    phone = phone_number.objects.all()
    location = address.objects.all()
    bread=breadcrumb.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(events, 4)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)
    
    context = {
       
        'events': events,
        'nextevent': nextevent,
        'slide': slideshow,
        'latestSermon': latestSermon,
        'donation': Donation,
        'email': email,
        'phone': phone,
        'location': location,
        'bread':bread
    }

    return render(request, 'armyofjesuschrist/index.html', context)


class sermonlist(ListView):
    model = LatestSermon
    context_object_name = 'sermon'
    template_name = 'armyofjesuschrist/sermons.html'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.all()
        context['phone'] = phone_number.objects.all()
        context['location'] = address.objects.all()
        context['sermonside'] = LatestSermon.objects.all()[:3]
        return context


class detailpost(DetailView):
     model = LatestSermon
     context_object_name = 'sermon'
     

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.all()
        context['phone'] = phone_number.objects.all()
        context['location'] = address.objects.all()
        context['sermonside'] = LatestSermon.objects.all()[:3]

        return context


def Ministry(request):
    email = Email.objects.all()
    phone = phone_number.objects.all()
    location = address.objects.all()
    ministry = Ministries.objects.all()
    pastor = pastors.objects.all()
    context = {
        'email': email,
        'phone': phone,
        'location': location,
        'ministry': ministry,
        'pastor': pastor,
    }
    return render(request, 'armyofjesuschrist/department.html', context)


def contact(request):
    email = Email.objects.all()
    phone = phone_number.objects.all()
    location = address.objects.all()
    context = {
        'email': email,
        'phone': phone,
        'location': location,
        

    }

   
    if request.method=='POST':
        name=request.POST['name']
        emailform=request.POST['emailform']
        message=request.POST['message']

        send_mail(
            name,
            message,
            emailform,
            ['michaelodor4@gmail.com']
        )
        context = {
        'email': email,
        'phone': phone,
        'location': location,
        "name":name }

        return render(request, 'armyofjesuschrist/contact.html',context)

    
    return render(request, 'armyofjesuschrist/contact.html', context)


class bloghome(ListView, MonthArchiveView):
    model = video
    
    date_field = "date_posted"
    allow_future = True
    template_name = 'armyofjesuschrist/video.html'
    context_object_name = 'post'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.all()
        context['phone'] = phone_number.objects.all()
        context['location'] = address.objects.all()
        return context

class videodetail(DetailView):
    model = video
    context_object_name = 'detailpost'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.all()
        context['phone'] = phone_number.objects.all()
        context['location'] = address.objects.all()
        context['post'] = video.objects.all().order_by('-date_posted')[0:3]
        return context

# def detail(request, pk):
#     post=Post.objects.all().order_by('-date_posted')[0:3]
#     detailpost=get_object_or_404(Post,pk=pk)
#     context={
#         'detailpost':detailpost,
#         'post':post,
#     }
#     return render(request, 'armyofjesuschrist/post_detail.html',context)


# class createpost(CreateView):
#     model=Post
#     context_object_name='post'

#     fields=['image','title','content']


def donationpage(request):

    email = Email.objects.all()
    phone = phone_number.objects.all()
    location = address.objects.all()
    context = {

        
        'email': email,
        'phone': phone,
        'location': location
    }
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phone=request.POST['phonenumber']
        amount=request.POST['amount']
        state=request.POST['state']
        email=request.POST['email']

        user=CustomerInfo.objects.create(firstname=firstname,lastname=lastname,phonenumber=phone,state=state,amount=amount, email=email)
        user.save()
        
        return render(request, 'armyofjesuschrist/payment.html',{"email":email,'phone':phone,'amount':amount})
    else:
         return render(request, 'armyofjesuschrist/donation.html',context)


def payment(request):
    email = Email.objects.all()
    phone = phone_number.objects.all()
    location = address.objects.all()
    context = {

        
        'email': email,
        'phone': phone,
        'location': location
    }
    
    return render(request, 'armyofjesuschrist/payment.html', context)



class prayerpoint(ListView):
    model = prayer
    context_object_name = 'prayer'
    template_name = 'armyofjesuschrist/prayerpointlist.html'
    ordering = ['-date_posted']
    paginate_by = 13

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.all()
        context['phone'] = phone_number.objects.all()
        context['location'] = address.objects.all()
        context['sermonside'] = LatestSermon.objects.all()[:3]
        return context

# class prayerdetailpost(DetailView):
#     model = prayerpoint
#     context_object_name = 'prayerd'
#     template_name = 'armyofjesuschrist/prayerpointdetail.html'
     

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['email'] = Email.objects.all()
#         context['phone'] = phone_number.objects.all()
#         context['location'] = address.objects.all()
       

#         return context


class test(DetailView):
    model=prayer
    template_name = 'armyofjesuschrist/prayerpointdetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['email'] = Email.objects.all()
        context['phone'] = phone_number.objects.all()
        context['location'] = address.objects.all()
       

        return context


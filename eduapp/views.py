from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# from django.db.models import Q
# from datetime import datetime

from .models import Activity
from .forms import Activity,EventForm,CatgoryForm,ClassForm,VenueForm

from .models import Profile
from .models import Activity

#USER SIDE org
def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == 'POST':
        print("test")
        first_name = request.POST['reg_first_name']
        last_name = request.POST['reg_last_name']
        phone_code = request.POST['reg_phone_code']
        mobile = request.POST['reg_mobile']
        email =  request.POST['reg_email']
        dob = request.POST['reg_dob']
        gender =  request.POST['reg_gender']
        location_id = request.POST['reg_location_id'] 
        national_status = request.POST['reg_national_status']
        nationality =  request.POST['reg_nationality']
        password = request.POST['reg_password']
        password2 = request.POST['reg_password_confirmation']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=email, email=email, password=password,first_name=first_name,last_name=last_name)
                user.save()
                print("user")

                #log user in and redirect to settings page
                user_login = auth.authenticate(username=email, password=password)
                auth.login(request, user_login)
                print("login")

                #create a Profile object for the new user
                user_model = User.objects.get(username=email)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id,phone_code=phone_code,mobile=mobile,dob=dob,gender=gender,location_id=location_id,national_status=national_status,nationality=nationality)
                new_profile.save()
                print("profile")
                return redirect('index')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        
    else:
        return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        print("kjfg")
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, "login.html")


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')


def search_event(request):
    return render(request,"search_event.html")

def search_class(request):
    return render(request,"search_class.html")

def search_venue(request):
    return render(request,"search_venue.html")

def search_all(request):
    return render(request,"search_all.html")


#ADMIN SIDE 
   
@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
   # enquiry=models.Request.objects.all().order_by('-id')
  #  customers=[]
    #for enq in enquiry:
      #  customer=models.Customer.objects.get(id=enq.customer_id)
      #  customers.append(customer)
    #dict={
   # 'total_customer':models.Customer.objects.all().count(),
   # 'total_mechanic':models.Mechanic.objects.all().count(),
   # 'total_request':models.Request.objects.all().count(),
  #  'total_feedback':models.Feedback.objects.all().count(),
    #'data':zip(customers,enquiry),
   # }
     return render(request,'admin/adminhome.html')

    # return render(request,'admin/adminhome.html',context=dict)  

def add_activity(request):
    activities=Activity.objects.all()
    print(activities)
    context={'activities':activities}   
    return render(request,'admin/add_activity.html',context)
    
def edit_activity(request, id):
    activity = Activity.objects.get(id=id)
    
    return render(request, 'edit_activity.html')

def delete_activity(request, id):
    activity = Activity.objects.get(id=id)
    activity.delete()
    return redirect('add_activity')


def event_view(request):
     form=EventForm()
     print("one")
     if request.POST:
        print("two")
        form=EventForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            print("three")
            form.save()
            return redirect('admin-dashboard')
     else:
        initial_values = {'catagory': 'Event'}
        form = EventForm(initial=initial_values)
     return render(request,'admin/first.html',{'form':form}) 
     
def class_view(request):
     form=ClassForm()
     if request.POST:
        print("req is at post ")
        form=ClassForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            print("form saved")
            return redirect('admin-dashboard')
     else:
        initial_values = {'catagory': 'Class'}
        form = ClassForm(initial=initial_values)
     return render(request,'admin/second.html',{'form':form}) 
     
def venue_view(request):
     form=VenueForm()
     if request.POST:
        form=EventForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
     else:
        initial_values = {'catagory': 'Venue'}
        form = VenueForm(initial=initial_values)
     return render(request,'admin/third.html',{'form':form}) 
   
 

def activitys(request):
    return render(request,'admin/select_activity.html')

def select_activity(request):
    if request.method=='POST':
        category=request.POST['category']
        print(category)
        if category=='event':
            return redirect('add_event')
        elif category=='class':
            return redirect('add_class')
        elif category=='venue':
            return redirect('add_venue')
        else:
         return HttpResponse("<h2>Select an option")
     
    else:
        return render(request,'admin/select_activity.html')
      
 

def one(request):
    return render(request, "one.html")

def search_event(request):
    events=Activity.objects.filter(catagory='Event')
    if request.method == 'POST':
        search_key=request.POST.get('event_search_key')
        event_type=request.POST.get('event_type')
        landmark=request.POST.get('event_landmark')
        start_date=request.POST.get('event_start_date')
        result = []
        print(search_key)
        if search_key:
            result+=Activity.objects.filter(activityname__icontains=search_key)
            print(result)
        if landmark:
            result+=Activity.objects.filter(landmark__icontains=landmark)
        print(landmark)
        
        if start_date:
            result+=Activity.objects.filter(start_date=start_date)
        # if event_type:
        #     result+=Activity.objects.filter()
        return render(request,'search_event.html',{'events':result})
    return render(request,'search_event.html',{'events':events})
        
def search_venue(request):
    
    venues=Activity.objects.filter(catagory='Venue')
    if request.method=='POST':
        search_key=request.POST.get('venue_search_key')
        venue_type=request.POST.get('venue_type')
        landmark=request.POST.get('venue_landmark')
        result=[]
        if search_key:
            result+=Activity.objects.filter(activityname__icontains=search_key)
        if landmark:
            result+=Activity.objects.filter(landmark__icontains=landmark)
    # print(venues)
        return render(request,'search_venue.html',{'venues':result})
    
    return render(request,'search_venue.html',{'venues':venues})

def search_class(request):
    classes=Activity.objects.filter(catagory='Class')
    if request.method == 'POST':
        search_key=request.POST.get('class_search_key')
        class_type=request.POST.get('class_type')
        landmark=request.POST.get('class_landmark')
        start_date=request.POST.get('class_start_date')
        end_date=request.POST.get('class_end_date')
        result=[]
        if search_key:
            result+=Activity.objects.filter(activityname__icontains=search_key)
        if landmark:
            result+=Activity.objects.filter(landmark__icontains=landmark)
        if start_date:
            result+=Activity.objects.filter(start_date=start_date)
        if end_date:
            result+=Activity.objects.filter(end_date=end_date)
    # print(venues)
        return render(request,'search_class.html',{'classes':result})
            
        
    return render(request,'search_class.html',{'classes':classes})

def search_all(request):
    all=Activity.objects.all()
    if request.method == 'POST':
        all_search_key=request.POST.get('all_search_key')
        all_start_date=request.POST.get('all_start_date')
        all_start_time=request.POST.get('all_start_time')
        result = []
        if all_search_key:
            result+=Activity.objects.filter(activityname__icontains= all_search_key)|Activity.objects.filter(select_sports__icontains=all_search_key)|Activity.objects.filter(select_sports__icontains=all_search_key)
        if all_start_date:
            result+=Activity.objects.filter(start_date=all_start_date)
        
        if all_start_time:
            result+=Activity.objects.filter(start_time=all_start_time)
        
        print(result)
        return render(request,'search_all.html',{"all":result})
    return render(request,'search_all.html',{"all":all})

# def search_view(request):
#     if request.method == 'POST':
#         all_search_key=request.POST.get('all_search_key')
#         all_things_to_do=request.POST.getlist('all_things_to_do')
#         all_start_date=request.POST.get('all_start_date')
#         all_start_time=request.POST.get('all_start_time')
#         all_gender_male=request.POST.get('all_gender_male')
#         all_gender_female=request.POST.get('all_gender_female')
#         landmarks=request.POST.get('landmarks')
#         result=Activity.objects.filter(activityname__icontains= all_search_key)|Activity.objects.filter(sports_type__icontains=all_search_key)|Activity.objects.filter(select_sports__icontains=all_search_key)|Activity.objects(stundent_leval_type__icontains=all_search_key)|Activity.objects.filter(start_date=all_start_date)|Activity.objects.filter(start_time=all_start_time)|Activity.objects.filter(landmark=landmarks)
        
#         print(result)
        
#         return render(request,'search_all.html',{"result":result})
 
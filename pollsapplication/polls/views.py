from django.shortcuts import render,redirect ,HttpResponse,get_object_or_404
from django.contrib.auth.models import User 
from django.contrib.auth  import authenticate,  login, logout
from django.contrib import messages

from polls.models import Pollsquestions, voter 
# Create your views here.
def index(request):
    if  request.user.is_authenticated:
        polls = Pollsquestions.objects.all()
        context = {
        'polls' : polls
     }
        return render(request,'index.html',context)
    else:
        return render(request,'login_register.html')
def mypolls(request):
    if  request.user.is_authenticated:
        polls = Pollsquestions.objects.filter(created_by=request.user)
        print(polls)
        context = {
        'polls' : polls
     }
        return render(request,'mypolls.html',context)
    else:
        return render(request,'login_register.html')


#profile
def profile(request):
    if  request.user.is_authenticated:
        details = User.objects.filter(id=request.user.id)
        print(details)
        context = {
        'details' : details
     }
        return render(request,'profile.html',context)
    else:
        return render(request,'login_register.html')

#signup
def handleSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)>10:
            messages.error(request, " Your user name must be under 10 characters")
            return redirect('index')

        if not username.isalnum():
            messages.error(request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1!= pass2):
             messages.error(request, " Passwords do not match")
             return redirect('index')
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request, " Your Wecode_polls id has been successfully created")
        return redirect('index')

    else:
        return HttpResponse("404 - Not found")

#login
def handeLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user) #session start
            messages.success(request, "Successfully Logged In")
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")
   




#logout
def handelLogout(request):
    logout(request)  #session end
    messages.success(request, "Successfully logged out")
    return redirect('index')


"""
def createpoll(request):
    if request.user.is_authenticated:

        return render (request,'createpoll.html')
    else:
        return render(request,'login_register.html')"""


def createpoll(request):
    if request.user.is_authenticated:
        current_user =request.user
        post=Pollsquestions.get_polls_by_user(current_user)
        post_count =post.count()
        print(post_count)
        if  request.method=="POST":
            category=request.POST['cate']
            question=request.POST['quest']
            option1 =request.POST['opt1']
            option2 =request.POST['opt2']
            option3 =request.POST['opt3']
            option4 =request.POST['opt4']


            data = Pollsquestions(created_by=current_user,category=category,question=question,option_1=option1,option_2=option2,option_3=option3,option_4=option4)
            data.save()
            if data is not None:
                messages.success(request, "Successfully Logged In")
                return redirect('createpoll')
        else:
            return render (request,'createpoll.html')

    else:
        return render(request,'login_register.html')


def vote(request, poll_id):
    current_user=request.user
    matches=voter.objects.filter(poll_question=poll_id, Voter_name=current_user)
    print(matches)
   
    poll = Pollsquestions.objects.get(pk=poll_id)
    
    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.count_opt_1 += 1
        elif selected_option == 'option2':
            poll.count_opt_2 += 1
        elif selected_option == 'option3':
            poll.count_opt_3 += 1
        elif selected_option == 'option4':
            poll.count_opt_4 += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()
        poll_id = get_object_or_404(Pollsquestions, pk=poll_id) #create instance of pollsquestions
        voters=voter(poll_question=poll_id,Voter_name=current_user)
        voters.save()
        return redirect('results', poll.id)
        
    
   
    context = {
                'poll' : poll
            }
    return render(request, 'vote.html', context)
    
# shows result
def results(request, poll_id):
    poll = Pollsquestions.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'result.html', context)
from django.shortcuts import render, redirect
from . models import Apply, State, Team, Participants, OwnState, OwnTeam, OwnParticipants
from . filters import StateFilter
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
import os
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
import random
from django.db import IntegrityError



@csrf_exempt
def download(request):
    file_path = 'static/img/blob.svg'
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="image/svg+xml")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


# Create your views here.

def state(request):
    a = State.objects.all()

    myFilter = StateFilter(request.GET, queryset=a)
    a = myFilter.qs
    return render(request,'ps/state.html', {'a':a,'myFilter':myFilter})

def reset(request):

    if request.method == 'GET':
        a = State.objects.all()
    return render(request,'ps/state.html', {'a':a})

def StateDetail(request, pk):
    a = State.objects.get(id=pk)
    contact = a.contact
    ps = a.problem
    des = a.description
    dom = a.domain
    hard = a.hardness
    cp = a.contact_person

    leaders = Team.objects.all()

    

    if request.method == 'POST':
        team_name = request.POST['team_name']
        team_leader_name = request.POST['team_leader_name']
        team_leader_email = request.POST['team_leader_email']
        team_leader_contact = request.POST['team_leader_contact']
        team_leader_regno = request.POST['team_leader_regno']

        if len(team_leader_contact) != 10:
            messages.warning(request, 'Please enter a valid contact number')
            return redirect('state_detail', pk=pk)

        # check for special characters in team_name, team_leader_name,team_leader_contact,team_leader_regno

        for i in team_leader_name:
            if i.isalpha() or i == ' ':
                continue
            else:
                messages.warning(request, 'Please enter a valid team leader name')
                return redirect('state_detail', pk=pk)

        for i in team_leader_contact:
            if i.isdigit():
                continue
            else:
                messages.warning(request, 'Please enter a valid contact number')
                return redirect('state_detail', pk=pk)

        for i in team_leader_regno:
            if i.isdigit() or i.isalpha():
                continue
            else:
                messages.warning(request, 'Please enter a valid registration number')
                return redirect('state_detail', pk=pk)

        for leader in leaders:

            if team_name in leader.team_name:
                messages.warning(request, 'This team name is already registered')
                return redirect('state_detail', pk=pk)

            if team_leader_regno in leader.leader_rollno:
                messages.warning(request, 'This roll number is already registered as a team leader')
                return redirect('state_detail' , pk=pk)
            
            if team_leader_email in leader.leader_email:
                messages.warning(request, 'This email is already registered as a team leader')
                return redirect('state_detail', pk=pk)
            
            if team_leader_contact in leader.leader_contact:
                messages.warning(request, 'This contact number is already registered as a team leader')
                return redirect('state_detail', pk=pk)

            if len(team_name) < 5:
                messages.warning(request, 'Team name should be atleast 5 characters')
                return redirect('state_detail', pk=pk)

        application = Team(team_name=team_name, leader_name=team_leader_name, leader_email=team_leader_email, leader_contact=team_leader_contact, leader_rollno=team_leader_regno, ps=a)

        if application is not None:
            application.save()
            messages.success(request, 'Your team has been registered successfully')
            maily = EmailMessage(
                'Ideathon Registration Successful',
                """
Dear"""+application.leader_name+""",

Thank you for registering for the Ideathon. We are glad to have you as a participant in this exciting event.

We wanted to remind you that the Ideathon is fast approaching, and we hope you are getting excited about it! As a registered participant, you will be receiving important updates and information via email leading up to the event.

We encourage you to keep a close eye on your inbox, as we will be sending updates on important dates, guidelines etc. to help you prepare for the competition.

If you have any questions or concerns in the meantime, please don't hesitate to reach out to us. We are here to support you and ensure that you have the best possible experience at the Ideathon.

Thank you for your participation and we look forward to seeing you soon.

Best regards,
Ré

Kindly join this link and add your team mates to your team
https://researchcell.up.railway.app/ps/team/"""+application.hashid,
                'godsgrace2608@gmail.com',
                [team_leader_email],)
            
            with open('static/pptx/sample.pptx', 'rb') as f:
                maily.attach('sample.pptx', f.read(), 'application/vnd.openxmlformats-officedocument.presentationml.presentation')
            
            maily.send()

            

       
            team_id = Team.objects.get(team_name=team_name)
            # this_id = team_id.id
        
            
            return HttpResponseRedirect(reverse('teamtest', args=[application.hashid]))

    return render(request,'ps/state_detail.html', {'a':a, 'contact':contact, 'ps':ps, 'des':des, 'dom':dom, 'hard':hard, 'cp':cp})

def suc(request):
    return render(request, 'ps/suc.html')


def usermodtest(request):
    leaders = Team.objects.all()

    for leader in leaders:
        #print("k")
        pass

    if request.method == 'POST':
        team_name = request.POST['team_name']
        team_leader_name = request.POST['team_leader_name']
        team_leader_email = request.POST['team_leader_email']
        team_leader_contact = request.POST['team_leader_contact']
        team_leader_regno = request.POST['team_leader_regno']

        if team_name in leader.team_name:
            messages.warning(request, 'This team name is already registered')
            return redirect('usermodtest')

        if team_leader_regno in leader.leader_rollno:
            messages.warning(request, 'This roll number is already registered as a team leader')
            return redirect('usermodtest')
        
        if team_leader_email in leader.leader_email:
            messages.warning(request, 'This email is already registered as a team leader')
            return redirect('usermodtest')
        
        if team_leader_contact in leader.leader_contact:
            messages.warning(request, 'This contact number is already registered as a team leader')
            return redirect('usermodtest')

        if len(team_name) < 5:
            messages.warning(request, 'Team name should be atleast 5 characters')
            return redirect('usermodtest')

        application = Team(team_name=team_name, leader_name=team_leader_name, leader_email=team_leader_email, leader_contact=team_leader_contact, leader_rollno=team_leader_regno)

        if application is not None:
            application.save()
            messages.success(request, 'Your team has been registered successfully')
            send_mail(
                'Ideathon Registration Successful',
                """Your team has been registered successfully for the Ideathon please proceed and your teammates and download the model ppt
                Thank you for Shit""",
                'godsgrace2608@gmail.com',
                [team_leader_email],)
       
            team_id = Team.objects.get(team_name=team_name)
            this_id = team_id.id
        
            
            return redirect('teamtest', this_id=this_id)

    return render(request, 'ps/usermodtest.html')

def teamtest(request, hashid):
    team = Team.objects.get(hashid=hashid)
    team_name = team.team_name
    leader_name = team.leader_name
    leader_email = team.leader_email
    leader_contact = team.leader_contact
    leader_rollno = team.leader_rollno
    problem = team.ps
    this_id = team.pk
    members = Participants.objects.filter(team = team)
    checker = Participants.objects.all()


    if request.method == 'POST':
        member_name = request.POST['member_name']
        member_email = request.POST['member_email']
        member_contact = request.POST['member_contact']
        member_rollno = request.POST['member_rollno']

        # check for special characters in member_name , member_contact , member_rollno
        for i in member_name:
            if i.isalpha() or i == ' ':
                continue
            else:
                messages.warning(request, 'Please enter a valid team leader name')
                return redirect('teamtest', hashid=hashid)

        if not member_rollno.isalnum():
            messages.warning(request, 'Roll number should contain only numbers')
            return redirect('teamtest', hashid=hashid)

        if not member_contact.isdigit():
            messages.warning(request, 'Contact number should contain only numbers')
            return redirect('teamtest', hashid=hashid)

        if len(member_name) < 3:
            messages.warning(request, 'Name should be atleast 3 characters')
            return redirect('teamtest', hashid=hashid)

        if len(member_rollno) != 9:
            messages.warning(request, 'Roll number should be 9 digits')
            return redirect('teamtest', hashid=hashid)

        if len(member_contact) != 10:
            messages.warning(request, 'Contact number should be 10 digits')
            return redirect('teamtest', hashid=hashid)

        if len(member_email) < 5:
            messages.warning(request, 'Email should be atleast 5 characters')
            return redirect('teamtest', hashid=hashid)

        if '@' not in member_email:
            messages.warning(request, 'Email should contain @')
            return redirect('teamtest', hashid=hashid)

        if '.' not in member_email:
            messages.warning(request, 'Email should contain .')
            return redirect('teamtest', hashid=hashid)

        if Participants.objects.filter(team_id=this_id).count() >= 4:
            messages.warning(request, 'You have reached the maximum number of team members')
            return redirect('teamtest', hashid=hashid)

        for checky in checker:

            if member_contact in checky.contact:
                messages.warning(request, 'This contact number is already registered as a team member')
                return redirect('teamtest', hashid=hashid)
            
            if Participants.objects.filter(team_id=this_id).count() >= 4:
                messages.warning(request, 'You have reached the maximum number of team members')
                return redirect('teamtest', hashid=hashid)

            if member_rollno in checky.rollno:
                messages.warning(request, 'This roll number is already registered as a team member')
                return redirect('teamtest', hashid=hashid)
            
            if member_email in checky.email:
                messages.warning(request, 'This email is already registered as a team member')
                return redirect('teamtest', hashid=hashid)
            

            
        add_member = Participants(team_id=this_id, name=member_name, email=member_email, contact=member_contact, rollno=member_rollno)

        if add_member is not None :
            try:
                add_member.save()
                messages.success(request, 'Your team member has been added successfully')
                return redirect('teamtest', hashid=hashid)

            except IntegrityError as e:
                #print(e)
                messages.warning(request, 'The details you entered are already registered')
                return redirect('teamtest', hashid=hashid)

            



    

    
    return render(request, 'ps/teamtest.html', {
        'team_name':team_name,
        'leader_name':leader_name, 
        'leader_email':leader_email, 
        'leader_contact':leader_contact, 
        'leader_rollno':leader_rollno, 
        'this_id':this_id,
        'problem':problem,
        'members':members,})



def ideasum(request):
    if request.method == 'POST':
        problem = request.POST['problem']
        domain = request.POST['domain']
        description = request.POST['description']

        if len(problem) < 8:
            messages.warning(request, 'Problem statement should be atleast 8 characters')
            return redirect('sum')
        
        if len(description) < 50:
            messages.warning(request, 'Description should be atleast 50 characters')
            return redirect('sum')
        
        sub = OwnState(problem=problem, domain=domain, description=description)
        
        if sub is not None:
            sub.save()
            a = sub.id
            #print(a)
            messages.success(request, 'Your idea has been submitted successfully')
            return redirect('ireg', a=a)


    return render(request, 'ps/sum.html')


def ideateamreg(request, a):

    ps = OwnState.objects.get(id=a)
    team = OwnTeam.objects.all()


    if request.method == 'POST':
        team_name = request.POST['team_name']
        leader_name = request.POST['team_leader_name']
        leader_email = request.POST['team_leader_email']
        leader_contact = request.POST['team_leader_contact']
        leader_rollno = request.POST['team_leader_regno']

        # check for special characters in leader_name , leader_contact , leader_rollno

        for i in leader_name:
            if i.isalpha() or i == ' ':
                continue
            else:
                messages.warning(request, 'Please enter a valid team leader name')
                return redirect('ireg', a=a)
        
        if not leader_rollno.isalnum():
            messages.warning(request, 'Roll number should contain only numbers')
            return redirect('ireg', a=a)
        
        if not leader_contact.isdigit():
            messages.warning(request, 'Contact number should contain only numbers')
            return redirect('ireg', a=a)

        if len(leader_name) < 3:
            messages.warning(request, 'Name should be atleast 3 characters')
            return redirect('ireg', a=a)

        if not '@' in leader_email:
            messages.warning(request, 'Email should contain @')
            return redirect('ireg', a=a)
        
        if not '.' in leader_email:
            messages.warning(request, 'Email should contain .')
            return redirect('ireg', a=a)


        for check in team:
            if team_name in check.team_name:
                messages.warning(request, 'This team name is already registered')
                return redirect('ireg', a=a)

            if leader_contact in check.leader_contact:
                messages.warning(request, 'This contact number is already registered as a team leader')
                return redirect('ireg', a=a)
            
            if leader_rollno in check.leader_rollno:
                messages.warning(request, 'This roll number is already registered as a team leader')
                return redirect('ireg', a=a)
            
            if leader_email in check.leader_email:
                messages.warning(request, 'This email is already registered as a team leader')
                return redirect('ireg', a=a)
            

        cusreg = OwnTeam(team_name=team_name, leader_name=leader_name, leader_email=leader_email, leader_contact=leader_contact, leader_rollno=leader_rollno, ps=ps)

        if cusreg is not None:
            cusreg.save()
            tid = cusreg.hashid
            messages.success(request, 'Your team has been registered successfully')
            maily = EmailMessage(
                'Ideathon Registration Successful',
                """
Dear """+cusreg.leader_name+""",

Thank you for registering for the Ideathon. We are glad to have you as a participant in this exciting event.

We wanted to remind you that the Ideathon is fast approaching, and we hope you are getting excited about it! As a registered participant, you will be receiving important updates and information via email leading up to the event.

We encourage you to keep a close eye on your inbox, as we will be sending updates on important dates, guidelines etc. to help you prepare for the competition.

If you have any questions or concerns in the meantime, please don't hesitate to reach out to us. We are here to support you and ensure that you have the best possible experience at the Ideathon.

Thank you for your participation and we look forward to seeing you soon.

Best regards,
Ré

Kindly join this link and add your team mates to your team
https://researchcell.up.railway.app/ps/team/"""+cusreg.hashid,
                'godsgrace2608@gmail.com',
                [leader_email],)
            
            with open('static/pptx/sample.pptx', 'rb') as f:
                maily.attach('sample.pptx', f.read(), 'application/vnd.openxmlformats-officedocument.presentationml.presentation')
            
            maily.send()
            return redirect('ideateam', tid=tid)



    return render(request, 'ps/ideateamreg.html' , {'ps':ps})


def ideateam(request, tid):

    t = OwnTeam.objects.get(hashid=tid)
    members = OwnParticipants.objects.filter(team = t)
    participants = OwnParticipants.objects.all()

    if request.method == 'POST':
        member_name = request.POST['member_name']
        member_email = request.POST['member_email']
        member_contact = request.POST['member_contact']
        member_rollno = request.POST['member_rollno']

        # check for special characters in member_name , member_contact , member_rollno

        for i in member_name:
            if i.isalpha() or i == ' ':
                continue
            else:
                messages.warning(request, 'Please enter a valid team member name')
                return redirect('ideateam', tid=tid)
        
        if not member_rollno.isalnum():
            messages.warning(request, 'Roll number should contain only numbers')
            return redirect('ideateam', tid=tid)
        
        if not member_contact.isdigit():
            messages.warning(request, 'Contact number should contain only numbers')
            return redirect('ideateam', tid=tid)

        if len(member_name) < 3:
            messages.warning(request, 'Name should be atleast 3 characters')
            return redirect('ideateam', tid=tid)

        if not '@' in member_email:
            messages.warning(request, 'Email should contain @')
            return redirect('ideateam', tid=tid)
        
        if not '.' in member_email:
            messages.warning(request, 'Email should contain .')
            return redirect('ideateam', tid=tid)
        
        if len(member_contact) != 10:
            messages.warning(request, 'Please enter a valid contact number')
            return redirect('ideateam', tid=tid)

        if OwnParticipants.objects.filter(team=t).count() >= 4:
            messages.warning(request, 'You can only add upto 4 members')
            return redirect('ideateam', tid=tid)
        
        for check in participants:
            if member_contact in check.contact:
                messages.warning(request, 'This contact number is already registered as a team member')
                return redirect('ideateam', tid=tid)
            
            if member_rollno in check.rollno:
                messages.warning(request, 'This roll number is already registered as a team member')
                return redirect('ideateam', tid=tid)
            
            if member_email in check.email:
                messages.warning(request, 'This email is already registered as a team member')
                return redirect('ideateam', tid=tid)

        add_member = OwnParticipants(team=t, name=member_name, email=member_email, contact=member_contact, rollno=member_rollno)

        if add_member is not None:
            add_member.save()
            messages.success(request, 'Your team member has been added successfully')
            return redirect('ideateam', tid=tid )


    return render(request, 'ps/ideateam.html', {'t':t, 'members':members})



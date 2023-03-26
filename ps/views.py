from django.shortcuts import render, redirect
from . models import Apply, State, Team, Participants
from . filters import StateFilter
from django.contrib import messages
from django.core.mail import send_mail

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

    for leader in leaders:
        print("k")

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

        application = Team(team_name=team_name, leader_name=team_leader_name, leader_email=team_leader_email, leader_contact=team_leader_contact, leader_rollno=team_leader_regno, ps=a)

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

    return render(request,'ps/state_detail.html', {'a':a, 'contact':contact, 'ps':ps, 'des':des, 'dom':dom, 'hard':hard, 'cp':cp})

def suc(request):
    return render(request, 'ps/suc.html')

def ideasum(request):
    return render(request, 'ps/sum.html')

def usermodtest(request):
    leaders = Team.objects.all()

    for leader in leaders:
        print("k")

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

def teamtest(request, this_id):
    team = Team.objects.get(id=this_id)
    team_name = team.team_name
    leader_name = team.leader_name
    leader_email = team.leader_email
    leader_contact = team.leader_contact
    leader_rollno = team.leader_rollno
    problem = team.ps
    members = Participants.objects.filter(team_id=this_id)
    checker = Participants.objects.all()



    if request.method == 'POST':
        member_name = request.POST['member_name']
        member_email = request.POST['member_email']
        member_contact = request.POST['member_contact']
        member_rollno = request.POST['member_rollno']

        for check in checker:
            pass
        
        if Participants.objects.filter(team_id=this_id).count() >= 4:
            messages.warning(request, 'You have reached the maximum number of team members')
            return redirect('teamtest', this_id=this_id)

        if member_rollno in check.rollno:
            messages.warning(request, 'This roll number is already registered as a team member')
            return redirect('teamtest', this_id=this_id)
        
        if member_email in check.email:
            messages.warning(request, 'This email is already registered as a team member')
            return redirect('teamtest', this_id=this_id)
        
        if member_contact in check.contact:
            messages.warning(request, 'This contact number is already registered as a team member')
            return redirect('teamtest', this_id=this_id)
        
        add_member = Participants(team_id=this_id, name=member_name, email=member_email, contact=member_contact, rollno=member_rollno)

        if add_member is not None:
            add_member.save()
            messages.success(request, 'Your team member has been added successfully')



    

    
    return render(request, 'ps/teamtest.html', {
        'team_name':team_name,
        'leader_name':leader_name, 
        'leader_email':leader_email, 
        'leader_contact':leader_contact, 
        'leader_rollno':leader_rollno, 
        'this_id':this_id,
        'problem':problem,
        'members':members,})



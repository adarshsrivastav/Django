from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponse
from forms import MyRegistrationForm



def login(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/repeat_login')
	else:
		c={}
		c.update(csrf(request))
		return render_to_response('login.html',c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username,password=password)

	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/repeat_login')	
	else:
		if user is not None:
			if user.is_active:
				auth.login(request,user)
				return HttpResponseRedirect('/accounts/loggedin')
			else:
				print("The password is valid, but the account has been disabled!")			
		else:
			return HttpResponseRedirect('/accounts/invalid')
			

def loggedin(request):
	return render_to_response('loggedin.html', {'full_name':request.user.username})
	

def invalid_login(request):
	return render_to_response('invalid_login.html')

def logout(request):
	if request.user.is_authenticated():
		auth.logout(request)
		return render_to_response('logout.html')
	else:
		return HttpResponseRedirect('/accounts/repeat_logout')


def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))
 
	args['form'] = MyRegistrationForm()

	return render_to_response('register.html',args)

def register_success(request):
	return render_to_response('register_success.html')

def contactus(request):
	return render_to_response('contactus.html')

def repeat_login(request):
	return render_to_response('repeat_login.html')

def repeat_logout(request):
	return render_to_response('repeat_logout.html')
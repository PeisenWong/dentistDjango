from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def contact_view(request):
	if request.method == 'POST':
		message_name = request.POST.get('contact-name')
		message_email = request.POST.get('contact-email')
		message_subject = request.POST.get('contact-subject')
		message = request.POST.get('contact-message')

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['wongpeisen@gmail.com'], # to email
			fail_silently = False
			)

		return render(request, 'contact.html', {'message_name':message_name})

	else:
		return render(request, 'contact.html', {})

def home_view(request):
	return render(request, 'home.html',{})

def about_view(request):
	return render(request, 'about.html',{})

def services_view(request):
	return render(request, 'services.html',{})


def appointment_view(request):
	if request.method == 'POST':
		message_name = request.POST.get('appointment-name')
		message_email = request.POST.get('appointment-email')
		message_phone = request.POST.get('appointment-phone')
		message_date = request.POST.get('appointment-date')
		message_department = request.POST.get('appointment-department')
		message_doctor = request.POST.get('appointment-doctor')
		message = request.POST.get('appointment-message')

		mail_subject = 'Appointment request from ' + message_name
		mail_message = 'Name: '+ message_name +'\n' + 'Phone: '  + message_phone +'\n'+'Email: '+ message_email +'\n' + 'Request date: '+ message_date +'\n' + 'Department: '+ message_department +'\n' + 'Doctor: '+ message_doctor + '\n' + 'Message: '+ message

		# send an email
		send_mail(
			mail_subject, # subject
			mail_message, # message
			message_email, # from email
			['wongpeisen@gmail.com'], # to email
			fail_silently = False
			)

		return render(request, 'appointment.html', {'message_name':message_name})

	else:
		return render(request, 'home.html', {})





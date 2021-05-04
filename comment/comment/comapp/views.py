from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
'''def home(request):
    obj = comment.objects.all()
    seen = comment.objects.create()
    seen.save()
    context = {
         'obj':obj,
        #'seen':seen
    }
    return render(request,'comment.html',context)'''

def home(request):
	if request.method == 'POST':
		#msg = send_sms()
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save() # saves in database
			#messages.success(request, f"Your message has been sent.Thanks for visiting our site!")
	else:
		form = CommentForm()
	return render(request,'comment.html',{'form': form})

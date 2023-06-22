from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import User, Bunk

class IndexView(generic.ListView):
    template_name = 'theapp/index.html'
    context_object_name = 'recent_bunks'

    def get_queryset(self):
        return Bunk.objects.order_by('-time')

def userView(request, idNo):
    my_bunks = Bunk.objects.filter(to_user__id=idNo).order_by('-time')
    template = loader.get_template('theapp/index.html')
    u = User.objects.get(pk=idNo)
    context = {
        'username': u.username,
        'prof_img': 'theapp/images/' + u.photo,
        'recent_bunks': my_bunks,
    }
    return HttpResponse(template.render(context, request))

def bunk(request): 
    #template = loader.get_template('theapp/bunk.html')
    users = User
    return render(request, 'theapp/bunk.html', {
        'users': User.objects.order_by('username')
    })

def submit_bunk(request):
    try:
        t_user = User.objects.get(pk=request.POST['to'])
        f_user = User.objects.get(pk=request.POST['from'])
    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'theapp/bunk.html', {
            'users': User.objects.order_by('username'),
            'error_message': "Bunking Error.",
        })
    else:
        if (request.POST['to'] == request.POST['from']):
            return render(request, 'theapp/bunk.html', {
                'users': User.objects.order_by('username'),
                'error_message': "You can't bunk yourself.",
            })
        b = Bunk(from_user=f_user, to_user=t_user, time=timezone.now())
        b.save()
        return HttpResponseRedirect(reverse('theapp:index'))

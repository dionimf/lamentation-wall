from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import login, logout as auth_logout

from index_board.forms import LamentationForm, CounselForm, VisitModel, PostRateModel
from index_board.models import *

from django.shortcuts import render_to_response
from django.template.context import RequestContext

import json
from mylib.general import get_client_ip
from django.utils import timezone
from datetime import datetime
import pytz
import time

def index(request):

    form = LamentationForm(prefix='lamentation')

    visit = VisitModel()
    visit.ip = get_client_ip(request)
    visit.date = timezone.now()
    visit.request_method = request.method
    visit.save()

    if request.method == 'POST':
        
        form = LamentationForm(request.POST, prefix='lamentation')

        if form.is_valid():
            #if not PostRateModel.is_too_much(visit.ip, 'lament'):
            if True:
                lament = form.save(commit=True)

                post = PostRateModel()
                post.ip = visit.ip
                post.date = visit.date
                post.type = 'lament'
                post.save()

                return redirect("/lamentacoes")
            else:
                return redirect("/?limit=1")

        else:
            print(form.errors)

    lamentations = LamentModel.objects.order_by('-id')[:50]

    for l in lamentations:
        l.calculate_user_cry(request.user)
    
    return render(request, 'me/index.djhtml',
                  {'user': request.user,
                   'form': form,
                   'counsel_form': CounselForm(prefix='counsel'),
                   'lamentations': lamentations})

def redirect_to_laments(request):
    return redirect("/lamentacoes")

def cry_together(request):
    if request.user.is_anonymous():
        return HttpResponse(-1)
    try:
        lament = LamentModel.objects.get(id=request.GET.get('id'))
    except:
        lament = None

    if lament:
        count = lament.cry(request.user)
        return HttpResponse(count)

def uncry(request):
    if request.user.is_anonymous():
        return HttpResponse(-1)

    try:
        lament = LamentModel.objects.get(id=request.GET.get('id'))
    except:
        lament = None

    if lament:
        count = lament.uncry(request.user)
        return HttpResponse(count)

def save_counsel(request):
    print('save_counsel')
    if request.method == 'POST':
        form = CounselForm(request.POST, prefix='counsel')

        if form.is_valid():
            counsel = form.save(commit=False)
            counsel.date = timezone.now()
            counsel.save()
            id = request.POST.get('counsel-lament_id')

            # count how many counsels
            count = LamentModel.objects.get(id=request.POST.get('counsel-lament_id')).count_counsels()

            # return the count for ajax
            response_data = {'count': count, 'lament_id': id}
            return HttpResponse(json.dumps(response_data))

    return HttpResponse(-1)

def list_counsels(request):
    if request.method == 'GET':
        lament_id = request.GET.get('lament')

        counsels = CounselModel.objects.filter(lament_id=lament_id)

        return render(request, 'me/list-counsels.djhtml',
                      { 'counsels': counsels })


def test(request):
    return render(request, 'me/test.djhtml')

def google_login(request):
    context = RequestContext(request,
                             {'user': request.user})
    return render_to_response('me/google-login.djhtml',
                              context_instance=context)

def twitter_auth_complete(request):
    print('auth:')
    print(request.user.is_authenticated())
    context = RequestContext(request, {'request': request,
                                       'user': request.user })
    user = request.user

    login(request, user)


def google_auth_complete(request):
    print('auth:')
    return HttpResponse(1)
    print(request.user.is_authenticated())
    context = RequestContext(request, {'request': request,
                                       'user': request.user })
    user = request.user

    login(request, user)

    # return render_to_response('me/index.djhtml', context_instance=context )

def auth_complete(request):
    return HttpResponse(request.user)

def login(request):
    return HttpResponse(request.user)
    
def logout(request):
    auth_logout(request)
    return redirect('/')

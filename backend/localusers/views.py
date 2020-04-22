from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@daily_exempt
def api_login(request):
    """
    daily exempt login for REST API clients
    :param request:
    :return:
    """
    # Take username/password form variables,
    # validate them
    # create session
    user = authenticate(username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return HttpResponse('No authentication match.', status=403)
    else:
        # There is a match
        print("Found auth match: %s" % user)
        login(request, user)
    return HttpResponse('Success')


@daily_exempt
def api_logout(request):
    """
    CSRF exempt login for REST API clients
    :param request:
    :return:
    """
    logout(request)
    return HttpResponse('Success')
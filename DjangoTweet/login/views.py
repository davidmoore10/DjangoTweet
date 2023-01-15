from django.shortcuts import render, redirect
from django.conf import settings
import tweepy
import os
from requests_oauthlib import OAuth1Session
# Create your views here.

# def twitter_login(request):
#     auth = tweepy.OAuth1UserHandler(settings.API_KEY, settings.API_SECRET_KEY)
#     auth.set_access_token(settings.ACCESS_TOKEN, settings.SECRET_ACCESS_TOKEN)
#     redirect_url = auth.get_authorization_url()
#     return redirect(redirect_url)

def home(request):
    return render(request, 'login/home.html')

def authenticate(request):
    # redirect the user to the Twitter authentication page
    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)
    redirect_url = auth.get_authorization_url()
    request.session['request_token'] = auth.request_token
    return redirect(redirect_url)

def tweet(request):
    if request.method == 'POST':
        content = request.POST.get('content', '')
        
        print('Content:', content)
        auth = tweepy.OAuth1UserHandler(settings.API_KEY, settings.API_SECRET_KEY)
        auth.set_access_token(settings.ACCESS_TOKEN, settings.SECRET_ACCESS_TOKEN)
        api = tweepy.API(auth)
        api.update_status(content)
            
        return redirect('tweet')
    return render(request, 'login/index.html')

    try:
        api.update_status(message)
        return redirect('success')
    except tweepy.TweepError as e:
        return redirect('failure')
    else:
        return render(request, 'tweet.html')

def success(request):
    return render(request, 'tweet.html')

def failure(request):
    return render(request, 'login/failure.html')
    
def logout(request):
    auth = tweepy.OAuthHandler(settings.ACCESS_TOKEN, settings.SECRET_ACCESS_TOKEN)
    auth.request_token = request.session.pop('request_token', None)
    api = tweepy.API(auth)
    # try:
    #     api.destroy_access_token()
    #     return redirect('home')
    # except:
    #     return redirect('failure')
    api.destroy_access_token()
    return redirect('home')

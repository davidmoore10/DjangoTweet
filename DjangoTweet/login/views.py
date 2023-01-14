from django.shortcuts import render, redirect
import tweepy
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# Create your views here.

def twitter_login(request):
    auth = tweepy.OAuth1UserHandler('b7yfU62Esaaa8P1aXWXYsYFvd', os.environ['TWITTER_SECRET_KEY'])
    redirect_url = auth.get_authorization_url()
    return redirect(redirect_url)


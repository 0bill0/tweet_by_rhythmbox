#coding:utf8
import tweepy
import shlex, subprocess

#set this from http://dev.twitter.com/apps/myappid 
CONSUMER_KEY = '' #your consumer_key
CONSUMER_SECRET = '' #your consumer_secret
#set this from http://dev.twitter.com/apps/myappid/my_token
ACCESS_TOKEN_KEY= '160253399-h3gTzH1rF3B6WX5eDKHeaFWmNXE62UTANP7uHAej'
ACCESS_TOKEN_SECRET= '7qQJjmYXp6Em9kBG9rDjinHf5EBEgYEJ22hllB3G59U3G'

message = "Estou ouvindo a música " #edit the message before of <name_music> here

def tweet(status):
    if len(status) > 140:
        raise Exception('Status message is too long!')
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    result = api.update_status(status)
    return result

command_line = 'rhythmbox-client --print-playing'
args = shlex.split(command_line)
current_music = subprocess.check_output(args)
opcao = True
while(opcao):
  if(current_music == subprocess.check_output(args)):
    current_music = current_music
  else:
    if(current_music == ' - \n'):
      current_music = subprocess.check_output(args)
    else:
      current_music = subprocess.check_output(args)
      status = message+current_music
      print tweet(status)

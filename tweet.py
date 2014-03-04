#coding:utf8
''''
The MIT License

Copyright (c) 2009 Hugo Lopes Tavares

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
''''
import tweepy
import shlex, subprocess

#set this from http://dev.twitter.com/apps/myappid 
CONSUMER_KEY = '' #your consumer_key
CONSUMER_SECRET = '' #your consumer_secret
#set this from http://dev.twitter.com/apps/myappid/my_token
ACCESS_TOKEN_KEY= '' #your token_key
ACCESS_TOKEN_SECRET= ''#your token_secret

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

''' Quick twitter API test using Twython '''

import twython


# Todo: retain access token in local storage
# Load the app credentials
try:
    from config import config as config
except ModuleNotFoundError:
    raise Exception('Please rename config.py.example to config.py')

if not 'twitter' in config:
    raise Exception('Missing Twitter config')

if not all(k in config['twitter'] for k in ('app_key', 'app_secret')):
    raise Exception('Missing Twitter credentials')

# Authenticate
twitter_auth = twython.Twython(config['twitter']['app_key'], config['twitter']['app_secret'], oauth_version=2)
access_token = twitter_auth.obtain_access_token()

# Initialize API client
twitter = twython.Twython(config['twitter']['app_key'], access_token=access_token)

# Search for tweets matching "make an app that"
search_results = twitter.search(q='"make an app that" exclude:replies exclude:retweets', tweet_mode='extended')

for result in search_results['statuses']:
    print(result['full_text'].replace("\n", " "))

"""

Example output:

Someone should make an app that transcribes Clubhouse rooms but leaves out the life story before a question.
I’m going to make an app that blocks anything that mentions @KimKardashian I do not care she went to dinner.
We believe the same thing, only we make an app that helps you simplify your life. Coming next week! Thanks for your patience! #adelayedappisagoodapp #nextweek #launch #rentado #apartments #easy https://t.co/aL8ihNGuKm
Can someone make an app that lists all the #kdrama’s that have come out. Where you can list if you’ve watched, want to watch, etc. Does this exist? And don’t say Viki.
gonna make an app that recreates the experience of dialing on a rotary phone, excited for my millions https://t.co/xRfFDaUnNg
Someone needs to make an app that’s got a customizable profile like MySpace, pictures like Instagram, and tweets - all in one. Please.
Can someone please make an app that shows me the films available on UK Netflix in order of their IMDB rating?
Somebody should make an app that people can use to decorate their homes, but with real items from furniture stores to see how it would look in real life. I could use that
Gonna make an app that will make you break your heart phones
Someone make an app that takes the restaurants near me and puts them in a randomizer ... and I click a button to decide where to eat
I wish they make an app that let you see all yo bills together. I be on like 5 different apps tryna pay bills.
Someone needs to make an app that tracks your misc activities and matches you up with ppl who do similar things  Like “this person also wandered aimlessly around a Meijer for 45 minutes, you should do it together”
"I want to make an app that sends notifications to people that will just ruin their day and remind them that they suck."  "Why would anyone get that app?"  "It will prey on their skin-deep desire to be cultured."  -The birth of Duolingo
They should make an app that locks me out all of my apps so i can shut up
i wish there was a way to block me from ever seeing nikita dragon on any platform someone make an app that mutes across all websites at once please

"""
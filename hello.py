#https://realpython.com/twitter-bot-python-tweepy/
import tweepy
CONSUMER_KEY=""
CONSUMER_SECRET= ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET= ""
# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Create API object
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    # Create a tweet
    api.update_status("Hello Tweepy")
except:
    print("Error during authentication")


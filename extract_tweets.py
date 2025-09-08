import tweepy
import json

API_KEY = "zseMaAkGa7B0FU3Iyzb5qFjL3"
API_SECRET_KEY = "xD7H43AcECXXk1z83KqYBuHe0thGScYh9gXLCO7bzF2SjU2WbY"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAOnr3wEAAAAAqSChy1ReKxFWOpoPaTydh31u%2F4U%3DeZpTTtt71emHrXT5OY0H9MU4StVnAFyLdVI10JBTNKc4Atqdkm"
ACCESS_TOKEN = "1964000211623444480-rEXIA7qCm8BYT9mro7yoURswz8DETV"
ACCESS_TOKEN_SECRET = "6ZRhqZBP2xlMtTnR9ZKj30hh2TRJJ3uKmXtpw0lxqkMck"

if __name__ == "__main__":
    twitterClient = tweepy.Client(
        bearer_token=BEARER_TOKEN,
        access_token=ACCESS_TOKEN,
        access_token_secret=ACCESS_TOKEN_SECRET,
        consumer_key=API_KEY,
        consumer_secret=API_SECRET_KEY,
        wait_on_rate_limit=True,
    )

    user = twitterClient.get_user(username="xai")
    user_id = user.data.id

    # get tweets
    tweets=twitterClient.get_users_tweets(
        user_id,
        max_results=50,
        tweet_fields=['created_at','public_metrics','text']
    )

   # save the tweets to json file
    with open("extracted_tweets.json" , 'w') as json_file :
         json.dump([tweet.data for tweet in tweets.data], json_file, indent=4)
    

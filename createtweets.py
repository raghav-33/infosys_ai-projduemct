import pandas as pd
import json
from run_prompt import execute_gemini_for_tweet_creation

def top_5_selection(analyzed_tweets,engagement_type):
    df=pd.DataFrame(analyzed_tweets)
    print("DataFrame columns:", df.columns)
    filtered_df=df[df['engagement_type']==engagement_type]
    return filtered_df.nlargest(5,columns=['engagement_score']).values.tolist()

def create_tweets(analyzed_tweets):
    prompt=''' write a tweet for new releasing Ai chatboot with new feature doctor report which will suggest you medicine according to your test report and best yoga practices '''
    engagement_type='like'
    top_5_tweets=top_5_selection(analyzed_tweets,engagement_type)

    system_prompt=f'''
    create a engaging twitter post for any tech company
    PROMPT: {prompt}

    here are some examples tweets and their sentiment analysis with very high 
    user engagement of other similar companies.
    Example Tweets :
    {top_5_tweets}

    create the tweets compare it with the example tweets
    and predict and explain why and how this tweets will perform
    well comparing to the given examples.'''

    output=execute_gemini_for_tweet_creation(system_prompt) # execute_gemini_for_tweet_creation
    dict=json.loads(output)
    twt=dict['tweet']
    twt2=dict['prediction']
    twt3=dict['explanation']
    print(twt,'\n')
    print(twt2,'\n')
    print(twt3,'\n')
    
with open('analyzed_tweets.json') as f:
    data=json.load(f)
    print("tweets loaded ", data)
    create_tweets(data)


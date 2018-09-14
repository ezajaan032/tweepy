#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "2945256679-eFenVqZwsaD4I3oeleZqtLVNZ9uQ0WzS6HAvMU5"
access_token_secret = "l0g9enDkyQLMfhxxxIjYfhhOjrrpXVwlavSRHmnle1TcJ"
consumer_key = "Ggjy35mCCAfTUTwbqqutzj1Dj"
consumer_secret = "ZkzamfEtcNJkisKblipmDBUSjWZN7L290qewZZnyaLMRHQpGK3"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])

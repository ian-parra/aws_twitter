import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

consumer_key = "8I13xu024DbZhk0TD27dqf6mH"
consumer_secret = "gity2Udfb30Pxa4IPAzq8eulUppHf4Zd8niqKhgM2RtnnLRgAi"
access_key = "1666909324617162753-0KSIYpMdSj6fOCoed4D7WmfJanjyIn"
access_secret = "tI3zVWWayv7QP9vmskFId21RgoRcHfxtW6HW11gzUbFqI"

# Twitter conexion y autenticacion
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key,access_secret )

# Creando el objeto de la API
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@_Ghosty_grs',
                           # maximo permitido 200
                           count=200,
                           include_rts=False,
                           # mantener el texto completo
                           tweet_mode='extended'
                           )
print(tweets)

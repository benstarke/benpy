# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
#account_sid = os.environ[]
#auth_token = os.environ[]
client = Client('ACa2a31b0ca89ccf73af8a80b92d8e3085','6ca2e1f9d42e53a26566a89b74cbe1cf')

message = client.messages.create(
                     body="Testing is successfully",
                     from_='+19388882392',
                     to='+2540792047134'
                 )

#print(message.sid)
print("Message sent")
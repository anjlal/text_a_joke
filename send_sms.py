from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC32a3c49700934481addd5ce1659f04d2"
auth_token  = ""
client = TwilioRestClient(account_sid, auth_token)
 
message = client.sms.messages.create(body="Jenny please?! I love you <3",
    to="+14088074454",    # Replace with your phone number
    from_="+14089161903") # Replace with your Twilio number
print message.sid
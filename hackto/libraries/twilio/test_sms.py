from twilio.rest import TwilioRestClient

account = 'AC783dfe8941fc425d9a25428d259080b3'
token = '8a5301aea9dce3732f5ff159b806951f'
client = TwilioRestClient(account, token)
body = "Test Auto shop"
# from sandbox number needs to be what's listed below.
message = client.sms.messages.create(to="+14168756762", from_="+16479311254", body=body)

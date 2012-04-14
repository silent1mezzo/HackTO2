from libraries.twilio.rest import TwilioRestClient
from libraries.yellow import yellowcache

account = 'AC7f1fcd893913af61806ca810d9681190'
token = '9f09dc0d475a931cd8f00b1219f00bf4'
client = TwilioRestClient(account, token)
body = "Test Auto shop"
# from sandbox number needs to be what's listed below.

def send_message(address, category):
    print address, category
    for business in yellowcache.getResults(address)[category]:
        msg = "%s at %s %s, %s %s..." % (business['name'], business['address']['street'], business['address']['city'], business['address']['prov'], business['address']['pcode']) 
        message = client.sms.messages.create(to="+14162949555", from_="+16479311254", body=msg[:160])

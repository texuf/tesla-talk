import os
import random
from twilio.rest import Client
import teslapy

QUOTES = [
	"Writers are desperate people and when they stop being desperate they stop being writers.",
	"We are here to laugh at the odds and live our lives so well that Death will tremble to take us.",
	"Stop insisting on clearing your head-clear your fucking heart instead.",
	"If you have the ability to love, love yourself first.",
	"Poetry is what happens when nothing else can.",
	"Find what you love and let it kill you.",
	"I guess the only time most people think about injustice is when it happens to them.",
	"Censorship is the tool of those who have the need to hide actualities from themselves and from others.",
	"A spark can set a whole forest on fire. Just a spark. Save it.",
	"I wanted the whole world or nothing.",
	"Almost everybody is born a genius and buried an idiot.",
	"Beware of those who seek constant crowds; they are nothing alone.",
	"You begin saving the world by saving one man at a time; all else is grandiose romanticism or politics.",
	"What matters most is how well you walk through the fire.",
	"We're all going to die, all of us, what a circus!",
	"An intellectual says a simple thing in a hard way. An artist says a hard thing in a simple way."
]

## doesn't work...
def revoke_token(token):
    with teslapy.Tesla('austinellis@gmail.com') as tesla:
        print(tesla.api('STATUS'))
        tesla.endpoints["REVOKE_TOKEN_XXX"] =  {
            'TYPE': 'POST',
            'URI': 'oath2/v3/revoke', 
            'AUTH': True
        }
        uri = "https://auth.tesla.com/oauth2/revoke"
        serialize = True
        arg_name = 'json'
        resp = tesla.request('POST', uri, serialize,
                            withhold_token=False,
                            **{arg_name: {'token': token}})
        print(resp)
        

def send_sms(message):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ['TWILIO_FROM']
    to_numbers = os.environ['TWILIO_TO'].split(",")
    client = Client(account_sid, auth_token)
    for number in to_numbers:
        resp = client.messages.create(
            body=message,
            from_=from_number,
            to=number
        )
        print(resp.sid)


def run():
    print("Hello World DEBUG_1:", os.environ.get("DEBUG_1", "Not set"))
    index = random.randint(0, len(QUOTES) - 1)
    quote = QUOTES[index]
    

if __name__ == "__main__":
    run()
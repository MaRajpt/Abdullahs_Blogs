import os
from twilio.rest import Client


# class NotificationManager:
#
#     def __init__(self):
#         self.recovery = "BvsNlAKHFA4d5qWcYLnqim1iRFWcyVCKqwmbZE-e"
#         self.phone_number = +18176461590
#         self.secret = "Eg8OwZAqw2GXUlTaRODOqgFFbEkgFphX"
#         self.sid = 'ACff137fd28518dd483bea732dfc91384e'
#         self.tok = 'c188e3db082bc3ccda0f529e2a44a6db'
#         self.account_sid=os.environ['TWILIO_ACCOUNT_SID'] = self.sid
#         self.auth_token=os.environ['TWILIO_AUTH_TOKEN'] = self.tok
#         self.client = Client(self.account_sid, self.auth_token)
#         self.client = Client(self.account_sid, self.auth_token)
#
#     def notification(self):
#         message1 = self.client.messages.create(
#             body=f"Send from your Twilio account\n{1}\nHeadline: {2}\nBrief: {3}",
#             from_='+18176461590',
#             to='+923044111814'
#         )
#
# nm = NotificationManager()
# nm.notification()

recovery = "BvsNlAKHFA4d5qWcYLnqim1iRFWcyVCKqwmbZE-e"
phone_number = +18176461590
secret = "Eg8OwZAqw2GXUlTaRODOqgFFbEkgFphX"

sid = 'ACff137fd28518dd483bea732dfc91384e'
tok = 'c188e3db082bc3ccda0f529e2a44a6db'


account_sid=os.environ['TWILIO_ACCOUNT_SID'] = sid
auth_token=os.environ['TWILIO_AUTH_TOKEN'] = tok
client = Client(account_sid, auth_token)

message1 = client.messages.create(
    body=f"Send from your Twilio account\n{1}\nHeadline: {2}\nBrief: {3}",
    from_='+18176461590',
    to='+923044111814'
)
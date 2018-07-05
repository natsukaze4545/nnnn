#SRSU LINE BOT TOKEN GENERATOR v7.0.3
import LAG
from LAPI.main import qr
c = LAG.LINE()
c.login(token=qr().get())
print("Auth token : " + c.authToken)
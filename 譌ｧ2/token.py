import LAG
from LAG.lib.Gen.ttypes import *
from LAPI.main import qr
cl = LAG.LINE()
cl.login(token=qr().get())
cl.loginResult()
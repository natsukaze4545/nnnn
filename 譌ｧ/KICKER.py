#SRSU LINE 6KICKER BOT v7.0.3
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
k1 = LAG.LINE()
k1.login(token="Eqggd679ZujCNIp7iSg7.hLkxQqwlVRIMzWaUqoo+DW.TzLXWd9blXJcnyUpX3Ni19i0r9bFJHU8nXWTtcG5Jck=")
k2 = LAG.LINE() 
k2.login(token="EqOvUY8yucBTeIp1h7y1.DPLuBYhMBUKAgmgenIJWGq.PJUujF0Yj44ySA0g2zHMtNarlcAECLjvL4gH1dhvSGU=")
k3 = LAG.LINE()
k3.login(token="Eq0xkbFlQkZuAuJZ9j70.3So3iW8wB5sEssSoxCD4ea.MRWAvyDMfS7ZWlOAMr9je7YP48464T4J80Xc/OOwWLg=")
k4 = LAG.LINE()
k4.login(token="EqB5m6Odc8V3p7szrTEa.nktOVlxstjXQ7JL0HvpVMG.OPNF8duCx5H7O3wsCXyXkd6Z884pWNkYxsQk+D2H9l4=")
k5 = LAG.LINE() 
k5.login(token="EqDwou25inP7yedQwZhe.8duTR3eAdO3VCcwVCVvDVG.6i27H/IbLPxy+RVsqqmIEWyNfSwxmIemrsEHzbZYiik=")
k6 = LAG.LINE() 
k6.login(token="Eq2oCHdKBRuDqvc31Qa4.Rm04MXNPyrxKCBXzVCH+Ta.Hyi0fr4H3M9aVHUZDTaK48lEETDEfO4LZxuKHaClXUc=")
##############################################
reload(sys)
sys.setdefaultencoding('utf-8')
##############################################
helpMessage ="""v7.0.3 SRSU 6KICKER BOT
=========================
help ...コマンド一覧を送信します
test ...動いているか確認します
speed ...bot speed
mid ...midを送信します
mmid： ...メンションした人のmidを送信します
csend： ...midから連絡先を送信します
midi： ...midで招待します

cn： ...名前を変更します
gn： ...グループ名を変更します

curl ...招待リンクを許可します
ourl ...招待リンクを拒否します
gurl ...招待リンクを生成します
nk： ...名前で退会させます
ginfo ...グループ情報を送信します

g： ...googleで検索します
search： ...検索
=========================
tsk ...キッカーが動いているか確認します
say： ...キッカーに発言させます
sayk： ...キッカー全員に発言させます
say10： ...キッカーに発言させます(10連続)
in ...キッカー入室
bye ...キッカー退出
nkk： ...名前で退会させます(キッカー使用)
. + kickall ...破壊します
=========================
自動参加と強制自動退出が常時有効になっています
srsu.weebly.com"""
##############################################
wait = {
    'autoJoin':True,
    'leaveRoom':True,
    }
##############################################
AK=[cl,k1,k2,k3,k4,k5,k6]
K=[k1,k2,k3,k4,k5,k6]
##############################################
mid = cl.getProfile().mid
k1m= k1.getProfile().mid
k2m= k2.getProfile().mid
k3m= k3.getProfile().mid
k4m= k4.getProfile().mid
k5m= k5.getProfile().mid
k6m= k6.getProfile().mid
profile = cl.getProfile()
##############################################
admsa ="u1e5297a9058bbeb8a667002e40e3bf77","ub965db7580e876c9088646dc9e23820d","u7699546f21e66ee91a18c1843628f081","udec3b7230f166f949e492b0e5dc77810","u34a4e8bcb5d24c9c6aee39748553ef9a","uf0352daf711a0e8def7025af72f55dbe","uaccd389b19e96115e471bc59bdc87fb4","u0d573209a9ec91c27bb4a8e86a00e922"
##############################################
mid = cl.getProfile().mid
profile = cl.getProfile()
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
###自動機能
                if op.type == 13:
                    if wait["autoJoin"] == True:
                        cl.acceptGroupInvitation(op.param1)
                        k1.acceptGroupInvitation(op.param1)
                        k2.acceptGroupInvitation(op.param1)
                        k3.acceptGroupInvitation(op.param1)
                        k4.acceptGroupInvitation(op.param1)
                        k5.acceptGroupInvitation(op.param1)
                        k6.acceptGroupInvitation(op.param1)

                if op.type == 22:
                    if wait["leaveRoom"] == True:
                        cl.leaveRoom(op.param1)
                        k1.leaveRoom(op.param1)
                        k2.leaveRoom(op.param1)
                        k3.leaveRoom(op.param1)
                        k4.leaveRoom(op.param1)
                        k5.leaveRoom(op.param1)
                        k6.leaveRoom(op.param1)

                if op.type == 24:
                    if wait["leaveRoom"] == True:
                        cl.leaveRoom(op.param1)
                        k1.leaveRoom(op.param1)
                        k2.leaveRoom(op.param1)
                        k3.leaveRoom(op.param1)
                        k4.leaveRoom(op.param1)
                        k5.leaveRoom(op.param1)
                        k6.leaveRoom(op.param1)
##############################################
### command ##################################
##############################################
###確認
                elif x.text.lower() == 'help':
                  cl.sendText(x.to,helpMessage)

                elif x.text in ["test"]:
                  cl.sendText(x.to,"ok")

                elif x.text in ["speed"]:
                  start = time.time()
                  cl.sendText(x.to, "...")
                  elapsed_time = time.time() - start
                  cl.sendText(x.to, "%s" % (elapsed_time))

                elif x.text in ["ver"]:
                  cl.sendText(x.to,"SRSU 6KICKER BOT\nversion 7.0.3")
##############################################
###mid系コマンド
                elif x.text in ["mid"]:
                  cl.sendText(x.to,mid)

                elif ".me" == x.text:
                  x.contentType = 13
                  x.contentMetadata = {'mid': mid}
                  cl.sendMessage(x)

                elif ("mmid:" in x.text):
                  key = eval(x.contentMetadata["MENTION"])
                  key1 = key["MENTIONEES"][0]["M"]
                  key = cl.getContact(key1)
                  cl.sendText(x.to,key1)

                elif "csend:" in x.text:
                  mmid = x.text.replace("csend:","")
                  x.contentType = 13
                  x.contentMetadata = {"mid":mmid}
                  cl.sendMessage(x)

                elif "midi:" in x.text:
                  midd = x.text.replace("midi:","")
                  cl.findAndAddContactsByMid(midd)
                  cl.inviteIntoGroup(x.to,[midd])
##############################################
###変更
                elif "cn:" in x.text:
                  string = x.text.replace("cn:","")
                  if len(string.decode('utf-8')) <= 20:
                      profile = cl.getProfile()
                      profile.displayName = string
                      cl.updateProfile(profile)
                      cl.sendText(x.to,"名前を" + string + "に変更しました")

                elif ("gn:" in x.text):
                  if x.toType == 2:
                      g = cl.getGroup(x.to)
                      g.name = x.text.replace("gn:","")
                      cl.updateGroup(g)
                  else:
                      cl.sendText(x.to,"ここでは使用できません")
##############################################
###グループ系コマンド
                elif x.text in ["curl"]:
                    g = cl.getGroup(x.to)
                    g.preventJoinByTicket = True
                    cl.updateGroup(g)
                    cl.sendText(x.to,"拒否しました")

                elif x.text in ["ourl"]:
                    g = cl.getGroup(x.to)
                    g.preventJoinByTicket = False
                    cl.updateGroup(g)
                    cl.sendText(x.to,"許可しました")

                elif x.text in ["gurl"]:
                    if x.toType == 2:
                        g = cl.getGroup(x.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            cl.updateGroup(g)
                        gurl = cl.reissueGroupTicket(x.to)
                        cl.sendText(x.to,"http://line.me/R/ti/g/" + gurl)

                elif "nk:" in x.text:
                    g = cl.getGroup(x.to)
                    cl.updateGroup(g)
                    invsend = 0
                    cl.updateGroup(g)

                    nk0 = x.text.replace("nk:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in g.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(x.to,"not found")
                        pass
                    else:
                        for target in targets:
                                cl.kickoutFromGroup(x.to,[target])

                elif "ginfo" == x.text:
                  if x.toType == 2:
                      g = cl.getGroup(x.to)
                      try:
                        gCreator = g.creator.displayName
                      except:
                        gCreator = "不明"
                      if g.invitee is None:
                        sinvitee = "0"
                      else:
                        sinvitee = str(len(g.invitee))
                      if g.preventJoinByTicket == True:
                        QR = "拒否"
                      else:
                        QR = "許可"
                      cl.sendText(x.to,"グループ名 : " + str(g.name) + "\ngid : " + x.to + "\n作成者 : " + gCreator + "\n\n招待URL :" + QR + "\nグループ画像 : http://dl.profile.line.naver.jp/" + g.pictureStatus + "\nメンバー数 : " + str(len(g.members)) + "\n招待数 : " + sinvitee)
##############################################
###検索系
                elif "g:" in x.text:
                  s = x.text.replace("g:","")
                  cl.sendText(x.to,"google.com/search?q=" + s.replace("g:",""))

                elif "search:" in x.text:
                  s = x.text.replace("search:","")
                  cl.sendText(x.to,"\ngoogle : " + "google.com/search?q=" + s.replace("search:","") + "\ngoo : " + "search.goo.ne.jp/web.jsp?MT=" + s.replace("search:","") + "&mode=0&sbd=goo001&IE=UTF-8&OE=UTF-8&from=gootop&PT=TOP" + "\nbing : " + "bing.com/search?scope=web&q=" + s.replace("search:","") + "\nexcite : " + "websearch.excite.co.jp/?q=" + s.replace("search:","") + "\nnever : " + "matome.naver.jp/search?q=" + s.replace("search:","") + "\n楽天 : " + "websearch.rakuten.co.jp/WebIS?col=OW&svx=100610&nc=1&lg=all&svp=SEEK&enc=UTF-8&qt=" + s.replace("search:","") + "\nBIGLOBE : " + "cgi.search.biglobe.ne.jp/cgi-bin/search2-b?search=検索&q=" + s.replace("search:","") + "\nlivedoor : " + "search.livedoor.com/search?ie=utf-8&q=%E6%A4%9C%E7%B4%A2&search_btn=1" + s.replace("search:","") + "\nnifty : " + "search.nifty.com/websearch/search?select=2&ss=nifty_top_tp&cflg=検索&q=" + s.replace("search:","") + "\nyahoo : " + "search.yahoo.co.jp/search;_ylt=A2RA5ONbn7NaBjEAmGCJBtF7?p=" + s.replace("search:",""))
##############################################
##############################################
##############################################
#kicker
                elif x.text in ["tsk"]:
                  cl.sendText(x.to,"client")
                  k1.sendText(x.to,"kicker1")
                  k2.sendText(x.to,"kicker2")
                  k3.sendText(x.to,"kicker3")
                  k4.sendText(x.to,"kicker4")
                  k5.sendText(x.to,"kicker5")
                  k6.sendText(x.to,"kicker6")

                elif "say:" in x.text:
                  s = x.text.replace("say:","")
                  random.choice(K).sendText(x.to,"" + s.replace("say:",""))

                elif "say10:" in x.text:
                  s = x.text.replace("say10:","")
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))
                  random.choice(K).sendText(x.to,"" + s.replace("say10:",""))

                elif "sayk:" in x.text:
                  s = x.text.replace("sayk:","")
                  k1.sendText(x.to,"" + s.replace("sayk:",""))
                  k2.sendText(x.to,"" + s.replace("sayk:",""))
                  k3.sendText(x.to,"" + s.replace("sayk:",""))
                  k4.sendText(x.to,"" + s.replace("sayk:",""))
                  k5.sendText(x.to,"" + s.replace("sayk:",""))
                  k6.sendText(x.to,"" + s.replace("sayk:",""))

                elif x.text in ["in"]:
                  cl.getGroup(x.to)
                  g = cl.getGroup(x.to)
                  g.preventJoinByTicket = False
                  cl.updateGroup(g)
                  invsend = 0
                  Ticket = cl.reissueGroupTicket(x.to)
                  k1.acceptGroupInvitationByTicket(x.to,Ticket)
                  k2.acceptGroupInvitationByTicket(x.to,Ticket)
                  k3.acceptGroupInvitationByTicket(x.to,Ticket)
                  k4.acceptGroupInvitationByTicket(x.to,Ticket)
                  k5.acceptGroupInvitationByTicket(x.to,Ticket)
                  k6.acceptGroupInvitationByTicket(x.to,Ticket)

                elif x.text in ["bye"]:
                  k1.leaveGroup(x.to)
                  k2.leaveGroup(x.to)
                  k3.leaveGroup(x.to)
                  k4.leaveGroup(x.to)
                  k5.leaveGroup(x.to)
                  k6.leaveGroup(x.to)

                elif "kn:" in x.text:
                  string = x.text.replace("kn:","")
                  if len(string.decode('utf-8')) <= 20:
                      profile = k1.getProfile()
                      profile = k2.getProfile()
                      profile = k3.getProfile()
                      profile = k4.getProfile()
                      profile = k5.getProfile()
                      profile = k6.getProfile()
                      profile.displayName = string
                      k1.updateProfile(profile)
                      k2.updateProfile(profile)
                      k3.updateProfile(profile)
                      k4.updateProfile(profile)
                      k5.updateProfile(profile)
                      k6.updateProfile(profile)
                      cl.sendText(x.to,"変更しました")

                elif "nkk:" in x.text:
                    g = cl.getGroup(x.to)
                    cl.updateGroup(g)
                    invsend = 0
                    cl.updateGroup(g)

                    nk0 = x.text.replace("nkk:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in g.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(x.to,"not found")
                        pass
                    else:
                        for target in targets:
                                random.choice(K).kickoutFromGroup(x.to,[target])

                elif ".kickall" in x.text:
                  if x.toType == 2:
                      _name = x.text.replace(".kickall","")
                      gs = cl.getGroup(x.to)
                      targets = []
                      for g in gs.members:
                          if _name in g.displayName:
                              targets.append(g.mid)
                      if targets == []:
                          cl.sendText(x.to,"Not found")
                      else:
                          for target in targets:
                            if not target in admsa:
                              try:
                                  random.choice(K).kickoutFromGroup(x.to,[target])
                              except:
                                  random.choice(K).sendText(x.to,"error")



##############################################
##############################################
##############################################
##############################################
##############################################
        if op.type == 59:
            print op           
    except Exception as error:
        print error
while True:
	bot(cl.Poll.stream(500000))

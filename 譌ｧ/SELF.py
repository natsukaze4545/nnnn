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
helpMessage ="""v7.0.3 SRSU SELF BOT
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
===============
自動参加と強制自動退出が常時有効になっています
srsu.weebly.com"""
##############################################
wait = {
    'autoJoin':True,
    'leaveRoom':True,
    }
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

                if op.type == 22:
                    if wait["leaveRoom"] == True:
                        cl.leaveRoom(op.param1)

                if op.type == 24:
                    if wait["leaveRoom"] == True:
                        cl.leaveRoom(op.param1)
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
                  cl.sendText(x.to,"SRSU SELF BOT\nversion 7.0.3")
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
#google
                elif "g:" in x.text:
                  s = x.text.replace("g:","")
                  cl.sendText(x.to,"google.com/search?q=" + s.replace("g:",""))

                elif "search:" in x.text:
                  s = x.text.replace("search:","")
                  cl.sendText(x.to,"\ngoogle : " + "google.com/search?q=" + s.replace("search:","") + "\ngoo : " + "search.goo.ne.jp/web.jsp?MT=" + s.replace("search:","") + "&mode=0&sbd=goo001&IE=UTF-8&OE=UTF-8&from=gootop&PT=TOP" + "\nbing : " + "bing.com/search?scope=web&q=" + s.replace("search:","") + "\nexcite : " + "websearch.excite.co.jp/?q=" + s.replace("search:","") + "\nnever : " + "matome.naver.jp/search?q=" + s.replace("search:","") + "\n楽天 : " + "websearch.rakuten.co.jp/WebIS?col=OW&svx=100610&nc=1&lg=all&svp=SEEK&enc=UTF-8&qt=" + s.replace("search:","") + "\nBIGLOBE : " + "cgi.search.biglobe.ne.jp/cgi-bin/search2-b?search=検索&q=" + s.replace("search:","") + "\nlivedoor : " + "search.livedoor.com/search?ie=utf-8&q=%E6%A4%9C%E7%B4%A2&search_btn=1" + s.replace("search:","") + "\nnifty : " + "search.nifty.com/websearch/search?select=2&ss=nifty_top_tp&cflg=検索&q=" + s.replace("search:","") + "\nyahoo : " + "search.yahoo.co.jp/search;_ylt=A2RA5ONbn7NaBjEAmGCJBtF7?p=" + s.replace("search:",""))
##############################################

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
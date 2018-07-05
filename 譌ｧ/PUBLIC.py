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
cl.login(token="Eq0xkbFlQkZuAuJZ9j70.3So3iW8wB5sEssSoxCD4ea.MRWAvyDMfS7ZWlOAMr9je7YP48464T4J80Xc/OOwWLg=")
cl.loginResult()
##############################################
reload(sys)
sys.setdefaultencoding('utf-8')
##############################################
helpMessage ="""PUBLIC BOT
help ...コマンド一覧を送信します
test ...動いているか確認します
speed ...bot speed
mid ...midを送信します
csend： ...midから連絡先を送信します
ginfo ...グループ情報を送信します
g： ...googleで検索します
search： ...検索
srsu.weebly.com"""
##############################################
mid = cl.getProfile().mid
profile = cl.getProfile()
##############################################
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']
##############################################
def Cmd(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = [""]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    x = Message()
    x.to = to
    x.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    x.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(x)
    except Exception as error:
        print error
##############################################
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 26:
            x = op.message
            if x.contentType == 13:
                return    
            if x.contentType == 0:
                if x.text == None:
                    return
### command ##################################
                elif x.text.lower() == '.help':
                  cl.sendText(x.to,helpMessage)

                elif x.text in [".test"]:
                  cl.sendText(x.to,"ok")

                elif x.text in [".speed"]:
                  start = time.time()
                  cl.sendText(x.to, "...")
                  elapsed_time = time.time() - start
                  cl.sendText(x.to, "%s" % (elapsed_time))

                elif x.text in [".version"]:
                  cl.sendText(x.to,"PUBLIC")
##############################################
                elif x.text in [".mid"]:
                  cl.sendText(x.to,mid)

                elif ".csend:" in x.text:
                  mmid = x.text.replace("csend:","")
                  x.contentType = 13
                  x.contentMetadata = {"mid":mmid}
                  cl.sendMessage(x)
##############################################
                elif ".ginfo" == x.text:
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

#全員をメンション(上が使えなかったらこっち) /allmention
                elif x.text in ["/all mention"]:
                  group = cl.getGroup(x.to)
                  nama = [contact.mid for contact in group.members]
                  nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                  if jml <= 100:
                     summon(x.to, nama)
                  if jml > 100 and jml < 200:
                     for i in range(0, 99):
                         nm1 += [nama[i]]
                     summon(x.to, nm1)
                     for j in range(100, len(nama)-1):
                         nm2 += [nama[j]]
                     summon(x.to, nm2)
                  if jml > 200  and jml < 500:
                     for i in range(0, 99):
                         nm1 += [nama[i]]
                     summon(x.to, nm1)
                     for j in range(100, 199):
                         nm2 += [nama[j]]
                     summon(x.to, nm2)
                     for k in range(200, 299):
                         nm3 += [nama[k]]
                     summon(x.to, nm3)
                     for l in range(300, 399):
                         nm4 += [nama[l]]
                     summon(x.to, nm4)
                     for m in range(400, len(nama)-1):
                         nm5 += [nama[m]]
                     summon(x.to, nm5)
                  if jml > 500:
                      print "Terlalu Banyak Men 500+"
                  cnt = Message()
                  cnt.text = "メンションした人数:\n" + str(jml) +  " 人"
                  cnt.to = x.to
                  cl.sendMessage(cnt)
##############################################
                elif ".g:" in x.text:
                  s = x.text.replace("g:","")
                  cl.sendText(x.to,"google.com/search?q=" + s.replace("g:",""))

                elif ".search:" in x.text:
                  s = x.text.replace("search:","")
                  cl.sendText(x.to,"\ngoogle : " + "google.com/search?q=" + s.replace("search:","") + "\ngoo : " + "search.goo.ne.jp/web.jsp?MT=" + s.replace("search:","") + "&mode=0&sbd=goo001&IE=UTF-8&OE=UTF-8&from=gootop&PT=TOP" + "\nbing : " + "bing.com/search?scope=web&q=" + s.replace("search:","") + "\nexcite : " + "websearch.excite.co.jp/?q=" + s.replace("search:","") + "\nnever : " + "matome.naver.jp/search?q=" + s.replace("search:","") + "\n楽天 : " + "websearch.rakuten.co.jp/WebIS?col=OW&svx=100610&nc=1&lg=all&svp=SEEK&enc=UTF-8&qt=" + s.replace("search:","") + "\nBIGLOBE : " + "cgi.search.biglobe.ne.jp/cgi-bin/search2-b?search=検索&q=" + s.replace("search:","") + "\nlivedoor : " + "search.livedoor.com/search?ie=utf-8&q=%E6%A4%9C%E7%B4%A2&search_btn=1" + s.replace("search:","") + "\nnifty : " + "search.nifty.com/websearch/search?select=2&ss=nifty_top_tp&cflg=検索&q=" + s.replace("search:","") + "\nyahoo : " + "search.yahoo.co.jp/search;_ylt=A2RA5ONbn7NaBjEAmGCJBtF7?p=" + s.replace("search:",""))
#-------------------------------------------------------------------------------#lastseen
                elif x.text == "ぽいんと":
                        cl.sendText(x.to, "既読ポイントを設定しました。確認したい場合は「ちぇっく」と送信してください。")
                        try:
                            del wait2['readPoint'][x.to]
                            del wait2['readMember'][x.to]
                        except:
                            pass
                        now2 = datetime.now()
                        wait2['readPoint'][x.to] = x.id
                        wait2['readMember'][x.to] = ""
                        wait2['setTime'][x.to] = datetime.strftime(now2,"%H:%M")
                        wait2['ROM'][x.to] = {}
                        print wait2

                elif x.text == "ちぇっく":
                        if x.to in wait2['readPoint']:
                            if wait2["ROM"][x.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2["ROM"][x.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            cl.sendText(x.to,"きどく %s\nきどくむし\n%s\nせっていじこく:\n[%s]" % (wait2['readMember'][x.to],chiya,setTime[x.to]))
                        else:
                             cl.sendText(x.to,"既読ポイントが設定されていません。「ぽいんと」と送信して既読ポイントを設定してください")

#-------------------------------------------------------#search

        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                cl.sendText
        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
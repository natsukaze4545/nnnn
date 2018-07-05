#SRSU LINE KICKER BOT v9.0.2
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
##############################################
k1 = LAG.LINE()
k1.login(token="Er0Xwc7yUPHSjDe5b7Ba.nktOVlxstjXQ7JL0HvpVMG.ruC0hU/zbYHS24/Nn3W0htLpPo4ImuTiKCLCasHsBzo=")
##############################################
k2 = LAG.LINE()
k2.login(token="ErM9EzKB2eXMx1mNdwKe.8duTR3eAdO3VCcwVCVvDVG.tNtHYRbl+q1qA5cOPO9ATxiKnKBpD4RJ0KCdhWFbH6M=")
##############################################
k3 = LAG.LINE()
k3.login(token="ErAFzOkeg0xFOxIqSBV4.Rm04MXNPyrxKCBXzVCH+Ta.MbSQbpmJ8eIB/l0uh+sWNK0AR6ZycIGWm1PXBCD9Xn0=")
##############################################
k4 = LAG.LINE()
k4.login(token="Ere3RcJpHmd97BgvcjV1.DPLuBYhMBUKAgmgenIJWGq.DycQo+7SocPyeMbrcBN5CNbrgf2AAFVsRqvvodJo68g=")
##############################################
k5 = LAG.LINE()
k5.login(token="ErbduPwuYTpzcP0QB8r7.hLkxQqwlVRIMzWaUqoo+DW.J/aKIZZWmEQbdHW5pH9IPbQ9WKxrnKWf0zLFA/Mcrak=")
##############################################
cl.loginResult()
print(cl.getUserTicket())
##############################################
reload(sys)
sys.setdefaultencoding('utf-8')
##############################################
helpMessage ="""SRSU KICKER BOT HELP

help ...コマンド一覧を表示
==================
test ...動作確認
speed ...処理速度
ver ...バージョン確認
runtime ...動作時間
time ...現在時刻
==================
mid ...my mid
me ...自分の連絡先
mif ...自分の情報
flist ...友達リスト
glist ...グループ一覧
blist ...ブロックリスト一覧
==================
cn：name ...名前変更
gn：name ...グループ名変更
cs：status ...ステータス変更
==================
ginfo ...グループ情報
gid ...group id
mlist ...グループメンバー
gcreator ...作成者
==================
mid：@ ...メンションした人のmid
mif：@ ...メンションした人の情報
csend：mid ...midで連絡先
tagall ...全員メンション
==================
gurl ...リンク作成
ourl ...リンク許可
curl ...リンク拒否
==================
nk：name ...名前蹴り
mk：@ ...メンションした人を蹴る
mik：mid ...midで蹴る
mi：mid ...midで招待
==================
search： ...検索
gift1~14 ...プレゼント
rps ...既読設定
rpc ...既読確認
==================
sayk：
in
bye
mikk：
nkk：
mkk：
! + kickall


srsu.weebly.com"""

#reboot ...再起動
##############################################
wait = {
    'likeOn':True,
    }
##############################################
wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }
##############################################
setTime = {}
setTime = wait2['setTime']
##############################################
mulai = time.time() 
##############################################
AK=[cl,k1,k2,k3,k4,k5]
K=[k1,k2,k3,k4,k5]
##############################################
mid = cl.getProfile().mid
k1m= k1.getProfile().mid
k2m= k2.getProfile().mid
k3m= k3.getProfile().mid
k4m= k4.getProfile().mid
k5m= k5.getProfile().mid
##############################################
admsa ="u0d573209a9ec91c27bb4a8e86a00e922","u34a4e8bcb5d24c9c6aee39748553ef9a","uf0352daf711a0e8def7025af72f55dbe","uaccd389b19e96115e471bc59bdc87fb4","u7699546f21e66ee91a18c1843628f081","u1e5297a9058bbeb8a667002e40e3bf77"
##############################################
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
##############################################
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d:%02d:%02d' % (hours, mins, secs) 
##############################################
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
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error 
##############################################
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 26:
            x = op.message
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k1.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k2.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k3.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k4.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k5.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            x = op.message
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k1.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k2.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k3.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k4.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k5.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 13:
                return 
            if x.contentType == 0:
                if x.text == None:
                    return
##############################################
##############################################
### command ##################################
##############################################
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
                  cl.sendText(x.to,"SRSU KICKER BOT\nversion 9.0.2")

                elif x.text.lower() == 'runtime':
                  eltime = time.time() - mulai
                  van = "Run time : "+waktu(eltime)
                  cl.sendText(x.to,van)
##############################################
                elif x.text in ["mid"]:
                  cl.sendText(x.to,mid)

                elif x.text in ["gid"]:
                  if x.toType == 2:
                      cl.getGroup(x.to)
                      cl.sendText(x.to,x.to)

                elif "me" == x.text:
                  x.contentType = 13
                  x.contentMetadata = {'mid': mid}
                  cl.sendMessage(x)

                elif ("mid:" in x.text):
                  key = eval(x.contentMetadata["MENTION"])
                  key1 = key["MENTIONEES"][0]["M"]
                  key = cl.getContact(key1)
                  cl.sendText(x.to,key1)

                elif "csend:" in x.text:
                  mmid = x.text.replace("csend:","")
                  x.contentType = 13
                  x.contentMetadata = {"mid":mmid}
                  cl.sendMessage(x)

                elif "mi:" in x.text:
                  midd = x.text.replace("mi:","")
                  cl.findAndAddContactsByMid(midd)
                  cl.inviteIntoGroup(x.to,[midd])

                elif "mik:" in x.text:
                  midd = x.text.replace("mik:","")
                  cl.kickoutFromGroup(x.to,[midd])
##############################################
                elif "cn:" in x.text:
                  string = x.text.replace("cn:","")
                  if len(string.decode('utf-8')) <= 20:
                      profile = cl.getProfile()
                      profile.displayName = string
                      cl.updateProfile(profile)
                      cl.sendText(x.to,"ok")

                elif ("gn:" in x.text):
                  if x.toType == 2:
                      g = cl.getGroup(x.to)
                      g.name = x.text.replace("gn:","")
                      cl.updateGroup(g)
                  else:
                      cl.sendText(x.to,"error")

                elif "cs:" in x.text:
                    string = x.text.replace("cs:","")
                    if len(string.decode('utf-8')) <= 500:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendText(x.to,"ok")
##############################################
                elif x.text in ["curl"]:
                    g = cl.getGroup(x.to)
                    g.preventJoinByTicket = True
                    cl.updateGroup(g)
                    cl.sendText(x.to,"close")

                elif x.text in ["ourl"]:
                    g = cl.getGroup(x.to)
                    g.preventJoinByTicket = False
                    cl.updateGroup(g)
                    cl.sendText(x.to,"open")

                elif x.text in ["gurl"]:
                    if x.toType == 2:
                        g = cl.getGroup(x.to)
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

	        elif "mk:" in x.text:        
		  if 'MENTION' in x.contentMetadata.keys()!= None:
		      names = re.findall(r'@(\w+)', x.text)
		      mention = ast.literal_eval(x.contentMetadata['MENTION'])
		      mentionees = mention['MENTIONEES']
		      print mentionees
		      for mention in mentionees:
			  cl.kickoutFromGroup(x.to,[mention['M']])

	        elif x.text in ["gcreator"]:
		  ginfo = cl.getGroup(x.to)
		  gCreator = ginfo.creator.mid
                  x.contentType = 13
                  x.contentMetadata = {'mid': gCreator}
                  cl.sendMessage(x)

                elif "ginfo" == x.text:
                  if x.toType == 2:
                      g = cl.getGroup(x.to)
                      try:
                        gCreator = g.creator.displayName
                      except:
                        gCreator = "error"
                      if g.invitee is None:
                        sinvitee = "0"
                      else:
                        sinvitee = str(len(g.invitee))
                      if g.preventJoinByTicket == True:
                        QR = "close"
                      else:
                        QR = "open"
                      cl.sendText(x.to,"gname : " + str(g.name) + "\ngid : " + x.to + "\ngcreator : " + gCreator + "\nglink : " + QR + "\ngpicture : http://dl.profile.line.naver.jp/" + g.pictureStatus + "\nmember : " + str(len(g.members)) + "\ninvite : " + sinvitee)
##############################################
                elif "search:" in x.text:
                  s = x.text.replace("search:","")
                  cl.sendText(x.to,"google : " + "google.com/search?q=" + s.replace("search:","") + "\ngoo : " + "search.goo.ne.jp/web.jsp?MT=" + s.replace("search:","") + "&mode=0&sbd=goo001&IE=UTF-8&OE=UTF-8&from=gootop&PT=TOP" + "\nbing : " + "bing.com/search?scope=web&q=" + s.replace("search:","") + "\nexcite : " + "websearch.excite.co.jp/?q=" + s.replace("search:","") + "\nnever : " + "matome.naver.jp/search?q=" + s.replace("search:","") + "\n楽天 : " + "websearch.rakuten.co.jp/WebIS?col=OW&svx=100610&nc=1&lg=all&svp=SEEK&enc=UTF-8&qt=" + s.replace("search:","") + "\nBIGLOBE : " + "cgi.search.biglobe.ne.jp/cgi-bin/search2-b?search=検索&q=" + s.replace("search:","") + "\nlivedoor : " + "search.livedoor.com/search?ie=utf-8&q=%E6%A4%9C%E7%B4%A2&search_btn=1" + s.replace("search:","") + "\nnifty : " + "search.nifty.com/websearch/search?select=2&ss=nifty_top_tp&cflg=検索&q=" + s.replace("search:","") + "\nyahoo : " + "search.yahoo.co.jp/search;_ylt=A2RA5ONbn7NaBjEAmGCJBtF7?p=" + s.replace("search:",""))
##############################################

                elif x.text in ["time"]:
                    cl.sendText(x.to,datetime.today().strftime('%H:%M:%S'))

                elif x.text in ["glist"]:
                     gid = cl.getGroupIdsJoined()
                     h = ""
                     for i in gid:
                      h += " %s \n" % (cl.getGroup(i).name + " : " + str(len (cl.getGroup(i).members)))
                     cl.sendText(x.to, "Group list : \n"+ h +"total : " +str(len(gid)))

                elif x.text.lower() == 'blist':
                    blockedlist = cl.getBlockedContactIds()
                    kontak = cl.getContacts(blockedlist)
                    num=1
                    msgs="Block list : \n"
                    for ids in kontak:
                       msgs+="\n%i. %s" % (num, ids.displayName)
                       num=(num+1)
                    msgs+="\n\n total : %i " % len(kontak)
                    cl.sendText(x.to, msgs)

                elif x.text in ["gift"]:
                    x.contentType = 9
                    x.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '3'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift2"]:
                    x.contentType = 9
                    x.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '4'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift3"]:
                    x.contentType = 9
                    x.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '5'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift4"]:
                    x.contentType = 9
                    x.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                        'PRDTYPE': 'THEME',
                                        'MSGTPL': '6'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift5"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '1',
                                       'STKPKGID': '1380280'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift6"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '2',
                                       'STKPKGID': '1360738'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift7"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '3',
                                       'STKPKGID': '1395389'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift8"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '4',
                                       'STKPKGID': '1329191'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift9"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '1',
                                       'STKPKGID': '9057'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift10"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '2',
                                       'STKPKGID': '9167'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift11"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '3',
                                       'STKPKGID': '7334'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift12"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '1',
                                       'STKPKGID': '1380280'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift13"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '4',
                                       'STKPKGID': '1405277'}
                    x.text = None
                    cl.sendMessage(x)

                elif x.text in ["gift14"]:
                    x.contentType = 9
                    x.contentMetadata= {'PRDTYPE': 'STICKER',
                                       'STKVER': '1',
                                       'MSGTPL': '1',
                                       'STKPKGID': '1296261'}
                    x.text = None
                    cl.sendMessage(x)
##############################################
                elif x.text in ["mif"]:
                    me = cl.getContact(mid)
                    cu = cl.channel.getCover(mid)
                    cl.sendText(x.to,"[mid]\n" + mid + "\n" + "\n" +"[name]\n" +  me.displayName + "\n" + "\n" + "[Status]\n" + me.statusMessage + "\n" + "\n" + "[picture]\n" + "http://dl.profile.line-cdn.net/" + me.pictureStatus + "\n" + "\n" + "[cover]\n" + str(cu))

                elif ("mif:" in x.text):
                    mention = eval(x.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    cu = cl.channel.getCover(mention1)
                    try:
                        cl.sendText(x.to,"[mid]\n" + mention1 + "\n" + "\n" +"[name]\n" +  contact.displayName + "\n" + "\n" + "[Status]\n" + contact.statusMessage + "\n" + "\n" + "[picture]\n" + "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n" + "\n" + "[cover]\n" + str(cu))
                    except:
                        pass

	        elif x.text in ["reboot"]:
		    cl.sendText(x.to, "...")
		    restart_program()

                elif x.text in ["tagall"]:
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
                     cnt.text = "total : " + str(jml)
                     cnt.to = x.to
                     cl.sendMessage(cnt)
##############################################
                elif x.text == "rps":
                        cl.sendText(x.to, "set")
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

                elif x.text == "rpc":
                        if x.to in wait2['readPoint']:
                            if wait2["ROM"][x.to].items() == []:
                                chiya = ""
                            else:
                                chiya = ""
                                for rom in wait2["ROM"][x.to].items():
                                    print rom
                                    chiya += rom[1] + "\n"
                            cl.sendText(x.to,"Read %s\n\n%s\nset time :\n[%s]" % (wait2['readMember'][x.to],chiya,setTime[x.to]))
                        else:
                             cl.sendText(x.to,"point has not")
##############################################
                elif x.text in ["flist"]:    
                    contactlist = cl.getAllContactIds()
                    kontak = cl.getContacts(contactlist)
                    num=1
                    msgs="Friend list"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="total : %i" % len(kontak)
                    cl.sendText(x.to, msgs)
                
                elif x.text in ["mlist"]:   
                    kontak = cl.getGroup(x.to)
                    group = kontak.members
                    num=1
                    msgs="Group member list"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="total : %i" % len(group)
                    cl.sendText(x.to, msgs)
##############################################
                elif x.text in ["kicker"]:
                  cl.sendText(x.to,"client")
                  k1.sendText(x.to,"kicker1")
                  k2.sendText(x.to,"kicker2")
                  k3.sendText(x.to,"kicker3")
                  k4.sendText(x.to,"kicker4")
                  k5.sendText(x.to,"kicker5")

                elif "sayk:" in x.text:
                  s = x.text.replace("sayk:","")
                  k1.sendText(x.to,"" + s.replace("sayk:",""))
                  k2.sendText(x.to,"" + s.replace("sayk:",""))
                  k3.sendText(x.to,"" + s.replace("sayk:",""))
                  k4.sendText(x.to,"" + s.replace("sayk:",""))
                  k5.sendText(x.to,"" + s.replace("sayk:",""))

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

                elif x.text in ["bye"]:
                  k1.leaveGroup(x.to)
                  k2.leaveGroup(x.to)
                  k3.leaveGroup(x.to)
                  k4.leaveGroup(x.to)
                  k5.leaveGroup(x.to)

                elif "mikk:" in x.text:
                  midd = x.text.replace("mikk:","")
                  random.choice(K).kickoutFromGroup(x.to,[midd])

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

	        elif "mkk:" in x.text:        
		  if 'MENTION' in x.contentMetadata.keys()!= None:
		      names = re.findall(r'@(\w+)', x.text)
		      mention = ast.literal_eval(x.contentMetadata['MENTION'])
		      mentionees = mention['MENTIONEES']
		      print mentionees
		      for mention in mentionees:
			  random.choice(K).kickoutFromGroup(x.to,[mention['M']])

                elif "!kickall" in x.text:
                  if x.toType == 2:
                      _name = x.text.replace("!kickall","")
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

	        elif x.text in ["mybots"]:
                  x.contentType = 13
                  x.contentMetadata = {'mid': "u0d573209a9ec91c27bb4a8e86a00e922"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "u34a4e8bcb5d24c9c6aee39748553ef9a"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "uf0352daf711a0e8def7025af72f55dbe"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "uaccd389b19e96115e471bc59bdc87fb4"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "u7699546f21e66ee91a18c1843628f081"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "u1e5297a9058bbeb8a667002e40e3bf77"}
                  cl.sendMessage(x)

                elif "kn:" in x.text:
                  string = x.text.replace("kn:","")
                  if len(string.decode('utf-8')) <= 20:
                      profile = k1.getProfile()
                      profile = k2.getProfile()
                      profile = k3.getProfile()
                      profile = k4.getProfile()
                      profile = k5.getProfile()
                      profile.displayName = string
                      k1.updateProfile(profile)
                      k2.updateProfile(profile)
                      k3.updateProfile(profile)
                      k4.updateProfile(profile)
                      k5.updateProfile(profile)
                      cl.sendText(x.to,"ok")

	        elif x.text in ["kicker set"]:
                      profile1 = k1.getProfile()
                      profile2 = k2.getProfile()
                      profile3 = k3.getProfile()
                      profile4 = k4.getProfile()
                      profile5 = k5.getProfile()
                      profile1.statusMessage = "1\nalFIVXw"
                      profile2.statusMessage = "2\nYlt8UWE"
                      profile3.statusMessage = "3\nWVwDXkh8"
                      profile4.statusMessage = "4\nSEZfR0o"
                      profile5.statusMessage = "5\naEpVSWg"
                      k1.updateProfile(profile1)
                      k2.updateProfile(profile2)
                      k3.updateProfile(profile3)
                      k4.updateProfile(profile4)
                      k5.updateProfile(profile5)
                      profile6 = k1.getProfile()
                      profile7 = k2.getProfile()
                      profile8 = k3.getProfile()
                      profile9 = k4.getProfile()
                      profile10 = k5.getProfile()
                      profile6.displayName = "alFIVXw"
                      profile7.displayName = "Ylt8UWE"
                      profile8.displayName = "WVwDXkh8"
                      profile9.displayName = "SEZfR0o"
                      profile10.displayName = "aEpVSWg"
                      k1.updateProfile(profile6)
                      k2.updateProfile(profile7)
                      k3.updateProfile(profile8)
                      k4.updateProfile(profile9)
                      k5.updateProfile(profile10)
                      cl.sendText(x.to,"ok")

	        elif x.text in ["kicker set2"]:
                      profile1 = k1.getProfile()
                      profile2 = k2.getProfile()
                      profile3 = k3.getProfile()
                      profile4 = k4.getProfile()
                      profile5 = k5.getProfile()
                      profile1.statusMessage = "1"
                      profile2.statusMessage = "2"
                      profile3.statusMessage = "3"
                      profile4.statusMessage = "4"
                      profile5.statusMessage = "5"
                      k1.updateProfile(profile1)
                      k2.updateProfile(profile2)
                      k3.updateProfile(profile3)
                      k4.updateProfile(profile4)
                      k5.updateProfile(profile5)
                      profile6 = k1.getProfile()
                      profile7 = k2.getProfile()
                      profile8 = k3.getProfile()
                      profile9 = k4.getProfile()
                      profile10 = k5.getProfile()
                      profile6.displayName = ""
                      profile7.displayName = ""
                      profile8.displayName = ""
                      profile9.displayName = ""
                      profile10.displayName = ""
                      k1.updateProfile(profile6)
                      k2.updateProfile(profile7)
                      k3.updateProfile(profile8)
                      k4.updateProfile(profile9)
                      k5.updateProfile(profile10)
                      cl.sendText(x.to,"ok")
##############################################
##############################################
##############################################
##############################################
##############################################
        if op.type == 59:
            print op         
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = cl.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n" + Name
                    wait2['ROM'][op.param1][op.param2] = "" + Name
            else:
                cl.sendText  
    except Exception as error:
        print error
while True:
	bot(cl.Poll.stream(500000))
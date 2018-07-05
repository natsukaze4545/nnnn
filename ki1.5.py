#MK:RENT BOT v10.0.0
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
try:
    f=open('cl8.csv','r')
    token=f.read()
    cl.login(token=token)
    f.close()
except:
    cl.login(token=qr().get())
    f=open('cl8.csv','w')
    f.write(cl.authToken)
    f.close()
##############################################
k1 = LAG.LINE()
k1.login(token="EuqyhHGgNxkRyK6RuMib.A2FDe2nvqKuQc80dP+Qq6W.71x8lSSeb6CTD9g+GBgruNIG4cc6zpVLVy3aRO0NCeI=")
##############################################
cl.loginResult()
print cl.getUserTicket()
##############################################
reload(sys)
sys.setdefaultencoding('utf-8')
##############################################
print "Login START"

helpMessage = """レタス　bot

help→コマンドを表示
=================
test→動作確認
speed→処理速度
ver→バージョン確認
runtime→動作時間
time→現在時刻
=================
mid→自分のmid
me→自分の連絡先
mif→自分の情報
flist→友達リスト
glist→グループ一覧
blist→ブロックリスト一覧
=================
cn:name→名前変更
gn:name→グループ名変更
cs:status→一コメ変更
=================
mid:@→メンションした人のmid
mif:@→メンションした人の情報
csend:mid→midで連絡先
tagall→全員メンション
=================
gurl→リンク作成
ourl→リンク許可
curl→リンク拒否
=================
nk:name→名前蹴り
mk:@→メンションした人を蹴る
mik:mid→midで蹴る
mi:mid→midで招待
=================
search:→検索
gift1~14→プレゼント
rps→既読設定
rpc→既読確認
mention→自分をメンション
=================
sayk:キッカー発言
mikk→midでkick
nkk→名前でkick
mkk→メンションした人kick
kickall→破壊
mybots→キッカーと自分の連絡先
kn→キッカー名前変更
=================
READ ON
READ OFF"""

#reboot ...再起動
##############################################
wait = {
    'likeOn':True,
    "alwayRead":False,
    }

message = {
    "replyPesan":"[AUTO RESPON]",
}

settings = {
    "responMention":False,
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
KI = [k1]
##############################################
AK=[cl,k1]
K=[k1]
##############################################
mid = cl.getProfile().mid
k1m= k1.getProfile().mid
##############################################
admsa ="ue2c03c7c19d52d851c61c18bf91a0635","ue04d0d3566d463a6bbb085be97a575de","u7361f4eb17a331ebc993588ef4127935","u24f57bf1dc033b4010bcd248333a5b23","ua2320e07ebf3d0eb33e3fdbcac0cfea1","u6989c73030948745fe083c4bf433f4bd"
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
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
##############################################
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 15:
            if op.param2 in mid:
                return
            random.choice(K).sendText(op.param1,"バイバイ〜" + cl.getContact(op.param2).displayName + "さん" + datetime.today().strftime('%H:%M:%S') )
        if op.type == 19:
            if op.param2 in mid:
                return
            random.choice(K).sendText(op.param1,cl.getContact(op.param2).displayName + "が退会させたよ〜\n" +datetime.today().strftime('%H:%M:%S') )
        if op.type == 26:
            x = op.message
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k1.like(url[25:58], url[66:], likeType=1001)

            if wait["alwayRead"] == True:
                if x.toType == 0:
                    cl.sendChatChecked(x.from_,x.id)
                else:
                    cl.sendChatChecked(x.to,x.id)

                if x.toType == 0:
                    k1.sendChatChecked(x.from_,x.id)
                else:
                    k1.sendChatChecked(x.to,x.id)

            if 'MENTION' in x.contentMetadata.keys()!=None:
                 if settings["responMention"] == True:
                    names = re.findall(r'@(\w+)',x.text)
                    mention = ast.literal_eval(x.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in mid:
                            xname = cl.getContact(x.from_).displayName
                            xlen = str(len(xname)+1)
                            x.contentType = 0
                            balas = "@" + xname + " " + str(message["replyPesan"])
                            x.text = balas
                            x.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(x.from_)+'}]}','EMTVER':'4'}
                            cl.sendMessage(x)
                            cl.sendText(x.to,"DON'T TAG ME.\nsrsu.weebly.com")

        if op.type == 25:
            x = op.message
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                cl.like(url[25:58], url[66:], likeType=1001)
            if x.contentType == 16:
                url = x.contentMetadata["postEndUrl"]
                k1.like(url[25:58], url[66:], likeType=1001)

            if wait["alwayRead"] == True:
                if x.toType == 0:
                    cl.sendChatChecked(x.from_,x.id)
                else:
                    cl.sendChatChecked(x.to,x.id)
                if x.toType == 0:
                    k1.sendChatChecked(x.from_,x.id)
                else:
                    k1.sendChatChecked(x.to,x.id)

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
                  cl.sendText(x.to,"SRSU KICKER BOT\nversion 10.0.0")

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
                  k1.sendText(x.to,"kicker")

                elif "sayk:" in x.text:
                  s = x.text.replace("sayk:","")
                  k1.sendText(x.to,"" + s.replace("sayk:",""))

                elif x.text in ["in"]:
                  cl.getGroup(x.to)
                  g = cl.getGroup(x.to)
                  g.preventJoinByTicket = False
                  cl.updateGroup(g)
                  invsend = 0
                  Ticket = cl.reissueGroupTicket(x.to)
                  k1.acceptGroupInvitationByTicket(x.to,Ticket)

                elif x.text in ["草"]:
                  for me in KI:
                    me.leaveGroup(x.to)

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
                  x.contentMetadata = {'mid': "ue2c03c7c19d52d851c61c18bf91a0635"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "ue04d0d3566d463a6bbb085be97a575de"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "u7361f4eb17a331ebc993588ef4127935"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "u24f57bf1dc033b4010bcd248333a5b23"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "ua2320e07ebf3d0eb33e3fdbcac0cfea1"}
                  cl.sendMessage(x)
                  x.contentMetadata = {'mid': "u6989c73030948745fe083c4bf433f4bd"}
                  cl.sendMessage(x)

                elif "kn:" in x.text:
                  string = x.text.replace("kn:","")
                  if len(string.decode('utf-8')) <= 20:
                      profile = k1.getProfile()
                      profile.displayName = string
                      k1.updateProfile(profile)
                      cl.sendText(x.to,"ok")
##############################################
                elif x.text in ["READ ON"]:
                    wait['alwayRead'] = True
                    cl.sendText(x.to,"AUTO READ ON")

                elif x.text in ["READ OFF"]:
                    wait['alwayRead'] = False
                    cl.sendText(x.to,"AUTO READ OFF")

                elif x.text in ["RESPON ON"]:
                    settings["responMention"] = True
                    cl.sendText(x.to, "AUTO RESPON ON")

                elif x.text in ["RESPON OFF"]:
                    settings["responMention"] = False
                    cl.sendText(x.to, "AUTO RESPON OFF")

                elif x.text in ["RESPON CHECK"]:
                    if message["replyPesan"] is not None:
                        cl.sendText(x.to,"My Set AutoRespon : " + str(message["replyPesan"]))
                    else:
                        cl.sendText(x.to,"My Set AutoRespon : No messages are set")

                elif "RESPON:" in x.text:
                    text = x.text.replace("RESPON:","")
                    try:
                        message["replyPesan"] = text
                        cl.sendText(x.to,"ok")
                    except:
                        cl.sendText(x.to,"Failed")
##############################################
                elif "mention" == x.text:
                    xname = cl.getProfile().displayName
                    xlen = str(len(xname)+1)
                    x.contentType = 0
                    x.text = "@"+xname+ ""
                    x.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                    cl.sendMessage(x)
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

# -*- coding: utf-8 -*-

import LAG
from LAG.lib.Gen.ttypes import *
from datetime import datetime
from LAG.lib.Gen.ttypes import *
from datetime import datetime
from LAPI.main import qr
from threading import Thread
import time,random,sys,re,os,json,subprocess,codecs,threading,glob,requests,string


acil = LAG.LINE()
acil.login(token=qr().get())
acil.loginResult()
#acil = LAG.LINE() 
#acil.login(token="your token here")
#acil.loginResult()

print "ログイン成功！"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""SRSU BOT v3

※： => :
※／ => /

/help >helpをだす
/version =>アップデート履歴・現在のバージョン

—test
/test =>動作確認
random =>ランダム動作確認
SRSU =>ランダム動作確認2

—restart
Reboot

—speed
/speed =>処理速度
/ns =>処理速度

—mid
/midk： =>midで蹴る
/midi： =>midで招待
/c： =>midから連絡先
/mid =>自分のmid
/mm： =>メンションした人

—other
/me =>自分の連絡先
/gift =>プレゼント
/block =>ブロックリスト
/ag =>グループリスト
／time =>現在時刻
／SPECIAL =>宣伝

—all mention
/tagall =>全員メンション
/all mention =>全員メンション

—name
/nc： =>名前変更
/gn： =>グループ名

—status
/sm： =>ステータス

—auto
/co：on / off =>連絡先情報
/j：on / off =>自動参加
/l：on / off =>自動退出
/s：on / off =>postURL
/a：on / off =>自動追加
/set =>設定確認

—group
/curl =>URL close
/ourl =>URL open
/gurl =>inviteURL
/ginfo =>グループ情報
/group info =>URL付き情報

—kick
/mk： =>メンションした人を蹴る
/nk： =>名前蹴り
／kickall =>破壊(クライアントのみで)
／group bye =>kickall(+SPECIAL)

—kicker join / leave

—lastseen
!set =>既読ポイント設定
!check =>既読確認

—search
/g： =>google検索
/yj： =>yahoo検索
/x： =>xvideos検索
/b： =>bing検索
/y： =>youtube検索
/ama： =>amazon検索
/t： =>twitter検索
/tid： =>twitterid検索(@不要)
/git： =>github検索
/gns： =>google news検索
/gm： =>googlemap検索
/r： =>楽天市場検索
/yw： =>yahoo天気・災害検索
/w： =>wikipedia検索
/gt： =>google翻訳(日本語➡︎英語)
/nn： =>niconico検索

—check
/cmt =>自分のトプ画確認
/cmc =>自分のカバー画像確認
/cmn =>自分の名前確認
/cms =>自分のステータス確認
/mcs： =>メンションした人のステータス
/mcn： =>メンションした人の名前確認
/mct： =>メンションした人のトプ画確認
/mcc： =>メンションした人のカバー画像確認
/myinfo =>自分の情報
/info： =>メンションした人の情報

creator↓
srsu.weebly.com"""

ver ="""7bot
srsu.weebly.com

v1 
QRログインに対応

v2  3/12
追加機能
現在時刻確認 ／time
メンションカバー画像確認 /mcc：
バージョン確認 /version
を追加

v3 3/13 (最新)
自分の情報を表示 /myinfo
メンションした人の情報を表示 /info：@
github検索 /git：
google news検索 /gns：
google map検索 /gm：
楽天市場検索 /r：
yahoo天気・防災検索 /yw：
wikipedia検索 /w：
google 翻訳 /gt：
niconico検索 /nn：
宣伝 ／SPECIAL
宣伝付き破壊 ／group bye
を追加"""

#検索用↓↓↓
#test =>テストコマンド
#restart =>再起動
#speed =>処理速度
#mid =>mid系コマンド
#other =>その他
#all mention =>全メンション
#name =>名前変更
#status =>ステータス変更
#auto =>自動
#group =>グループコマンド
#kick =>蹴りコマンド
#kicker join/leave =>キッカー参加 / 退出
#lastseen =>既読確認
#search =>検索
#check =>確認

KAC=[acil]
mid = acil.getProfile().mid
Bots=[mid]
Creator ="your mid here"
admsa ="your mid here"

wait = {
    'contact':False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":10},
    'leaveRoom':False,
    'timeline':True,
    'autoAdd':False,
    'message':"""srsu.weebly.com""",
    "lang":"JP",
    "comment1":"srsu.weebly.com",
    "comment":"Thanks For Add Me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "Autolike":True,
    "cName":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "copy":False,
    "copy2":"target",
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


contact = acil.getProfile()
backup = acil.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

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
        acil.sendMessage(msg)
    except Exception as error:
        print error

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = acil.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            acil.rejectGroupInvitation(op.param1)
                        else:
                            acil.acceptGroupInvitation(op.param1)
                    else:
                        acil.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        acil.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    acil.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                acil.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                acil.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "your_mid":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            acil.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = acil.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            acil.updateGroup(G)
                        except:
                            acil.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    acil.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                acil.like(url[25:58], url[66:], likeType=1001)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        acil.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        acil.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        acil.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        acil.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        acil.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        acil.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        acil.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        acil.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    acil.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = acil.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = acil.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        acil.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = acil.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = acil.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        acil.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "postURL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "_\n" + msg.contentMetadata["postEndUrl"]
                    acil.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == '/help':
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,helpMessage)
                else:
                    acil.sendText(msg.to,helpMessage)

            elif msg.text.lower() == '/version':
                if wait["lang"] == "JP":
                    acil.sendText(msg.to,ver)
                else:
                    acil.sendText(msg.to,ver)


#----------------------------------------------------------#test

#動作確認 test
            elif msg.text in ["test","/test"]:
                acil.sendText(msg.to,"ok")

#ランダムで送信2 SRSU
            elif msg.text in ["SRSU"]:
                acil.sendText(msg.to,"───ᶳᴿᶳᵁᴸᴵᶰᵉᴮᴼᵀˢ───")

#-------------------------------------------------------#Restart

#再起動 Reboot
	    elif msg.text in ["Update","Reboot"]:
		if msg.from_ in Creator:
		    acil.sendText(msg.to, "...")
		    restart_program()
		    print "@Restart"
		else:
		    acil.sendText(msg.to, "権限が無いよ")	
	    
#-----------------------------------------------#speed

#処理速度をだす /speed
            elif msg.text in ["/speed"]:
                start = time.time()
                acil.sendText(msg.to, "...")
                elapsed_time = time.time() - start
                acil.sendText(msg.to, "%s秒" % (elapsed_time))

#偽速度をだす /ns
            elif msg.text in ["/ns"]:
                acil.sendText(msg.to, "...")
                start = time.time()
                time.sleep(0.002)
                elapsed_time = time.time() - start
                acil.sendText(msg.to, "%ssec" % (elapsed_time)) 

#---------------------------------------------------#mid

#midで蹴る /midk:mid
            elif "/midk:" in msg.text:
                midd = msg.text.replace("/midk:","")
                acil.kickoutFromGroup(msg.to,[midd])

#midで招待する /midi:mid
            elif "/midi:" in msg.text:
                midd = msg.text.replace("/midi:","")
                acil.findAndAddContactsByMid(midd)
                acil.inviteIntoGroup(msg.to,[midd])

#midで連絡先を出す /c:mid
            elif "/c:" in msg.text:
                mmid = msg.text.replace("/c:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                acil.sendMessage(msg)

#自分のmidを送信 /mid
            elif "/mid" == msg.text:
                acil.sendText(msg.to,mid)

#メンションした人のmidを送信 /mm:@
            elif ("/mm:" in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = acil.getContact(key1)
                   acil.sendText(msg.to,key1)

#---------------------------------------------------#other

#自分の連絡先送信 /me
            elif "/me" == msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                acil.sendMessage(msg)

#プレゼント /gift
            elif msg.text in ["/gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '3'}
                msg.text = None
                acil.sendMessage(msg)
                msg.text = None
                pb2.sendMessage(msg)

#ブロックリスト確認 /block
            elif msg.text.lower() == '/block':
                blockedlist = acil.getBlockedContactIds()
                acil.sendText(msg.to, "...")
                kontak = acil.getContacts(blockedlist)
                num=1
                msgs="ブロックリスト\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\n計 %i 人のユーザーをブロックしています" % len(kontak)
                acil.sendText(msg.to, msgs)

#グループリスト /ag
            elif msg.text in ["/ag"]:
                 gid = acil.getGroupIdsJoined()
                 h = ""
                 for i in gid:
                  h += " %s \n" % (acil.getGroup(i).name + "|人数:" + str(len (acil.getGroup(i).members)))
                 acil.sendText(msg.to, "参加中のグループ\n"+ h +"合計:" +str(len(gid)))

#現在時刻確認 /time
            elif "/time" in msg.text:
                acil.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))

#宣伝 /SPECIAL
            elif "/SPECIAL" in msg.text:
                msg.contentType = 13
                c = "ub965db7580e876c9088646dc9e23820d" #main
                c2 = "u8deda100197101d96935d9faed3e3bca" #manjbot
                c3 = "u05282cb61a7ac8b879a3e43c6b88b8b7" 
                c4 = "uaa71757f0820e2ad366b3eb394656d2b" 
                c5 = "ua65f3983bdd87fff7b2235f41cd71edc" 
                c6 = "uff140ccaaa739556b51bb13dda5c7883" 
                c7 = "u1cb6076d7d046a98d9b66e0cdff18626" 
                msg.contentMetadata = {'mid': c}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c2}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c3}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c4}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c5}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c6}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c7}
                acil.sendMessage(msg)

#-------------------------------------------#all mention

#全員をメンション /tagall
            elif msg.text in ["/tagall"]:
                group = acil.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    acil.sendMessage(msg)
                except Exception as error:
                    print error

#全員をメンション(上が使えなかったらこっち) /allmention
            elif msg.text in ["/all mention"]:
                 group = acil.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "メンションした人数:\n" + str(jml) +  " 人"
                 cnt.to = msg.to
                 acil.sendMessage(cnt)

#--------------------------------------------------------#name

#名前変更 /nc:任意の名前
            elif "/nc:" in msg.text:
                string = msg.text.replace("/nc:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = acil.getProfile()
                    profile.displayName = string
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"名前を" + string + "に変更しました")

#グループ名変更 /gn:任意の名前
            elif ("/gn:" in msg.text):
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.name = msg.text.replace("/gn:","")
                    acil.updateGroup(group)
                else:
                    acil.sendText(msg.to,"ここでは使えないよ")

#--------------------------------------------------------#status

#ステータスメッセージ変更 /sm:任意
            elif "/sm:" in msg.text:
                string = msg.text.replace("/sm:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = acil.getProfile()
                    profile.statusMessage = string
                    acil.updateProfile(profile)
                    acil.sendText(msg.to,"ステータスメッセージを" + string + "に変更しました")

#--------------------------------------------------------#auto

#連絡先情報オン /co:on
            elif msg.text.lower() == '/co:on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on!")
                    else:
                        acil.sendText(msg.to,"on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on")
                    else:
                        acil.sendText(msg.to,"on")

#連絡先情報オフ /co:off
            elif msg.text.lower() == '/co:off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off!")
                    else:
                        acil.sendText(msg.to,"off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off")
                    else:
                        acil.sendText(msg.to,"off")

#自動参加オン /j:on
            elif msg.text.lower() == '/j:on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on!")
                    else:
                        acil.sendText(msg.to,"on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on")
                    else:
                        acil.sendText(msg.to,"on")

#自動参加オフ /j:off
            elif msg.text.lower() == '/j:off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off!")
                    else:
                        acil.sendText(msg.to,"off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off")
                    else:
                        acil.sendText(msg.to,"off")

#自動退出オン /l:on
            elif msg.text in ["/l:on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on!")
                    else:
                        acil.sendText(msg.to,"on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on")
                    else:
                        acil.sendText(msg.to,"on")

#自動退出オフ /l:off
            elif msg.text in ["/l:off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off!")
                    else:
                        acil.sendText(msg.to,"off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off")
                    else:
                        acil.sendText(msg.to,"off")

#postURLオン　自動スタ(?)オン /s:on
            elif msg.text in ["/s:on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on!")
                    else:
                        acil.sendText(msg.to,"on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on")
                    else:
                        acil.sendText(msg.to,"on")

#postURLオフ　自動スタ(?)オフ /s:off
            elif msg.text in ["/s:off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off!")
                    else:
                        acil.sendText(msg.to,"off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off")
                    else:
                        acil.sendText(msg.to,"off")

#自動追加オン /a:on
            elif msg.text in ["/a:on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on!")
                    else:
                        acil.sendText(msg.to,"on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"on")
                    else:
                        acil.sendText(msg.to,"on")

#自動追加オン /a:off
            elif msg.text in ["/a:off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off!")
                    else:
                        acil.sendText(msg.to,"off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"off")
                    else:
                        acil.sendText(msg.to,"off")

#設定確認 /set
            elif msg.text.lower() == '/set':
                md = ""
                if wait["contact"] == True: md+="連絡先情報:オン\n"
                else: md+="連絡先情報:オフ\n"
                if wait["autoJoin"] == True: md+="自動参加:オン\n"
                else: md +="自動参加:オフ\n"
                if wait["leaveRoom"] == True: md+="自動退出:オン\n"
                else: md+="自動退出:オフ\n"
                if wait["timeline"] == True: md+="シェア:オン\n"
                else:md+="シェア:オフ\n"
                if wait["autoAdd"] == True: md+="自動追加:オン\n"
                else:md+="自動追加:オフ\n"
                acil.sendText(msg.to,md)

#---------------------------------------------------#group

#urlを閉じる(招待URL拒否) /curl
            elif msg.text in ["/curl"]:
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    acil.updateGroup(group)
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"close")
                    else:
                        acil.sendText(msg.to,"close")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"ここでは使えないよ")
                    else:
                        acil.sendText(msg.to,"ここでは使えないよ")

#URLを開ける(招待URL許可) /ourl
            elif msg.text in ["/ourl"]:
                if msg.toType == 2:
                    group = acil.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    acil.updateGroup(group)
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"open")
                    else:
                        acil.sendText(msg.to,"open")
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"ここでは使えないよ")
                    else:
                        acil.sendText(msg.to,"ここでは使えないよ")

#URLをつくる(招待URL生成) /gurl
            elif msg.text in ["/gurl"]:
                if msg.toType == 2:
                    g = acil.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        acil.updateGroup(g)
                    gurl = acil.reissueGroupTicket(msg.to)
                    acil.sendText(msg.to,"参加URL↓\nhttp://line.me/R/ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        acil.sendText(msg.to,"ここでは使えないよ")
                    else:
                        acil.sendText(msg.to,"ここでは使えないよ")

#グループ情報を送信 /ginfo
            elif "/ginfo" == msg.text:
              if msg.toType == 2:
#                if msg.from_ in admin:
                  ginfo = acil.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    acil.sendText(msg.to,"[グループ名]\n" + "・" + str(ginfo.name) + "\n\n[gid]\n" + msg.to + "\n\n[作成者]\n" + "・" + gCreator + "\n\n[URL]\n" + "・URL👉" + QR + "\n\n[グループ画像]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n人数:" + str(len(ginfo.members)) + "\n招待数:" + sinvitee)
                  else:
                    acil.sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
#                else:
                  if wait["lang"] == "JP":
                    acil.sendText(msg.to,"")
                  else:
                    acil.sendText(msg.to,"むり")

#グループ情報(URL付き) /group info
            elif msg.text in ["/group info"]:
                group = acil.getGroup(msg.to)
                try:
                    gCreator = group.creator.displayName
                except:
                    gCreator = "不明"
                if group.invitee is None:
                    gPending = "0"
                else:
                    gPending = str(len(group.invitee))
                if group.preventJoinByTicket == True:
                    gQr = "拒否してるよ"
                    gTicket = "拒否されているよ"
                else:
                    gQr = "許可してるよ"
                    gTicket = "https://line.me/R/ti/g/{}".format(str(acil.reissueGroupTicket(group.id)))
                ret_ = "Group info"
                ret_ += "\nグループ名 : {}".format(group.name)
                ret_ += "\ngid : {}".format(group.id)
                ret_ += "\n作成者 : {}".format(gCreator)
                ret_ += "\nメンバー : {}".format(str(len(group.members)))
                ret_ += "\n招待数 : {}".format(gPending)
                ret_ += "\nURL : {}".format(gQr)
                ret_ += "\n招待URL : {}".format(gTicket)
                acil.sendText(msg.to, str(ret_))
                acil.sendText(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)

#-----------------------------------------------------------#kick

#メンションキック(クライアントのみ) /mk:@
            elif ("/mk:" in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"][0]["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           acil.kickoutFromGroup(msg.to,[target])
                       except:
                           acil.sendText(msg.to,"Error")

#名前で蹴る /nk:
            elif "/nk:" in msg.text:
                    X = acil.getGroup(msg.to)
                    acil.updateGroup(X)
                    invsend = 0
                    G = acil.getGroup(msg.to)
                    acil.updateGroup(G)

                    nk0 = msg.text.replace("/nk:","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3

                    targets = []
                    for s in X.members:
                        if _name in s.displayName:
                            targets.append(s.mid)
                    if targets == []:
                        sendMessage(msg.to,"not found")
                        pass
                    else:
                        for target in targets:
                                acil.kickoutFromGroup(msg.to,[target])


#クライアントのみで破壊 /kickall
            elif "/kickall" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("/kickall","")
                    gs = acil.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        acil.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if not target in admsa:
                            try:
                                acil.kickoutFromGroup(msg.to,[target])
                            except:
                                acil.sendText(msg.to,"ok")

#連絡先出した後破壊 /group bye
            elif "/group bye" in msg.text:
                msg.contentType = 13
                c = "ub965db7580e876c9088646dc9e23820d" #main
                c2 = "u8deda100197101d96935d9faed3e3bca" #manjbot
                c3 = "u05282cb61a7ac8b879a3e43c6b88b8b7" 
                c4 = "uaa71757f0820e2ad366b3eb394656d2b" 
                c5 = "ua65f3983bdd87fff7b2235f41cd71edc" 
                c6 = "uff140ccaaa739556b51bb13dda5c7883" 
                c7 = "u1cb6076d7d046a98d9b66e0cdff18626" 
                msg.contentMetadata = {'mid': c}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c2}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c3}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c4}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c5}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c6}
                acil.sendMessage(msg)
                msg.contentMetadata = {'mid': c7}
                acil.sendMessage(msg)
                acil.sendText(msg.to,"srsu.weebly.com")
                if msg.toType == 2:
                    _name = msg.text.replace("/group bye","")
                    gs = acil.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = ki2.getGroup(msg.to)
                    gs = ki3.getGroup(msg.to)
                    gs = ki4.getGroup(msg.to)
                    gs = ki5.getGroup(msg.to)
                    gs = ki6.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        acil.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if not target in admsa:
                            try:
                               acil.kickoutFromGroup(msg.to,[target])
                            except:
                                acil.sendText(msg.to,"ok")

#--------------------------------------------------------#kicker join/leave
#-------------------------------------------------------------------------------#lastseen

#既読ポイント設定 !set
            elif msg.text == "!set":
                    acil.sendText(msg.to, "既読ポイントを設定しました。確認したい場合は「!check」と送信してください。")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                    wait2['ROM'][msg.to] = {}
                    print wait2

#既読ポイント設定 !check
            elif msg.text == "!check":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        acil.sendText(msg.to,"以下のユーザーが既読しています %s\n既読無視しているユーザー\n%s\n設定時刻:\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                         acil.sendText(msg.to,"既読ポイントが設定されていません。「!set」と送信して既読ポイントを設定してください")

#-------------------------------------------------------#search

#google検索 /g:検索内容
            elif "/g:" in msg.text:
                s = msg.text.replace("/g:","")
                acil.sendText(msg.to,"https://www.google.com/search?q=" + s.replace("/g:",""))

#yahoo検索 /yj:検索内容
            elif "/yj:" in msg.text:
                s = msg.text.replace("/yj:","")
                acil.sendText(msg.to,"http://search.yahoo.co.jp/search?p=" + s.replace("/yj:",""))

#xvideos検索 /x:検索内容
            elif "/x:" in msg.text:
                s = msg.text.replace("/x:","")
                acil.sendText(msg.to,"https://www.xvideos.com/?k=" + s.replace("/x:",""))

#bing検索 /b:検索内容
            elif "/b:" in msg.text:
                s = msg.text.replace("/b:","")
                acil.sendText(msg.to,"https://www.bing.com/search?q=" + s.replace("/b:",""))

#twitterid検索 /tid:twitterid
            elif "/tid:" in msg.text:
                s = msg.text.replace("/tid:","")
                acil.sendText(msg.to,"https://twitter.com/" + s.replace("/tid:",""))

#twitter検索 /t:検索内容
            elif "/t:" in msg.text:
                s = msg.text.replace("/t:","")
                acil.sendText(msg.to,"https://twitter.com/search?q=" + s.replace("/t:",""))

#youtube検索 /y:検索内容
            elif "/y:" in msg.text:
                s = msg.text.replace("/y:","")
                acil.sendText(msg.to,"https://www.youtube.com/results?search_query=" + s.replace("/y:",""))

#amazon検索 /ama:検索内容
            elif "/ama:" in msg.text:
                s = msg.text.replace("/ama:","")
                acil.sendText(msg.to,"https://www.amazon.co.jp/s/?keywords=" + s.replace("/ama:",""))

#github検索 /git:検索内容
            elif "/git:" in msg.text:
                s = msg.text.replace("/git:","")
                acil.sendText(msg.to,"https://github.com/search?utf8=✓&q=" + s.replace("/git:",""))

#google news検索 /gns:検索内容
            elif "/gns:" in msg.text:
                s = msg.text.replace("/gns:","")
                acil.sendText(msg.to,"https://news.google.com/news/search/section/q/" + s.replace("/gns:",""))

#yahoo news検索 /yn:検索内容
            elif "/yn:" in msg.text:
                s = msg.text.replace("/yn:","")
                acil.sendText(msg.to,"https://news.yahoo.co.jp/search/?p=" + s.replace("/yn:",""))

#google map検索 /gm:検索内容
            elif "/gm:" in msg.text:
                s = msg.text.replace("/gm:","")
                acil.sendText(msg.to,"https://www.google.co.jp/maps/search/" + s.replace("/gm:",""))

#楽天市場検索 /r:検索内容
            elif "/r:" in msg.text:
                s = msg.text.replace("/r:","")
                acil.sendText(msg.to,"https://search.rakuten.co.jp/search/mall/" + s.replace("/r:",""))

#yahoo天気・災害 /yw:検索内容
            elif "/yw:" in msg.text:
                s = msg.text.replace("/yw:","")
                acil.sendText(msg.to,"https://weather.yahoo.co.jp/weather/search/?p=" + s.replace("/yw:",""))

#wiki検索 /w:検索内容
            elif "/w:" in msg.text:
                s = msg.text.replace("/w:","")
                acil.sendText(msg.to,"https://ja.wikipedia.org/wiki/" + s.replace("/w:",""))

#google翻訳 /gt:翻訳内容
            elif "/gt:" in msg.text:
                s = msg.text.replace("/gt:","")
                acil.sendText(msg.to,"https://translate.google.co.jp/?hl=ja#ja/en/" + s.replace("/gt:",""))

#niconico検索 /nn:検索内容
            elif "/nn:" in msg.text:
                s = msg.text.replace("/nn:","")
                acil.sendText(msg.to,"http://www.nicovideo.jp/search/" + s.replace("/nn:",""))

#---------------------------------------------------------------#check

#自分のトプ画確認 /cmt
            elif msg.text in ["/cmt"]:
                    me = acil.getContact(mid)
                    acil.sendText(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)

#自分のカバー画像確認 /cmc
            elif msg.text in ["/cmc"]:
                    me = acil.getContact(mid)
                    cover = acil.channel.getCover(mid)          
                    path = str(cover)
                    acil.sendText(msg.to, path)

#自分の名前確認 /cmn
            elif msg.text in ["/cmn"]:
                    me = acil.getContact(mid)
                    acil.sendText(msg.to,"[DisplayName]\n" + me.displayName)

#自分のステータス確認 /cms
            elif msg.text in ["/cms"]:
                    me = acil.getContact(mid)
                    acil.sendText(msg.to,"[StatusMessage]\n" + me.statusMessage)

#メンションした人のステータス確認 /mcs:@
            elif ("/mcs:" in msg.text):
                mention = eval(msg.contentMetadata["MENTION"])
                mention1 = mention["MENTIONEES"][0]["M"]
                contact = acil.getContact(mention1)
                try:
                    acil.sendText(msg.to, "[StatusMessage]\n" + contact.displayName)
                except:
                    pass

#メンションした人の名前確認 /mcn:@
            elif ("/mcn:" in msg.text):
                mention = eval(msg.contentMetadata["MENTION"])
                mention1 = mention["MENTIONEES"][0]["M"]
                contact = acil.getContact(mention1)
                try:
                    acil.sendText(msg.to, "[DisplayName]\n" + contact.displayName)
                except:
                    pass

#メンションした人のトプ画確認 /mct:@
            elif ("/mct:" in msg.text):
                mention = eval(msg.contentMetadata["MENTION"])
                mention1 = mention["MENTIONEES"][0]["M"]
                contact = acil.getContact(mention1)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    acil.sendText(msg.to,image)
                except:
                    pass

#メンションした人のカバー画像確認 /mcc:@
            elif "/mcc:" in msg.text:          
                mention = eval(msg.contentMetadata["MENTION"])
                mention1 = mention["MENTIONEES"][0]["M"]
                gs = acil.getGroup(msg.to)
                me = acil.getContact(mention1)
                cover = acil.channel.getCover(mention1)          
                path = str(cover)
                try:
                    acil.sendText(msg.to, path)
                except:
                    pass

#自分の情報 /myinfo
            elif msg.text in ["/myinfo"]:
                    me = acil.getContact(mid)
                    cu = acil.channel.getCover(mid)
                    acil.sendText(msg.to,"[mid]\n" + mid + "\n" + "\n" +"[DisplayName]\n" +  me.displayName + "\n" + "\n" + "[StatusMessage]\n" + me.statusMessage + "\n" + "\n" + "[pictureStatus]\n" + "http://dl.profile.line-cdn.net/" + me.pictureStatus + "\n" + "\n" + "[coverURL]\n" + str(cu))

#メンションした人の情報 /info:@
            elif ("/info:" in msg.text):
                mention = eval(msg.contentMetadata["MENTION"])
                mention1 = mention["MENTIONEES"][0]["M"]
                contact = acil.getContact(mention1)
                cu = acil.channel.getCover(mention1)
                try:
                    acil.sendText(msg.to,"[mid]\n" + mention1 + "\n" + "\n" +"[DisplayName]\n" +  contact.displayName + "\n" + "\n" + "[StatusMessage]\n" + contact.statusMessage + "\n" + "\n" + "[pictureStatus]\n" + "http://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n" + "\n" + "[coverURL]\n" + str(cu))
                except:
                    pass

#------------------------------------
#------------------------------------
        if op.type == 55:
            if op.param1 in wait2['readPoint']:
                Name = acil.getContact(op.param2).displayName
                if Name in wait2['readMember'][op.param1]:
                    pass
                else:
                    wait2['readMember'][op.param1] += "\n・" + Name
                    wait2['ROM'][op.param1][op.param2] = "・" + Name
            else:
                acil.sendText

        if op.type == 59:
            print op


    except Exception as error:
        print error

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = acil.getProfile()
                profile.displayName = wait["cName"] + nowT
                acil.updateProfile(profile)
            time.sleep(0.30)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = acil.fetchOps(acil.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(acil.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            acil.Poll.rev = max(acil.Poll.rev, Op.revision)
            bot(Op)



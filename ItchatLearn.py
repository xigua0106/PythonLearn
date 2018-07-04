import requests
import itchat,time,xlwt

file = xlwt.Workbook()
table = file.add_sheet('info', cell_overwrite_ok=True)

#自动登录 -- 命令行二维码
itchat.auto_login(hotReload=True, enableCmdQR=True)
itchat.dump_login_status()

'''
# 获取收到信息，向API发送请求
@itchat.msg_register(itchat.content.TEXT)
def get_response(msg):
    print(msg)
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '71f28bf79c820df10d39b4074345ef8c',  # 如果这个Tuling Key不能用，那就换一个
        'info': msg,            # 这是我们发出去的消息
        'userid': 'wechat-robot',   # 这里你想改什么都可以
    }
    # print(msg['Text'])
    try:
        r = requests.post(apiUrl, data=data).json()
        print(r)
        # 字典的get方法在字典没有'text'值的时候会返回None而不会抛出异常
        return r.get('text')
    except Exception as e:
        print("[Error]", str(e))
        return

# 回复
@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'I received: ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = get_response(msg['Text'])
    return reply or defaultReply
    
#因为popen实现机制问题无法使用cd命令

#使用-download 文件名 命令来下载指定文件
@itchat.msg_register([itchat.content.TEXT])#注册文本消息回复
def text_reply(msg):
    if msg['Text'] == '-authority':
        itchat.send(msg["FromUserName"], msg['FromUserName'])
    elif msg["FromUserName"] in authority.permissionUserName:
        print('permit')
        if msg['Text'].split(" ")[0] == '-download':#下载文件指令
            itchat.send_file(msg['Text'].split(' ')[1], msg['FromUserName'])
        elif msg['Text'].split(" ")[0] == 'cd':#拦截cd命令通过os.chdir来实现目录切换
            os.chdir(msg['Text'].split(' ')[1])
        else:
            with os.popen(msg['Text']) as cmd:#普通指令
                itchat.send(cmd.read(), msg["FromUserName"])

@itchat.msg_register([itchat.content.ATTACHMENT, itchat.content.PICTURE, itchat.content.RECORDING, itchat.content.VIDEO])
def download_files(msg):#接收到文件图片语音视频时将其存到本地
    if msg['FromUserName'] in authority.permissionUserName:
        print(msg["Text"])
        with open(msg["FileName"], 'wb') as f:
            f.write(msg["Text"]())

'''

# author = itchat.search_friends(nickName='LittleCoder')[0]
# itchat.search_friends(name='曾志伟')
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
print(friends)
male = female = other = 0

for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

table.write(0, 5, u'【made by junzi】')
table.write(0, 7, u'【共'+str(len(friends)-1)+u'位朋友，'+str(male)+u'位男性朋友，'+str(female)+u'位女性朋友，另外'+str(other)+u'位不明性别】')
table.write(0, 0, u' 【昵称】')
table.write(0, 1, u' 【备注名】')
table.write(0, 2, u' 【省份】')
table.write(0, 3, u' 【城市】')
table.write(0, 4, u' 【签名】')

a = 0
for i in friends:
    table.write(a+1, 0, i['NickName'])
    table.write(a+1, 1, i['RemarkName'])
    table.write(a+1, 2, i['Province'])
    table.write(a+1, 3, i['City'])
    table.write(a+1, 4, i['Signature'])
    if i['RemarkName'] == u'':
        table.write(a+1,1,u'[ ]')
    if i['Province'] == u'':
        table.write(a+1,2,u'[ ]')
    if i['City'] == u'':
        table.write(a+1,3,u'[ ]')
    if i['Signature'] == u'':
        table.write(a+1,4,u'[ ]')
    a = a+1

file_name = 'weixin_'+time.strftime("%Y%m%d", time.localtime())+'.xls'
file.save(file_name)
# itchat.send('made by junzi', 'filehelper')
# itchat.send('@%s@%s' % ('fil', file_name), 'filehelper')
print("over")

# 给文件传输助手发送消息
# itchat.send(u'测试消息发送', 'filehelper')

# 自动回复
# itchat.run(debug=True)


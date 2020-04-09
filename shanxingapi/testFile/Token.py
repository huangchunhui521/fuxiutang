
from shanxingapi import *

class Token(object):

    def __init__(self):
        self.host = conf.get("Master", "host")
        self.login_random = ''

    def sq(self):
        # 法师登录验证码授权
        url = self.host + conf.get("Master", "grant_authorization")
        print('url:'+url)
        # 接口参数
        phone="15818650805",
        verifiable_code="123456"
        data = json.dumps({"phone": phone, "verifiable_code": verifiable_code})
        print('data:' + data)
        try:
            # 对接口发送请求
            ret = requests.post(url=url,  data=data)
            # 把返回结果转换成json格式
            ret_json=ret.json()
            if ret_json['code']==0:
                self.login_random = ret.json()['data']['login_random']
                print(' self.login_random:'+ self.login_random)
                log.info("success")
            else:
                log.warning("warning，response：%s" % ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    def login_fs(self):
        # 登录法师端获取token
        url=self.host+conf.get('Master','login_Master')
        print('url:' + url)
        # 接口参数
        login_random=self.login_random
        phone='15818650805'
        data = json.dumps({"phone": phone, "login_random": login_random})
        try:
            # 对接口发送请求
            ret = requests.post(url=url,data=data)
            # 把返回结果转换成json格式
            ret_json = ret.json()
            if ret_json["code"] == 0:
                self.token = ret.json()['data']['token']
                print('self.token:'+self.token)
                log.info("success")
                return ret
            else:
                log.warning("warning，response：%s" % ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


token=Token()
sq=token.sq()
# token_fs=token.login_fs()








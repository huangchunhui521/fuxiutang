from shanxingapi import *
import unittest

try:
    conf.get("Master", "host")
except Exception as msg:
    log.error("请检查配置文件是否正确:%s" % msg)



class Token(unittest.TestCase):

    def grant_authorization(self, phone, code):
        # 法师登录验证码授权
        self.host = conf.get("Master", "host")
        url = self.host + conf.get("Master", "grant_authorization")
        print('url:' + url)
        # 接口参数
        data = json.dumps({"phone": phone, "verifiable_code": code})
        print('data:' + data)
        try:
            # 对接口发送请求
            ret = requests.post(url=url, data=data)
            # 把返回结果转换成json格式
            ret_json = ret.json()
            if ret_json['code'] == 0:
                self.login_random = ret.json()['data']['login_random']
                print(' self.login_random:' + self.login_random)
                log.info("success")
            else:
                log.warning("warning，response：%s" % ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False


    def login_Master(self,phone):
        """法师登录接口"""
        fs_url=self.host+conf.get('Master','login_Master')
        print('fs_url:'+fs_url)
        print("login_random:" + self.login_random)
        # 接口参数
        # 获取login_random
        login_random=self.login_random
        data = json.dumps({"phone": phone, "login_random": login_random})
        print('data:'+data)
        try:
            # 对接口发送请求
            ret = requests.post(url=fs_url, data=data)
            # 把返回结果转换成json格式
            ret_json = ret.json()
            if ret_json["code"]==0:
                token=ret.json()['data']['token']
                print('self.token:'+token)
                log.info("success")
                return token
            else:
                log.warning("warning，response：%s" % ret_json)
                return False

        except Exception as msgs:
            log.error("error, %s" % msgs)
            return False

# t=Token()
# token=t.login_Master()
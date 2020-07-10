# -*- coding: utf-8 -*-

# @File:接口依赖
# @Time :
# @Author :
# @Detail : 善行
import json

case=None
new_data=None
case_logger=None
do_re=None
res=None
def test1():
    """请求体的字段依赖"""
    if case["check_info"]=='user_info':
        user_name=json.loads(new_data)['name']
        case_logger.info("{:-^50s}".format(f"user_name:{user_name}"))
        setattr(do_re,'user_name',user_name)

def test2():
    """响应体的字段依赖"""
    if case["check_info"]=='get_op_svc_servicestage_domainId':
        op_svc_servicestage_domainId=res.json()['user']['domain']['id']
        case_logger.info("{:-^50s}".format(f"op_svc_servicestage_domainId:{op_svc_servicestage_domainId}"))
        setattr(do_re,'op_svc_servicestage_domainId',op_svc_servicestage_domainId)
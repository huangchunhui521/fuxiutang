# -*- coding: utf-8 -*-

# @File:
# @Time :
# @Author :
# @Detail : 善行




a={"code":0}

b={"code":1,"body":22}

aa=set(a.items())
bb=set(b.items())

print(aa.issubset(b.items()))
print(aa.issubset(bb))
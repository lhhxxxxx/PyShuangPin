# PyShuangPin

汉字转双拼工具

## 使用方法

```python
# from samply.py

from pyshuangpin import *

hans = 'xcw的脚，软软的、香香的'
print(hans)
sp = shuangpin(hans, mode="xiaohe", style=Style.NORMAL)
print(sp)
sp = shuangpin(hans, mode="小鹤", style=Style.NORMAL)
print(sp)
sp = shuangpin(hans, mode="xiaohe", style=Style.TONE)
print(sp)
sp = shuangpin(hans, mode="xiaohe", style=Style.INITIALS)
print(sp)
sp = shuangpin(hans, mode="xiaohe", style=Style.FINALS)
print(sp)
sp = shuangpin(hans, mode="xiaohe", style=Style.FINALS_TONE)
print(sp)
sp = lazy_shuangpin(hans, mode="xiaohe", style=Style.NORMAL)
print(sp)
```
其中，``mode``参数可以是以下几种（参阅 [可扩展性](#可扩展性)）：
* ``"xiaohe"``、``"小鹤"``：小鹤双拼，默认模式

``style``参数可以是以下几种：
* ``Style.NORMAL``：普通样式，默认模式
* ``Style.TONE``：带声调样式
* ``Style.INITIALS``：仅声母样式
* ``Style.FINALS``：仅韵母样式
* ``Style.FINALS_TONE``：带声调的韵母样式

``shuangpin``还具有参数``heteronym``，可以指定是否返回多音字的双拼，默认为``False``，即不返回多音字的双拼。

``lazy_shuangpin``还具有参数``tone_sandhi``，可以指定是否返回带变调的双拼，默认为``False``，即不返回带变调的双拼。

## 可扩展性
在``pyshaungpin.modules``文件夹下可添加自己的模块，并使用以下装饰器注册：

* ``@finals_register.register``注册韵母字典，可使用``@finals_register.register(name:str)``修改注册名（默认函数名），可以多次注册。
* ``@initials_register.register``注册声母字典，可使用``@initials_register.register(name:str)``修改注册名（默认函数名），可以多次注册。
* ``@zero_initial_finals_register.register``注册零声母韵母字典，可使用``@zero_initial_finals_register.register(name:str)``修改注册名（默认函数名），可以多次注册。

注册后将``mode``参数设为注册名，即可使用。

## 鸣谢

[pypinyin库](https://pypi.org/project/pypinyin/)

思路来源 [@MistEO](@MistEO) [python-shuangpin](https://github.com/MistEO/python-shuangpin)

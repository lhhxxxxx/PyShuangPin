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

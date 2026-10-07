import sys
from datetime import datetime

sys.set_int_max_str_digits(1000000000)

now = datetime.now()
t_int = int(now.strftime("%H"))*60*60 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))

num = 2**100000000
print(num)

now = datetime.now()
t = int(now.strftime("%H"))*60*60 + int(now.strftime("%M"))*60 + int(now.strftime("%S"))

print("time spent in seconds:", t-t_int)

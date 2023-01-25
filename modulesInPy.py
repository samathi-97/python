import time as t

print(t.localtime())

print(t.time()) 
print(t.time()) 

time_now = t.time()
delivary_date = time_now + (86400 * 7)
print("delivary date :",delivary_date)
print (t.localtime(delivary_date))
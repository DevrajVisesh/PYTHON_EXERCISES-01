#Program to print the longest string
def longest_string(s):
   a = s.split(" ")
   max=0
   for i in a:
    l = len(i)
    if l > max:
       max = l
   for i in a:
    if len(i) == max:
     print(i)

longest_string ("Shape of you Xp")

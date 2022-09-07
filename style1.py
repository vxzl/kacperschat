import random as r
import time as t

def style(charNum, minInc, maxInc, minPause, maxPause):
  percent = 0
  charDiv = 100 / charNum
  char = "-"
  
  while percent < 100:
    percent = percent + r.randint(minInc, maxInc)
    
    if percent > 100:
      percent = 100
      
    for i in range(round(percent/charDiv)):
      print(char, end="")
    print(str(percent) + "%", end="")
    for i in range(round(charNum - percent/charDiv)):
      print(char, end="")
      
    print(end="\r")
    t.sleep(r.randint(minPause, maxPause)/10)
  print()
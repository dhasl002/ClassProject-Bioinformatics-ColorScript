import Midas
import sys
colors = ["tan", "sienna", "brown", "salmon", "red", "sandy brown", "orange red", "orange", "goldenrod", "gold", "yellow", "khaki", "dark khaki", "dark olive green", "olive drab", "chartreuse", "green", "dark green", "dark cyan", "light sea green", "aquamarine", "cyan", "deep sky blue", "steel blue", "sky blue", "blue", "medium blue", "navy blue", "medium purple", "purple", "plum", "orchid", "magenta", "dark magenta", "hot pink", "deep pink", "slate gray", "dark slate gray", "white"]
#39 colors

AAList = []

#path = "C:/Users/dhaslam/Downloads/274635.all_in_one/274635.all_in_one/274635.contactmap.txt"
path = sys.argv[1]

it = 0
i = 0
breakVar = 0
noRepeat = int(sys.argv[2])

with open(path) as inf:
  for line in inf:
    AA1, AA2, trash1, trash2, trash3 = line.strip().split(",")
    next(inf)
    
    if it == 38:
      break
    
    if float(trash3) < float(sys.argv[3]):
      break
    
    if noRepeat == 1:
      for i in range (0,len(AAList)):
        if AA1 == AAList[i] or AA2 == AAList[i]:
          breakVar = 1
      
      if breakVar == 1:
        break
    Midas.color(colors[it], sel=':' + str(AA1))
    Midas.color(colors[it], sel=':' + str(AA2))
    it = it + 1
    AAList.append(AA1)
    AAList.append(AA2)
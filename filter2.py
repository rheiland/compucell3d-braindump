fp = open('index2b.html')
for line in fp:
    idx = line.find("title") 
    if idx >= 0:
      print line[:idx-2] + '.html"',
      print line[idx-1:],
#      print ' ------- idx=',idx
    else:
      print line,

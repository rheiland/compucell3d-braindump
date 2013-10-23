fp = open('index2.html')
for line in fp:
    if line.find("/mediawiki1.7/index.php/") >= 0:
      l2 = line.replace("/mediawiki1.7/index.php/","")
      print l2,
    else:
      print line,

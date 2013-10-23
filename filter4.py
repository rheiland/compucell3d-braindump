import glob

fcount = 0
#for filename in ['old/Cells_in_3D.html']:
#for filename in ['old/Wound_model.html']:
#for filename in ['old/TST.html']:
#for filename in ['html/Wound_model.html']:
for filename in glob.iglob('html/*.html'):
  print fcount, ') ----------------------- ',filename
  if filename.find("index")  > 0:
    continue
  fp = open(filename)
  fpout = open("new/"+filename[5:], "w")
  lcount = 0

  for line in fp:
    lcount += 1
    if line.find('src="images')  > 0:
      idx = line.find('src="images')
      s = line[:idx+5] + "../" + line[idx+5:]
      s2 = s[idx+5:]
      if s2.find('src="images')  > 0:
        print '------------ waaaaaah - found another img'
      fpout.write(s)
    else:
#      print line,
      fpout.write(line)

  fp.close()
  fpout.close()
  fcount += 1
  if fcount > 1000:
    break;

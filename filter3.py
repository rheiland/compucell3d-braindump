import glob

fcount = 0
#for filename in ['old/Cells_in_3D.html']:
#for filename in ['old/Wound_model.html']:
#for filename in ['old/TST.html']:
for filename in ['old/Hex_Lattice.html']:
#for filename in glob.iglob('old/*.html'):
  print fcount, ') ----------------------- ',filename
  if filename.find("index")  > 0:
    continue
  fp = open(filename)
  fpout = open("new/"+filename[4:], "w")
  fpout.write( '<html><body>\n')
  lcount = 0

  for line in fp:
    lcount += 1
    if lcount < 30:
      continue
    elif lcount == 30:
      fpout.write( line)
    elif lcount < 35:
      continue
    elif line.find("<img src")  > 0:
      idx = line.find("<img src")
      s = "<p>" + line[idx:-5]
      idx2 = s.find('="')
      idx3 = s.find('/')
      s2 = s[:idx2+2] + "images" + s[idx3:]
#      fpout.write( "<p>"+line[idx:-5])
      fpout.write(s2)
    elif line.find("Back to")  > 0:
      fpout.write( '<li>Back to <a href="index.html">index</a>')
      fpout.write( '</body></html>')
      break
    elif line.find("Saved in parser")  > 0:
      fpout.write( '<li>Back to <a href="index.html">index</a>')
      fpout.write( '</body></html>')
      break

#    idx = line.find("title") 
#      print ' ------- idx=',idx
    else:
#      print line,
      fpout.write(line)

  fp.close()
  fpout.close()
  fcount += 1
  if fcount > 1000:
    break;

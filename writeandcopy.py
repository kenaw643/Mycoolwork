filename=input('enter file name')
orgFile=open(filename+".txt",'r+')

filename2=input('enter file name to copy')
copyfile=open(filename2,'w')
data=orgFile.read()
copyfile.write(data)
copyfile.read(data)
f.flush()
f.close()

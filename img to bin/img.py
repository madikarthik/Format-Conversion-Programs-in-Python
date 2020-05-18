import base64
 
with open("t.png", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    print (str)
fi = open("bini.txt","wb")
fi.write(str)
fi.close()

fh = open("imageToSave.png", "wb")
fh.write(str.decode('base64'))
# for py 2.7 decode()
#for py 3.x fh.write(base64.decodebytes(imgdata))
fh.close()

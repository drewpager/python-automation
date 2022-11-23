import shutil, os
lis=[]
i=1
# destinationdir='/Users/drewpage/Desktop/Everything'
# while os.path.exists(destinationdir):
#     destinationdir+=str(i)
#     i+=1
# os.makedirs(destinationdir)

lis=('/Users/drewpage/Desktop/')
for x in lis:
    y = open(x)
    if (os.path.isfile(y)):
        print(y)
        continue
    # shutil.move(x,destinationdir)

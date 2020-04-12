import cv2
import numpy as np

from SimpleCV import *
import SimpleCV
import random
import PIL
import time
def findcoord(index):
    minx=5000
    maxx=-1000
    miny=5000
    maxy=-1000
    for i in range(len(contours[index])):
        if minx>contours[index][i][0][0]:
            minx=contours[index][i][0][0]
        if maxx<contours[index][i][0][0]:
            maxx=contours[index][i][0][0]
        if miny>contours[index][i][0][1]:
            miny=contours[index][i][0][1]
        if maxy<contours[index][i][0][1]:
            maxy=contours[index][i][0][1]
    temp=[]
    temp.append(miny)
    temp.append(maxy)
    temp.append(minx)
    temp.append(maxx)
    return temp
def drawrectangles(coord,dupimg,index,name): 
   
    x=coord[index][2]
    y=coord[index][0]
    w=coord[index][3]-coord[index][2]
    h=coord[index][1]-coord[index][0]
    if name=='windows':
        cv2.rectangle(dupimg, (x, y), (x + w, y + h), (0, 255, 0), 2)
    else:
        cv2.rectangle(dupimg, (x, y), (x + w, y + h), (255, 0, 0), 2)
#height=raw_input('Enter building\'s height')
fname=raw_input('Enter file name: ')
img = cv2.imread(fname+".jpg")
dupimg= cv2.imread(fname+".jpg")
dupimg1= cv2.imread(fname+".jpg")


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,5),0)
edges = cv2.Canny(blur,100,200)
drawing = np.zeros(img.shape,np.uint8)  
contours, hierarchy = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

coord=[]
indexes=0
for j in range(len(contours)):
    if len(contours[j])<4:
        continue
    else:
        points=findcoord(j)
    
        cropped=dupimg[points[0]:points[1], points[2]:points[3]]
        x,y,z=cropped.shape
        if x>=10 and y>=10 and x<=120 and y<=120:
            name='./windows/test/crop'
            name+=str(indexes)
            indexes=indexes+1
            name+='.jpg'
            coord.append(points)
            cv2.imwrite(name, cropped)

hhfe=HueHistogramFeatureExtractor()
ehfe=EdgeHistogramFeatureExtractor()
extractor=[hhfe,ehfe]
tree=TreeClassifier (extractor)
trainPaths=['./training/window set/','./training/other set/']
testPaths=['./test/']
classes=['windows','other']
tree.train(trainPaths,classes,verbose=True)
test=ImageSet()
for p in testPaths:
    test+=ImageSet(p)



answer=0
for t in test:
    className=tree.classify(t)
    #t.drawText(className,10,10,fontsize=60,color=Color.RED)
    #t.show()
    if className=='':
        fname=t.filename
        x=fname.find('crop')+4
        y=fname.rfind('.')
        index=int(fname[x:y])
        print index,' ',coord[index]
        drawrectangles(coord,dupimg,index,className)
        answer=answer+1
    #time.sleep(2.1)]
cv2.imwrite('hometest.jpg',dupimg)
cv2.imshow('Original',dupimg1)
cv2.imshow('Result',dupimg)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()


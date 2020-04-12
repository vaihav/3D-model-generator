import os
import math
def newcoord(lat1,long1,lat2,long2):
    
    #return (math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1) )) 
    r=6371
    lat1=math.radians (lat1)
    lat2=math.radians (lat2)
    long1=math.radians (long1)
    long2=math.radians (long2)

    x1=r*math.cos(lat1)*math.cos(long1)*1000
    y1=r*math.cos(lat1)*math.sin(long1)*1000
    z1=r*math.sin(lat1)*1000

    x2=r*math.cos(lat2)*math.cos(long2)*1000
    y2=r*math.cos(lat2)*math.sin(long2)*1000
    z2=r*math.sin(lat2)*1000
    distance=math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1) )
    slope=(y2-y1)/(x2-x1)
    theta=math.atan(slope)
    if slope<0:
        x1=x1-math.cos(theta)-1
        x2=x2-math.cos(theta)-1
        y1=y1+math.sin(theta)+math.cos(theta)
        y2=y2+math.sin(theta)+math.cos(theta)
        z1=z1
        z2=z2
    else:
        x1=x1-math.cos(theta)
        x2=x2-math.cos(theta)
        y1=y1+math.sin(theta)+math.cos(theta)+1
        y2=y2+math.sin(theta)+math.cos(theta)+1
        z1=z1
        z2=z2
    lon1=math.atan2 (y2,x2)
    lon2=math.atan2 (y1,x1)
    
    hyp=math.sqrt(x2*x2+y2*y2)
    latt1=math.atan2(z2,hyp)
    hyp=math.sqrt(x1*x1+y1*y1)
    latt2=math.atan2(z1,hyp)

    latt1=math.degrees(latt1);
    latt2=math.degrees(latt2);
    lon1=math.degrees(lon1);
    lon2=math.degrees(lon2);
    latt1='%.14f'%latt1
    latt2='%.14f'%latt2
    lon1='%.14f'%lon1
    lon2='%.14f'%lon2
    
    xi=lon1+' '+latt1+' '+lon2+' '+latt2
    return xi
def dist(x1,y1,z1,x2,y2,z2):
    
    return (math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1) )) 
def calclatlong(lat1,long1,lat2,long2,d):
      
    r=6371
    lat1=math.radians (lat1)
    lat2=math.radians (lat2)
    long1=math.radians (long1)
    long2=math.radians (long2)

    x1=r*math.cos(lat1)*math.cos(long1)*1000
    y1=r*math.cos(lat1)*math.sin(long1)*1000
    z1=r*math.sin(lat1)*1000

    x2=r*math.cos(lat2)*math.cos(long2)*1000
    y2=r*math.cos(lat2)*math.sin(long2)*1000
    z2=r*math.sin(lat2)*1000
    distance=dist(x2,y2,z2,x1,y1,z1)
    slope=(y2-y1)/(x2-x1)
    print slope
    a=d/distance
    xx=x1*(1-a)+x2*a
    yy=y1*(1-a)+y2*a
    zz=z1*(1-a)+z2*a
    xx=xx/6371000
    yy=yy/6371000
    zz=zz/6371000

    #print xx,' ',yy,' ',zz

    lon=math.atan2 (yy,xx)
    hyp=math.sqrt(xx*xx+yy*yy)
    lat=math.atan2(zz,hyp)
    lat=math.degrees(lat);
    lon=math.degrees(lon);
    
    xi=''
    xi+=str(lon)+' '+str(lat)
    return xi
def calcwidth(lat1,long1,lat2,long2):
    
    #return (math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1) )) 
    r=6371
    lat1=math.radians (lat1)
    lat2=math.radians (lat2)
    long1=math.radians (long1)
    long2=math.radians (long2)

    x1=r*math.cos(lat1)*math.cos(long1)*1000
    y1=r*math.cos(lat1)*math.sin(long1)*1000
    z1=r*math.sin(lat1)*1000

    x2=r*math.cos(lat2)*math.cos(long2)*1000
    y2=r*math.cos(lat2)*math.sin(long2)*1000
    z2=r*math.sin(lat2)*1000
    distance=math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) + (z2-z1)*(z2-z1) )
    return distance
fname=raw_input('Enter the file name: ')
ofname=fname+"_new.kml"
fname+=".kml"
x=open(fname,"r")
#z=open(ofname,"w")
alti=int(raw_input('Enter the altitude for the building: '))
y=x.readlines()
flag=0
coord=[]
for i in y:
    if i.find("</coordinates>")!=-1:
        flag=0
    if flag==1:
        coord.append(i)
    if i.find("<coordinates>")!=-1:
        flag=1
pos=0
for i in coord[0]:
    if i>='0' and i<='9':
        break
    else:
        pos=pos+1
lat=[]
lon=[]
coordinates=coord[0][pos:len(coord[0])]
coordarr=coordinates.split(' ')
for i in range(len(coordarr)-1):
    temp=coordarr[i].split(',')
    lon.append(temp[0])
    lat.append(temp[1])
faces=len(coordarr)-2
x.close()

f=open('datafile.txt')
xs=f.readline()
xs=xs.split(' ')
rows=int(xs[0])
cols=int(xs[1])
xml=open('finalmodel.kml','w')
tempxml=open('copytext.txt','r')
start=tempxml.read()
xml.write(start)
tempxml.close()
tempxml=open('polygon.txt','r')
start=tempxml.read()
f.close()
#os.system('smartcity.py')
for i in range(faces):
    
    lat1=float(lat[i])
    lat2=float(lat[i+1])
    long1=float(lon[i])
    long2=float(lon[i+1])

    width=calcwidth(lat1,long1,lat2,long2)
    print width
    
    f=open('datafile.txt')
    xs=f.readline()
    for xs in f:
        xs=xs.split(' ')
        minx=int(xs[2])
        miny=int(xs[0])
        maxx=int(xs[3])
        maxy=int(xs[1])
        d=width*1.0*minx/cols
        latstr=calclatlong(lat1,long1,lat2,long2,d)
        latstr=latstr.split(' ')
        wlat1=latstr[1]
        wlong1=latstr[0]
        d=width*1.0*maxx/cols
        latstr=calclatlong(lat1,long1,lat2,long2,d)
        latstr=latstr.split(' ')
        
        wlat2=latstr[1]
        wlong2=latstr[0]
        latstr=newcoord(float(wlat1),float(wlong1),float(wlat2),float(wlong2))
        latstr=latstr.split(' ')
        wlat3=latstr[3]
        wlong3=latstr[2]
        wlat4=latstr[1]
        wlong4=latstr[0]
        height1=(rows-miny)*alti*1.0/rows
        height2=(rows-maxy)*alti*1.0/rows
        height1=int(height1)
        height2=int(height2)
        #back window
        xml.write(start)
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height1)+'\n')
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height1)+'\n')
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height2)+'\n')
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height2)+'\n')
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height1)+'\n')
        xml.write('</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n</Polygon>\n</Placemark>\n')
        #front window
        xml.write(start)
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height1)+'\n')
        xml.write(str(wlong4)+','+str(wlat4)+','+str(height1)+'\n')
        xml.write(str(wlong4)+','+str(wlat4)+','+str(height2)+'\n')
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height2)+'\n')
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height1)+'\n')
        xml.write('</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n</Polygon>\n</Placemark>\n')
        #top window
        xml.write(start)
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height1)+'\n')
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height1)+'\n')
        xml.write(str(wlong4)+','+str(wlat4)+','+str(height1)+'\n')
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height1)+'\n')
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height1)+'\n')
        xml.write('</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n</Polygon>\n</Placemark>\n')
        #bottom window
        xml.write(start)
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height2)+'\n')
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height2)+'\n')
        xml.write(str(wlong4)+','+str(wlat4)+','+str(height2)+'\n')
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height2)+'\n')
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height2)+'\n')
        xml.write('</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n</Polygon>\n</Placemark>\n')
        #left window
        xml.write(start)
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height1)+'\n')
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height1)+'\n')
        xml.write(str(wlong3)+','+str(wlat3)+','+str(height2)+'\n')
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height2)+'\n')
        xml.write(str(wlong1)+','+str(wlat1)+','+str(height1)+'\n')
        xml.write('</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n</Polygon>\n</Placemark>\n')
        #right window
        xml.write(start)
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height1)+'\n')
        xml.write(str(wlong4)+','+str(wlat4)+','+str(height1)+'\n')
        xml.write(str(wlong4)+','+str(wlat4)+','+str(height2)+'\n')
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height2)+'\n')
        xml.write(str(wlong2)+','+str(wlat2)+','+str(height1)+'\n')
        xml.write('</coordinates>\n</LinearRing>\n</outerBoundaryIs>\n</Polygon>\n</Placemark>\n')
        

        '''
        print wlong2,',',wlat2,',',height1
        print wlong2,',',wlat2,',',height2
        print wlong1,',',wlat1,',',height2
        print wlong1,',',wlat1,',',height1
        '''
    f.close()
xml.write('</Document>\n</kml>')
xml.close()
    
    
    
f.close()



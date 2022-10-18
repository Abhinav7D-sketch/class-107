import cv2
import time
import math

p1 = 530
p2 = 300

video = cv2.VideoCapture("bb3.mp4")
tracker = cv2.TrackerCSRT_create()

returned,img = video.read()
pBox = cv2.selectROI('tracking',img,False)
tracker.init(img,pBox)

def drawbox(img,pBox): 
    #code
    x,y,w,h = int(pBox[0]),int(pBox[1]),int(pBox[2]),int(pBox[3])
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3)
    cv2.putText(img,'Tracking',(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    
def goal_track(img,pBox):
    #code
    x,y,w,h = int(pBox[0]),int(pBox[1]),int(pBox[2]),int(pBox[3])
    c1 = x+int(w/2)
    c2 = y+int(h/2)
    cv2.circle(img,(c1,c2),2,(0,255,0),3)
    cv2.circle(img,(p1,p2),2,(0,255,255),3)
    dist = math.sqrt(((c1-p1)**2) + (c2-p2)**2)
    if(dist<=25):
        cv2.putText(img,'Goal!',(300,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(150,230,0),2)
        
    print(dist)
    
while True:
    check,img = video.read()
    success,pBox = tracker.update(img)
    
    if success:
        drawbox(img,pBox)
    else:
        cv2.putText(img,'Lost',(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    
    goal_track(img,pBox)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break

video.release()
cv2.destroyALLwindows()
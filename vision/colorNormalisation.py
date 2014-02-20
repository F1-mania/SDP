import cv2
import numpy as np
import tools

cap = cv2.VideoCapture(0)
for i in range(10):
    _,frame = cap.read()

calibration = tools.get_calibration('calibrate.json')
crop = tools.find_extremes(calibration['outline'])
while True:
    t,frame = cap.read()
    if t:
        frame = frame[crop[2]:crop[3],crop[0]:crop[1]]
        f = frame.copy()
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #Convert to HSV
        #frame[:,:,0] = cv2.equalizeHist(frame[:,:,0])
        frame[:,:,1] = cv2.equalizeHist(frame[:,:,1]) #Equalize the saturation channel
        #frame[:,:,2] = cv2.equalizeHist(frame[:,:,2])
        frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR) # Convert back for display
       # frame = cv2.blur(frame,(2,2))
        cv2.imshow("Normalized",frame)
        cv2.imshow("Original",f)
        cv2.waitKey(10)
    else:
        print "No frame"



#get ball pos
#The ball position should be the pos of the highest intensity in the red channel
#min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(frame[:,:,2])

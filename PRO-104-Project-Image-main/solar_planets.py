import cv2

img=cv2.imread("planets.jpg")

cv2.putText(img,"Sun",(60,40),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1, color=(0,0,255))
cv2.putText(img,"Mercury",(60,90),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.25, color=(255,255,255))
cv2.putText(img,"Venus",(95,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.25, color=(255,255,255))
cv2.putText(img,"Earth",(140,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.35, color=(255,255,255))
cv2.putText(img,"Mars",(180,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Jupiter",(250,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Saturn",(380,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Uranus",(470,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5, color=(255,255,255))
cv2.putText(img,"Neptune",(530,130),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.5, color=(255,255,255))

cv2.imshow("output",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)
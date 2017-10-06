
import cv2
img = cv2.imread("1.jpg")
res = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)
cv2.imshow("zhs", res)
cv2.waitKey(10000)
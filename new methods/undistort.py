import numpy as np
import cv2
import glob

nffile = np.load('Camera.npz')

mtx = nffile['mtx']

dist =  nffile['dist']





imgl=cv2.imread('l.jpg')
imgr= cv2.imread('r.jpg')
h,  w = imgl.shape[:2]
cv2.imshow("Original",imgl)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 0, (w,h))


mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(imgl,mapx,mapy,cv2.INTER_LINEAR)
# undistort
#dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst1 = dst[y:y+h, x:x+w]
#cv2.imwrite('right1.png', dst1)
cv2.imwrite('undist_left.png', dst1)

h,  w = imgr.shape[:2]
cv2.imshow("Original",imgr)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 0, (w,h))


mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)
dst = cv2.remap(imgr,mapx,mapy,cv2.INTER_LINEAR)
# undistort
#dst = cv2.undistort(img, mtx, dist, None, newcameramtx)
# crop the image
x, y, w, h = roi
dst1 = dst[y:y+h, x:x+w]
cv2.imwrite('undist_right.png', dst1)

cv2.waitKey()
cap.release()
cv2.destroyAllWindows()

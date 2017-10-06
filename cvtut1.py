import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('p1eye.jpg',cv2.IMREAD_GRAYSCALE)
# IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

## normal fumctions 

#cv2.imshow('image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


##matplot lib functions

#plt.imshow(img,cmap='gray',interpolation='bicubic')
#plt.plot([800,200],[200,600],'c',linewidth=5)
#plt.show()

cv2.imwrite('eyegray.png',img) # save a grayscale copy
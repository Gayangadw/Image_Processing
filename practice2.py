import matplotlib.pyplot as plt
import numpy as np
import cv2 as cv


def image_brighten_1(image,shift):
    h=image.shape[0]
    w=image.shape[1]

    result=np.zeros(image.shape,image.dtype)
    for i in range(0,h):
        for j in range(0,w):
            result[i,j]=image[i,j]+shift
    return result

def image_brighten_2(image,shift):
    h=image.shape[0]
    w=image.shape[1]

    result=np.zeros(image.shape,image.dtype)
    for i in range(0,h):
        for j in range(0,w):
            result[i,j]=min(image[i,j]+shift,255)
    return result
image=cv.imread('C:/Users/User/Downloads/new1.jpeg',cv.IMREAD_GRAYSCALE)
imgb=image_brighten_1(image,90)
imgc=image_brighten_2(image,50)
f,ax=plt.subplots(1,3,figsize=(9,3))
ax[0].imshow(image,cmap='gray',vmin=0,vmax=255)
ax[1].imshow(image,cmap='gray',vmin=0,vmax=255)
ax[2].imshow(image,cmap='gray',vmin=0,vmax=255)
cv.waitKey(0)
cv.destroyAllWindows()
plt.show()



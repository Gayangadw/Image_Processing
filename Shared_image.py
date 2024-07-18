import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading the image from the disk
img=cv2.imread('C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg')

#convert the bgr image to  rgb image
image_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#image shape along x and y
width= image_rgb.shape[1]
height=image_rgb.shape[0]

#Define the sharing factor
ShearX= -0.15
ShearY=0
#Dfine the Translation matrix for sharing

transformation_matrix=np.array([[1,ShearX,0],[0,1,ShearY]],dtype=np.float32)

#apply sharing
Sheared_image = cv2.warpAffine(image_rgb,transformation_matrix,(width,height))

#Create subplots
fig,axs=plt.subplots(1,2,figsize=(7,4))

#plot the original image
axs[0].imshow(Sheared_image)
axs[0].set_title('Original Image')

#plot the shared image

axs[1].imshow(Sheared_image)
axs[1].set_title('Sheared Image')

#Remove ticks the subplots

for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

#Display the subplots

plt.tight_layout()
plt.show()


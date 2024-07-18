import cv2
import numpy as np
import matplotlib.pyplot as plt

#reading the image from the disk
img=cv2.imread('C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg')

#convert the bgr image to  rgb image
image_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

width=image_rgb.shape[1]
height= image_rgb.shape[0]

tx=100
ty= 70

#Translation matrix
translation_matrix= np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)

translated_image=cv2.warpAffine(image_rgb,translation_matrix,(width,height))

#create subplots
fig,axs =plt.subplots(1,2,figsize=(7,4))

#plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Image Original')

#plot the translated image
axs[1].imshow(translated_image)
axs[1].set_title('Image Translation')
#remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

#Display the subplots
plt.tight_layout()
plt.show()


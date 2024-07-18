import cv2
import numpy as np
import matplotlib.pyplot as plt

# Reading the image from the disk
img = cv2.imread('C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg')

# Convert the BGR image to RGB image
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Canny edge detection
edges = cv2.Canny(image=image_rgb, threshold1=100, threshold2=200)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(7, 4))

# Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')

# Plot the edge-detected image
axs[1].imshow(edges, cmap='gray')
axs[1].set_title('Edge-detected Image')

# Remove ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image from your PC
image = cv2.imread('C:/Users/User/OneDrive/Pictures/Pictures/photo.jpg')

# Convert the BGR image to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the scale factors
scale_factor_1 = 3.0  # Increase the size by three times
scale_factor_2 = 1/3.0  # Decrease the size by three times

# Get the original image dimensions
height, width = image_rgb.shape[:2]

# Calculate the new image dimensions for the zoomed image
new_height = int(height * scale_factor_1)
new_width = int(width * scale_factor_1)

# Resize the image (zoomed in)
zoomed_image = cv2.resize(src=image_rgb, dsize=(new_width, new_height), interpolation=cv2.INTER_CUBIC)

# Calculate the new image dimensions for the scaled image
new_height1 = int(height * scale_factor_2)
new_width1 = int(width * scale_factor_2)

# Resize the image (scaled down)
scaled_image = cv2.resize(src=image_rgb, dsize=(new_width1, new_height1), interpolation=cv2.INTER_AREA)

# Create subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image\nShape: ' + str(image_rgb.shape))

# Plot the zoomed image
axs[1].imshow(zoomed_image)
axs[1].set_title('Zoomed Image\nShape: ' + str(zoomed_image.shape))

# Plot the scaled image
axs[2].imshow(scaled_image)
axs[2].set_title('Scaled Image\nShape: ' + str(scaled_image.shape))

# Remove the ticks from the subplots
for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])

# Display the subplots
plt.tight_layout()
plt.show()

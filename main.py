from skimage import io, color
import matplotlib.pyplot as plt

# Load the image
image = io.imread(r'C:\Users\Vagelis\Desktop\DSC_0335.jpg')

# Convert to Lab color space
lab_image = color.rgb2lab(image)

# Normalize the Lab image values to the valid range
lab_image = lab_image / 100.0  # Divide by 100 to bring the values in the range [0, 1]

# Display the L channel
plt.imshow(lab_image[:, :, 0], cmap='gray')
plt.axis('off')
plt.show()

# Display the a channel
plt.imshow(lab_image[:, :, 1], cmap='RdYlGn')
plt.axis('off')
plt.show()

# Display the b channel
plt.imshow(lab_image[:, :, 2], cmap='RdYlBu')
plt.axis('off')
plt.show()

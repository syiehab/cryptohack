![image](https://github.com/user-attachments/assets/9a122c6f-198a-4349-87e2-8eec38905721)


```
from PIL import Image
import numpy as np

# Load the two images
image1 = Image.open('flag.png')
image2 = Image.open('lemur.png')

# Ensure both images are the same size
if image1.size != image2.size:
    raise ValueError("Images must be of the same size")

# Convert the images to numpy arrays (RGB format)
arr1 = np.array(image1)
arr2 = np.array(image2)

# Perform the XOR operation on each pixel's RGB values
xor_result = np.bitwise_xor(arr1, arr2)

# Convert the result back to an image
result_image = Image.fromarray(xor_result)

# Save or display the result image
result_image.save('xor_image.png')
result_image.show()
```
C:\Users\user\Documents\uniten\ctf\cryptohack\xor_image.png

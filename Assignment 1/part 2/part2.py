import cv2
import numpy as np

def adjust_brightness(image, value):
    return cv2.add(image, np.full(image.shape, value, dtype=np.uint8))

def adjust_contrast(image, factor):
    return cv2.convertScaleAbs(image, alpha=factor, beta=0)

def blend_images(img1, img2, alpha):
    return cv2.addWeighted(img1, 1 - alpha, img2, alpha, 0)

# Load first image
img1 = cv2.imread("image1.jpg")
cv2.imshow("Original Image", img1)
cv2.waitKey(0)

# Increase brightness
bright_img = adjust_brightness(img1, 150)
cv2.imshow("Brightened Image", bright_img)
cv2.waitKey(0)

# Adjust contrast
contrast_img = adjust_contrast(img1, 0.5)
cv2.imshow("Contrast Adjusted Image", contrast_img)
cv2.waitKey(0)

# Load second image
img2 = cv2.imread("image2.jpg")
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
cv2.imshow("Second Image", img2)
cv2.waitKey(0)

# Get alpha value from user
alpha = float(input("Enter alpha (0 to 1): "))
while alpha < 0 or alpha > 1:
    alpha = float(input("Invalid input. Enter alpha (0 to 1): "))

# Blend images
blended_img = blend_images(img1, img2, alpha)
cv2.imshow("Blended Image", blended_img)
cv2.waitKey(0)

cv2.destroyAllWindows()
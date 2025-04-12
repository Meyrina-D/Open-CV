import cv2
img = cv2.imread("color.jpg")
cv2.imshow("original image", img)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
cv2.imshow("Grayscale", gray_image)
cv2.waitKey(0)
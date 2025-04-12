import cv2
img = cv2.imread("/home/administrator/Pictures/istockphoto-1403500817-612x612.jpg")
cv2.imshow("meyrina", img)
height = img.shape[0]
width = img.shape[1]
print("Height of Image:", height)
print("Width of Image:", width)
cv2.waitKey(0)
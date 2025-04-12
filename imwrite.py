import cv2
img = cv2.imread("/home/administrator/Pictures/istockphoto-1403500817-612x612.jpg")
cv2.imshow("meyrina", img)
cv2.imwrite("meyrina.png", img)
cv2.imwrite("meyrina.tiff", img)
cv2.imshow("meyrina.png", img)
cv2.imshow("meyrina.tiff", img)
cv2.waitKey(0)
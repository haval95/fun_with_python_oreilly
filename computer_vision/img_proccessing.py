import cv2

img = cv2.imread("img.jpg", 0)

print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img,(int(img.shape[1]/5),int(img.shape[0]/5)))
cv2.imshow("water", resized_img)
cv2.imwrite("newImg.jpg",resized_img )
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2
imgMatrix= cv2.imread("Jayanta.JPG")
cv2.imshow("Original image",imgMatrix)#it only show with a name

cv2.imwrite("output.jpg",imgMatrix)#jpg
cv2.imwrite("output.png",imgMatrix)#png

print(imgMatrix.shape)


# convert 2 gray
grayMatrix = cv2.cvtColor(imgMatrix,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image",grayMatrix)



cv2.waitKey()
cv2.destroyAllWindows()
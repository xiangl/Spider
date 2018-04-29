import cv2
'''
im = cv2.imread("C:/Users/Administrator/Pictures/Snap4.jpg")  #读取图片
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   #转换了灰度化
print('hello')


im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   #转换了灰度化
cv2.axis("off")
cv2.title("Input Image")
cv2.imshow(im_gray, cmap="gray")  #显示图片
cv2.show()
'''
#灰度读取
img = cv2.imread("C:/Users/Administrator/Pictures/Snap4.jpg",0)
ret,img2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#ret,img2 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow('image',img2)

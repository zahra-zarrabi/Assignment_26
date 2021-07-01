import cv2
import numpy as np
import argparse

my_parser=argparse.ArgumentParser()
my_parser.add_argument('--kernel_size', type=int)
my_parser.add_argument('--output_name',type=str)
my_parser.add_argument('--image',default='image/flower_input.jpg',type=str)
args=my_parser.parse_args()

image=cv2.imread(args.image,cv2.IMREAD_GRAYSCALE)

# kernel=np.array([[1,1,1],[0,0,0],[1,1,1]])
# result=cv2.filter2D(image,-1,kernel)
result=cv2.blur(image,(args.kernel_size,args.kernel_size))
for i in range(0,image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i,j]>170:
            result[i,j]=image[i,j]

cv2.imshow('output',result)
cv2.imwrite(args.output_name,result)
cv2.waitKey()

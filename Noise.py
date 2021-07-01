import cv2
import numpy as np
import argparse

my_parser=argparse.ArgumentParser()
my_parser.add_argument('--output_name',type=str)
my_parser.add_argument('--image',default='image/board.tif',type=str)
args=my_parser.parse_args()

image=cv2.imread(args.image)
image=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

for i in range(1,image.shape[0]-1):
    for j in range(1, image.shape[1] - 1):
        small_image=image[i-1:i+2,j-1:j+2]
        sort=np.sort(small_image, axis=None)
        image[i,j]=sort[4]

cv2.imshow('out',image)
cv2.imwrite(args.output_name,image)
cv2.waitKey()
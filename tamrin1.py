import cv2
import shutil
import os
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str)
ap = parser.parse_args()
img_chess=cv2.imread(ap.path)

img_chess=cv2.cvtColor(img_chess,cv2.COLOR_RGB2GRAY)
print(img_chess.shape)
(thresh,img_binary)=cv2.threshold(img_chess, 170, 255, cv2.THRESH_BINARY)

column = []
obj = False

for n in range(img_binary.shape[1]):
    if not obj:
        if any(img_binary[:, n] == 255):
            column.append(n)
            obj = True
    else:
        if all(img_binary[:, n] != 255):
            column.append(n)
            obj = False
# for m in range(0, len(column), 2):
#     cv2.imwrite(f"out/result{m}.jpg",img_chess[:, column[m]:column[m+1]])

row=[]
obj = 0
for index in range(0, len(column), 2):
    # print(co.shape)
    for n in range(img_binary.shape[0]):
        if obj == 0:
            if any(img_binary[n, column[index]:column[index+1]] == 255):
                x = n
                obj = 1
        elif obj == 1:
            if np.sum(img_binary[n, column[index]:column[index+1]]) < (np.size(img_binary[n, column[index]:column[index+1]])-(1/4))*255:
                row.append(x)
                obj = 2
        else:
            if all(img_binary[n, column[index]:column[index+1]] != 255):
                y = n
                obj = 0

                row.append(y)

# shutil.rmtree('out',ignore_errors=True)
# os.makedirs('out')
cnt = 0
for m in range(0, len(column), 2):
    for n in range(0, len(row),  2):
        cnt += 1
        # print(row[n])
        cv2.imwrite(f"out/resultt{cnt}.jpg", img_chess[row[n]:row[n + 1], column[m]: column[m+1]])


cv2.imshow("show output",img_binary)
cv2.waitKey()
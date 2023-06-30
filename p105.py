import os
import cv2

path="C:/Users/Mauli/Downloads/PRO-C105-Student-Boilerplate-main/p105/imgs"

images=[]

for file in os.listdir(path):
    name, ext=os.path.splitext(file)

    if ext in['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name =path+'/'+file
        print(file_name)
        images.append(file_name)




count=len(images)
frames=cv2.imread(images[0])
width, height, channels=frames.shape
size=(width, height)

out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, size)


for i in range(0, count-1):
    cv2.imread(images[i])
    out.write(frames)
    print("done")

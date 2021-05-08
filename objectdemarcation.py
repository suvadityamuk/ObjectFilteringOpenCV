import cv2
import numpy
import os

pt_list = []
roiselected = False

def roi_sel(event, x, y, flags, param):
    global pt_list, roiselected
    if event == cv2.EVENT_LBUTTONDOWN:
        pt_list = [(x,y)]
        roiselected = True
    elif event == cv2.EVENT_LBUTTONUP:
        pt_list.append((x,y))
        print(pt_list)
        roiselected = False
        cv2.rectangle(img, pt_list[0], pt_list[1], (0,255,255), thickness=2)
        cv2.imshow(f'Object Demarcation ({counter} out of {len(os.listdir(folder))})', img)

counter = 1
for folder in ['negative', 'positive']:
    for filename in os.listdir(folder):
        print(filename)
        try:
            if folder=='negative':
                img = cv2.imread(folder + '/resized/' + filename, cv2.IMREAD_COLOR)
                line = folder + '/resized/' + filename + '\n'
                with open('negative/bg.txt', 'a') as f:
                    f.write(line)
            elif folder=='positive':
                img = cv2.imread((folder + '/' + filename), cv2.IMREAD_COLOR)
                print(type(img))
                clone = img.copy()
                print(type(clone))
                cv2.namedWindow(f'Object Demarcation ({counter} out of {len(os.listdir(folder))})')
                cv2.setMouseCallback(f'Object Demarcation ({counter} out of {len(os.listdir(folder))})', roi_sel)
                while True:
                    cv2.imshow(f'Object Demarcation ({counter} out of {len(os.listdir(folder))})', img)
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord('r'):
                        img = clone.copy()
                        pt_list.pop()
                    elif key == ord('l'):
                        if(len(pt_list)==2):
                            counter+=1
                            break
                        elif(len(pt_list)==1):
                            img = clone.copy()                            
                line = folder + '/' + filename + f' 1 {pt_list[0][1]} {pt_list[0][1]} {pt_list[1][0]} {pt_list[1][1]}' +'\n'
                pt_list.clear()
                with open('positive/positive.txt', 'a') as f:
                    f.write(line)
                cv2.destroyAllWindows()
        except Exception as e:
            print(str(e))
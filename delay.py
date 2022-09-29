import os
import cv2

path = os.getcwd()
os.chdir(path + '\src')

fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter(f'{path}\res\output.mp4', fourcc, 60.0, (1920, 1080))

for videoName in os.listdir():

    cap = cv2.VideoCapture(videoName)
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = cap.get(cv2.CAP_PROP_FPS)


    print(f'Init Finish')
    print(f'Starting process all: {frame_num}')

    for i in range(int(frame_num)):
        ret, frame = cap.read()
        now_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
        print(f'Processing Frame [{videoName}]: {now_frame} / {frame_num}')

        if i % (2*int(fps)) == 0:
            out.write(frame)


    cap.release()

out.release()
cv2.destroyAllWindows()
print('Process Finish')
import cv2

vid = cv2.VideoCapture(0)
if(vid.isOpened() == False):
    print("Unable to read the fid")
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(vid.get(cv2.CAP_PROP_FPS))
print(height, width, fps)

out = cv2.VideoWriter("MyVideo.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while(True):
    ret, frame = vid.read()
    cv2.imshow("Webcam", frame)
    out.write(frame)
    if(cv2.waitKey(1) == 32):
        break
vid.release()
cv2.destroyAllWindows()
out.release()
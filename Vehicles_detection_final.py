# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
import pandas as pd

 
# capture frames from a video
cap = cv2.VideoCapture('video.avi')
 
# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

no_obj_det=0
frames_got_processed = 0
frame_processed = []
number_of_object_detected= []

# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    try:
        ret, frames = cap.read()
        frames_got_processed += 1
        # convert to gray scale of each frames
        gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
        # Detects cars of different sizes in the input image
        cars = car_cascade.detectMultiScale(gray, 1.1, 1)
        # To draw a rectangle in each cars
        for (x,y,w,h) in cars:
            cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

        # # Display frames in a window
        cv2.imshow('video2', frames)
        if cv2.waitKey(33) == 27:
            break

        # loop to count the number of objects detected at every 5th frame
        if frames_got_processed % 5 == 0:
            print "appended in frame number",frames_got_processed,len(cars)
            frame_processed.append(frames_got_processed)
            number_of_object_detected.append(len(cars))


    except:
        print "somthing went wrong"
        break

# Display every 5th frame and number of object detected
print frame_processed
print number_of_object_detected


# writing results into CSV file
raw_data = {'frame_processed': frame_processed,
        'number_of_object_detected':number_of_object_detected}
df = pd.DataFrame(raw_data, columns = ['frame_processed', 'number_of_object_detected'])

df.to_csv('example.csv')


# De-allocate any associated memory usage
cv2.destroyAllWindows()

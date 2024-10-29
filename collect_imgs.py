import os

import cv2

#Data Directory: The DATA_DIR variable specifies the directory where the collected data will be stored.
#If the directory does not exist, it is created using the os.makedirs() function.

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

#Number of Classes: The number_of_classes variable determines the number of classes or categories for which data
#will be collected. In this example, we assume there are three classes.
#The dataset_size variable specifies the number of images to collect for each class. In this case, we collect 100
#images per class
    
number_of_classes = 3
dataset_size = 100

#we collect data using video capture from the default camera (index 2)
#Data Collection Loop: The code uses a loop to collect data for each class. 
#Then, it prompts the user to press the'Q' key to start collecting data for the current class.
#Once the 'Q' key is pressed, the code enters another loop to collect the specified number of images for the current class.
#It captures frames from the video feed using cap.read() and displays them using cv2.imshow(). Each frame is saved as
#an image file in the corresponding class directory using cv2.imwrite().
#After collecting the data, the code releases the video capture resources using cap.release() and closes any
#open windows using cv2.destroyAllWindows().


cap = cv2.VideoCapture(2)
for j in range(number_of_classes):
    if not os.path.exists(os.path.join(DATA_DIR, str(j))):
        os.makedirs(os.path.join(DATA_DIR, str(j)))

    print('Collecting data for class {}'.format(j))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()

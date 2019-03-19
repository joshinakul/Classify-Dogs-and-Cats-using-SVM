# Importing Libraries
import cv2
import os 
import numpy as np

# Declaring input and output variables 
input_data = []
labeled_data = []

#Path of dataset
image_dir = 'dataset/'

# Reading all the image names
img_path = [image_dir+i for i in os.listdir(image_dir)]

# Taking image one by one
for i in img_path:
    img = cv2.imread(i,0) # converting img to grayscale
    img = cv2.resize(img,(64,64)) # resizing img into (64,64)
    input_data.append(img) # appending img to input list
    if 'cat' in i:  # if name of img contains cat then append 0
        labeled_data.append(0)
    elif 'dog' in i:    # if name of img contains dog then append 1
        labeled_data.append(1)

# Converting list into numpy arrays
input_data = np.array(input_data)
input_data = input_data.reshape((input_data.shape[0],64*64)) # Reshaping a 3d array into 2d array
labeled_data = np.array(labeled_data)

# Splitting the dataset in 7000 and 3000
from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test = tts(input_data,labeled_data,test_size = 0.2,random_state = 42)

# Training the SVM model
from sklearn.svm import SVC
model = SVC(gamma = 0.0000001)
model.fit(x_train,y_train)

# Predicting on the test set
y_pred = model.predict(x_test)

# Evaluation of model
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test,y_pred)
print('Accuracy =',accuracy*100)
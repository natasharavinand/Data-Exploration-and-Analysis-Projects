# import libraries

import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import streamlit as st
import os

# create a title for program

st.write("""
# Heart Disease Detection
Detect if a patient has heart disease using a random forest classifier.
""")

# open and display Image

image = Image.open(os.getcwd()+'/heart.jpg')
st.image(image, caption="ML", use_column_width=True)

# get data, drop certain features

df = pd.read_csv('heart.csv')
df.drop(['restecg', 'oldpeak', 'slope','thal'], inplace=True, axis=1)

# set a subheader

st.subheader('Data Information:')

# show data as table

st.dataframe(df)

# show stats

st.write(df.describe())

# show the data as a bar chart

bar_chart = st.bar_chart(df)

# split data into independent X (features) and dependent y (target)

X = df.iloc[:, 0:-1].values
y = df.iloc[:, -1].values

# split data into training and test

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# get user's input for features

def get_input():
    sex = st.radio("Select Sex: ", ('Male', 'Female'))
    if sex == 'Male':
        sex = 1
    else:
        sex = 0
    age = st.sidebar.slider('age', 0, 100, 50)
    chest_pain = st.radio("Select Chest Pain Type: ", (1, 2, 3, 4))
    trestbps = st.sidebar.slider('Resting Blood Pressure in mm Hg', 80, 180, 110)
    chol = st.sidebar.slider('Serum Cholestoral in mg/dl', 150, 450, 250)
    thalach = st.sidebar.slider('Maximum Heart Rate Achieved in BPM', 100, 210, 150)
    exang = st.radio("Exercise Induced Angina Present: ", ('True', 'False'))
    if exang == 'True':
        exang = 1
    else:
        exang = 0
    ca = st.sidebar.slider("Number of Major Blood Vessels Colored by Flouroscopy", 0, 3, 0)
    fbs = st.radio("Fasting Blood Sugar > 120 mg/dl: ", ('True', 'False'))
    if fbs == 'True':
        fbs = 1
    else:
        fbs = 0

    # store data in dictionary

    user_features = {'sex':sex,
    'age':age,
    'chest_pain':chest_pain,
    'trestbps':trestbps,
    'chol':chol,
    'thalach':thalach,
    'exang':exang,
    'ca':ca,
    'fbs':fbs}

    # transform to a dataframe

    features = pd.DataFrame(user_features, index=[0])
    return features

# store the users input into a variable

user_input = get_input()

# set a subheader and display the user's get_input

st.subheader('User Input: ')
st.write(user_input)

# create and train model_selection

RandomForestClassifier = RandomForestClassifier()
RandomForestClassifier.fit(X_train, y_train)

# Show the model's metrics

st.subheader('Model Test Accuracy Score:')
st.write(str(round(accuracy_score(y_test, RandomForestClassifier.predict(X_test))*100,2)), "%")

# store model's predictions

prediction = RandomForestClassifier.predict(user_input)

# set a subheader and display the classification

st.subheader('Classification: ')
if prediction == 0:
    st.write("No predicted heart disease")
else:
    st.write("Predicted heart disease")

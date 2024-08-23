import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns = iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names, iris.DESCR
    # print(dir(iris))
    # print(iris.DESCR)
    # print(iris.data)
    # print(iris.data_module)
    # print(iris.feature_names)
    # print(iris.filename)
    # print(iris.frame)
    # print(iris.target)
    # print(iris.target_names)

df, target_names, description = load_data()

if 'show_datset_descr' not in st.session_state:
    st.session_state.show_datset_descr = False
    

model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Select Sepal Length", min(df['sepal length (cm)']), max(df['sepal length (cm)']))
sepal_width = st.sidebar.slider("Select Sepal Width", min(df['sepal width (cm)']), max(df['sepal width (cm)']))
petal_length = st.sidebar.slider("Select Petal Length", min(df['petal length (cm)']), max(df['petal length (cm)']))
petal_width = st.sidebar.slider("Select Petal Width", min(df['petal width (cm)']), max(df['petal width (cm)']))

input_data = [sepal_length, sepal_width, petal_length, petal_width]
input_data = [input_data] # to convert it to 2d array, the predict method expects the input to be in the shape of [n_samples, n_features]. Even if you have only one sample, it still needs to be a 2D array.

#prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.title("**Iris Plants Prediction**")


# CSS for styling the box
st.markdown("""
    <style>
    .prediction-box {
        border: 2px solid #4CAF50;
        padding: 10px;
        border-radius: 10px;
        background-color: #f9f9f9;
        box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
        # color: #4CAF50;
        # font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Display the prediction in a styled box
st.markdown(f'<div class="prediction-box">The predicted species is: <strong>{predicted_species.upper()}</strong></div>', unsafe_allow_html=True)


st.write('')
st.write('')
if st.button('About Dataset'):
    st.session_state.show_datset_descr = not st.session_state.show_datset_descr

if st.session_state.show_datset_descr:
    st.write(description)
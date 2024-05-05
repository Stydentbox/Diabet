import pandas as pd
import streamlit as st
from PIL import Image
from model import load_model_and_predict


def process_main_page():
    st.title('Предсказание диабета')
    st.write('Данные взяты из репозитория [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) платформы Kaggle.')
    image = Image.open('data/diabetes.jpg')
    st.image(image)
    personal_info = process_side_bar_inputs()
    if st.button("Предсказать вероятность диабета"):
        prediction, prediction_probas = load_model_and_predict(personal_info)
        write_prediction(prediction, prediction_probas)


def write_prediction(prediction, prediction_probas):
    st.write("## Предсказание диабета")
    st.write(prediction)

    st.write("## Вероятность предсказания диабета")
    st.write(prediction_probas)


def process_side_bar_inputs():
    st.sidebar.header('Введите данные пациента')
    user_input_df = sidebar_input_features()
    st.write("## Данные пациента")
    st.write(user_input_df)

    return user_input_df

def sidebar_input_features():
    age = st.sidebar.number_input("Возраст, лет", 1, 150, 25, 1)
    pregnancies = st.sidebar.number_input("Количество родов", 0, 20, 0, 1)
    glucose = st.sidebar.slider("Глюкоза mg/dl (mmol/l = mg/dl / 18)", 0, 200, 25, 1)
    skinthickness = st.sidebar.slider("Толщина складки трицепса", 0, 99, 20, 1)
    bloodpressure = st.sidebar.slider('Диастолическое артериальное давление', 0, 122, 69, 1)
    insulin = st.sidebar.slider("Инсулин пмоль/л", 0, 846, 79, 1)
    bmi = st.sidebar.slider("Индекс массы тела", 0.0, 67.1, 31.4, 0.1)
    dpf = st.sidebar.slider("Функция определения родословной диабета, DPF", 0.000, 2.420, 0.471, 0.001)
    
    user_input_data = {
        "Age": [age],
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "SkinThickness": [skinthickness],
        "BloodPressure": [bloodpressure],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [dpf]
    }
    
    user_input_df = pd.DataFrame(user_input_data)
    
    return user_input_df
    
    df = pd.DataFrame(data, index=[0])
    
    return df


if __name__ == "__main__":
    process_main_page()
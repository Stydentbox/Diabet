# Предсказание диабета

Веб приложение для предсказание диабета на основе диагностических исследований.

Данные взяты из репозитория [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) платформы Kaggle.
Датасет содержат данные о женщинах индианках Пима старше 21 года.

## Колонки
- Pregnancies : количество беременностей
- Glucose : mmol/L (millimoles per liter)
- BloodPressure : diastolic blood pressure in mm of hg
- SkinThickness : triceps skin fold thickness in mm
- Insulin : the 2-Hour serum insulin (mu U/ml)
- BMI : Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction : Diabetes pedigree function
- Age : Age (years)

## Files

- `DPapp.py`: streamlit app file
- `model.py`: script for generating the Random Forest classifier model
- `data/diabetes.csv` and `data/model_weights.mw`: data file and pre-trained model
- `requirements.txt`: package requirements files

## Run App Locally 

### Shell

For directly run streamlit locally in the repo root folder as follows:

```shell
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ streamlit run DPapp.py
```
Open http://localhost:8501 to view the app.

&copy; ANLobanov


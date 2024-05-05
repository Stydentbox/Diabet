# Предсказание диабета

Веб приложение для предсказание диабета на основе диагностических исследований.

Данные взяты из репозитория [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) платформы Kaggle.
Датасет содержат данные о женщинах индианках Пима старше 21 года.

## Колонки
- Pregnancies : количество беременностей
- Glucose : Глюкоза mmol/L (millimoles per liter)
- BloodPressure : Диастолическое артериальное давление в mm of hg
- SkinThickness : Толщина кожной складки трицепса в мм
- Insulin : 2-часовой сывороточный инсулин (mu U/ml)
- BMI : Индекс массы тела (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction : Функция родословной диабета
- Age : Возраст (лет)

## Файлы

- `DPapp.py`: streamlit app file
- `model.py`: script for generating the Random Forest classifier model
- `data/diabetes.csv` and `data/model_weights.mw`: data file and pre-trained model
- `requirements.txt`: package requirements files

## Локальный запуск приложения 

```shell
$ python -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ streamlit run DPapp.py
```
Open http://localhost:8501 to view the app.

&copy; ANLobanov


# Employee Salary Classification App

A web application for predicting whether an employee earns **>50K** or **≤50K** per year based on demographic and job-related features. Built with **Flask**, **scikit-learn**, and **pandas**.

---

## Features

- **Single Prediction:** Enter employee details in a web form to predict salary class.
- **Batch Prediction:** Upload a CSV file of multiple employees for batch salary class prediction and download results.
- **User-friendly UI:** Clean, responsive interface styled with Google Fonts and custom CSS.
- **Model Integration:** Uses a pre-trained machine learning model (`best_model.pkl`).

---

## Demo

![App Screenshot](screenshot.png) <!-- Add your screenshot file if available -->

---

## Project Structure

```
Employee Salary Final Project/
│
├── app.py                      # Main Flask application
├── best_model.pkl              # Trained ML model (scikit-learn)
├── uploads/                    # Folder for batch uploads and results
├── templates/
│   ├── index.html              # Main page template
│   └── batch.html              # Batch prediction template
├── static/                     # (Optional) For static files (CSS, images)
└── README.md                   # Project documentation
```

---

## Requirements

- Python 3.7+
- Flask
- pandas
- scikit-learn
- joblib

Install dependencies:
```bash
pip install flask pandas scikit-learn joblib
```

---

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/employee-salary-classification.git
cd employee-salary-classification
```

### 2. Place the Model

Ensure `best_model.pkl` (your trained model) is in the project root.

### 3. Run the App

```bash
python app.py
```

The app will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Web App Usage

### Single Prediction

1. Fill in the employee details:
    - Age
    - Workclass
    - Education Number
    - Job Role (Occupation)
    - Hours per week
    - Years of Experience
2. Click **Predict Salary Class**.
3. The prediction result will be displayed.

### Batch Prediction

1. Click **Batch Prediction** in the top right.
2. Upload a CSV file with the following columns:
    - `age`
    - `workclass`
    - `educational-num`
    - `occupation`
    - `hours-per-week`
    - `experience`
3. Click **Predict for Batch**.
4. Download the results CSV with predictions.

---

## Example Input Format

### Single Prediction

Form fields correspond to these columns:
- `age`: Integer (18-65)
- `workclass`: Categorical (e.g., Private, Self-emp-not-inc, etc.)
- `educational-num`: Integer (1-16)
- `occupation`: Categorical (e.g., Tech-support, Sales, etc.)
- `hours-per-week`: Integer (1-120)
- `experience`: Integer (0-40)

### Batch Prediction CSV

```csv
age,workclass,educational-num,occupation,hours-per-week,experience
34,Private,10,Sales,40,5
45,State-gov,12,Exec-managerial,50,20
...
```

---

## Model Training (Optional)

If you want to retrain the model:

1. Prepare your dataset with the above columns and target.
2. Train a classifier (e.g., RandomForest, LogisticRegression).
3. Save the model:
    ```python
    import joblib
    joblib.dump(model, "best_model.pkl")
    ```

---

## License

This project is for educational purposes. Please check the license before commercial use.

---

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [scikit-learn](https://scikit-learn.org/)
- [pandas](https://pandas.pydata.org/)

---

## Author

- Your Name (your.email@example.com)
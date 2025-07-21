from flask import Flask, render_template, request, send_file, redirect, url_for, flash
import pandas as pd
import joblib
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "your_secret_key"
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the trained model
model = joblib.load("best_model.pkl")

def allowed_file(filename):
    return '.' in filename and filename.lower().endswith('.csv')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    input_df = None

    # Single prediction logic
    if request.method == 'POST' and 'predict_single' in request.form:
        try:
            # Get the form data
            age = int(request.form['age'])
            workclass = request.form['workclass']
            educational_num = int(request.form['educational-num'])
            occupation = request.form['occupation']
            hours_per_week = int(request.form['hours_per_week'])
            experience = int(request.form['experience'])

            # Single record DataFrame (as in Streamlit)
            input_df = pd.DataFrame({
                'age': [age],
                'workclass': [workclass],
                'educational-num': [educational_num],
                'occupation': [occupation],
                'hours-per-week': [hours_per_week],
                'experience': [experience]
            })
            prediction = model.predict(input_df)[0]
        except Exception as e:
            flash(f"Prediction failed: {e}")

    return render_template('index.html',
                           prediction=prediction,
                           input_df=input_df)

@app.route('/batch', methods=['GET', 'POST'])
def batch():
    batch_data = None
    preds_present = False
    csv_download_path = None

    if request.method == 'POST':
        file = request.files.get('batchfile')
        if file and allowed_file(file.filename):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(file_path)
            try:
                batch_data = pd.read_csv(file_path)
                preds = model.predict(batch_data)
                batch_data['PredictedClass'] = preds
                preds_present = True
                # Save for download
                out_path = os.path.join(UPLOAD_FOLDER, "predicted_classes.csv")
                batch_data.to_csv(out_path, index=False)
                csv_download_path = out_path
            except Exception as e:
                flash(f"Batch prediction failed: {e}")
        else:
            flash('Please upload a valid .csv file!')

    return render_template('batch.html', batch_data=batch_data, preds_present=preds_present, csv_download_path=csv_download_path)

@app.route('/download')
def download():
    filename = request.args.get('file')
    if filename and os.path.exists(filename):
        return send_file(filename, as_attachment=True)
    flash("File does not exist.")
    return redirect(url_for('batch'))

if __name__ == '__main__':
    app.run(debug=True)

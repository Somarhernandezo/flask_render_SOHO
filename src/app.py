from flask import Flask, render_template, request
from pickle import load
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "Smarthphone_addiction_XG_Boost.sav")

model = load(open(model_path, "rb"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", prediction=None)


@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form.get("age")),
            float(request.form.get("daily_screen_time_hours")),
            float(request.form.get("social_media_hours")),
            float(request.form.get("gaming_hours")),
            float(request.form.get("work_study_hours")),
            float(request.form.get("sleep_hours")),
            float(request.form.get("notifications_per_day")),
            float(request.form.get("app_opens_per_day")),
            float(request.form.get("weekend_screen_time")),
            float(request.form.get("gender_Male")),
            float(request.form.get("gender_Other")),
            float(request.form.get("stress_level_Low")),
            float(request.form.get("stress_level_Medium")),
            float(request.form.get("academic_work_impact_Yes"))
        ]

        prediction = model.predict([features])[0]

        result = "Adicto" if prediction == 1 else "No adicto"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return f"Error: {str(e)}"

        # https://flask-render-soho-1.onrender.com
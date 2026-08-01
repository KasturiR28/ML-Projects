from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = [
            float(request.form["CGPA"]),
            int(request.form["Internships"]),
            int(request.form["Projects"]),
            int(request.form["WorkshopsCertifications"]),
            float(request.form["AptitudeTestScore"]),
            float(request.form["SoftSkillsRating"]),
            int(request.form["ExtracurricularActivities"]),
            int(request.form["PlacementTraining"]),
            float(request.form["SSC_Marks"]),
            float(request.form["HSC_Marks"])
        ]

        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "🎉 High Chances of Placement"
            status = "success"
        else:
            result = "⚠️ Lower Chances of Placement"
            status = "danger"

        return render_template(
            "index.html",
            prediction_text=result,
            status=status
        )

    except Exception as e:
        return render_template(
            "index.html",
            prediction_text=f"Error: {str(e)}",
            status="danger"
        )

if __name__ == "__main__":
    app.run(debug=True)
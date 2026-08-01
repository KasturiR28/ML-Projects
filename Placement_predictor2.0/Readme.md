# 🎓 AI Student Placement Predictor

A Machine Learning-based web application that predicts whether a student is likely to be placed based on academic performance, skills, and extracurricular activities.

## 🚀 Features

- Predicts student placement chances using Machine Learning.
- Interactive and modern web interface built with Flask.
- Uses Random Forest Classifier for prediction.
- Responsive design with icons and professional UI.
- Real-time prediction results.

---

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- Font Awesome Icons

### Backend
- Python
- Flask

### Machine Learning
- Pandas
- NumPy
- Scikit-Learn
- Random Forest Classifier

---

## 📊 Dataset Features

The model uses the following student attributes:

| Feature | Description |
|----------|-------------|
| CGPA | Student's CGPA |
| Internships | Number of internships completed |
| Projects | Number of projects completed |
| WorkshopsCertifications | Workshops and certifications completed |
| AptitudeTestScore | Aptitude test score |
| SoftSkillsRating | Soft skills rating |
| ExtracurricularActivities | Participation in extracurricular activities |
| PlacementTraining | Placement training attended |
| SSC_Marks | 10th standard marks (%) |
| HSC_Marks | 12th standard marks (%) |

### Target Variable

- PlacementStatus
  - 1 = Placed
  - 0 = Not Placed

---

## 📂 Project Structure

```text
StudentPlacementPredictor/
│
├── app.py
├── model.pkl
├── placementdata.csv
├── requirements.txt
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/student-placement-predictor.git
```

### 2. Navigate to Project Directory

```bash
cd student-placement-predictor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open Browser

```text
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Model

The project uses a **Random Forest Classifier** trained on student placement data.

### Model Training Steps

1. Load dataset
2. Remove unnecessary columns
3. Split data into training and testing sets
4. Train Random Forest model
5. Evaluate model accuracy
6. Save model using Pickle

---

## 📈 Sample Prediction

### Input

```text
CGPA: 8.5
Internships: 2
Projects: 4
Workshops: 3
Aptitude Score: 85
Soft Skills Rating: 8
Extracurricular Activities: Yes
Placement Training: Yes
SSC Marks: 88
HSC Marks: 84
```

### Output

```text
🎉 High Chances of Placement
```

---

## 🔮 Future Enhancements

- Placement probability percentage
- Data visualization dashboard
- Student performance analytics
- Resume analysis integration
- Interview preparation recommendations
- Deployment on Render or Railway

---

## 👨‍💻 Author

**Kasturi Raskar**

Artificial Intelligence and Data Science Engineering Student

Machine Learning | AI | Web Development Enthusiast

---

## 📜 License

This project is developed for educational and learning purposes.
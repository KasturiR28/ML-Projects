# 📊 Customer Churn Prediction System

A Machine Learning-based web application that predicts whether a bank customer is likely to leave (churn) or stay with the bank based on demographic and account-related information.

The project uses a Random Forest Classifier trained on customer banking data and provides real-time predictions through an interactive Streamlit interface.

---

## 🚀 Features

- Predict customer churn probability.
- Interactive web interface using Streamlit.
- Real-time prediction results.
- Machine Learning-powered decision making.
- User-friendly input forms.
- Fast and lightweight deployment.

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- Scikit-Learn
- Random Forest Classifier
- StandardScaler

### Data Processing
- Pandas
- NumPy

### Web Framework
- Streamlit

---

## 📂 Project Structure

```text
Customer-Churn-Prediction/
│
├── app.py
├── random_forest_churn_model.pkl
├── scaler.pkl
├── Python_Implementation_for_churn_prediction.ipynb
├── requirements.txt
│
└── README.md
```

---

## 📊 Dataset Features

The model predicts customer churn using the following features:

| Feature | Description |
|----------|-------------|
| Credit Score | Customer credit score |
| Age | Customer age |
| Tenure | Years with the bank |
| Balance | Account balance |
| Number of Products | Products used by customer |
| Has Credit Card | Credit card ownership |
| Active Member | Active membership status |
| Estimated Salary | Customer salary |
| Geography | Customer country |
| Gender | Customer gender |

### Target Variable

| Value | Meaning |
|---------|---------|
| 0 | Customer Stays |
| 1 | Customer Exits |

---

## 🧠 Machine Learning Model

### Algorithm Used

- Random Forest Classifier

### Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Feature Encoding
      ↓
Feature Scaling
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Model Deployment
```

---

## 📈 Sample Prediction

### Input

```text
Credit Score: 700
Age: 35
Tenure: 5
Balance: 50000
Products: 2
Credit Card: Yes
Active Member: Yes
Salary: 60000
Country: Germany
Gender: Male
```

### Output

```text
Customer Will Stay
```

or

```text
Customer Will Exit
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/customer-churn-prediction.git
```

### Navigate to Project Folder

```bash
cd customer-churn-prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📌 Requirements

```text
streamlit
numpy
pandas
scikit-learn
```

---

## 📉 Business Impact

Customer churn prediction helps organizations:

- Identify customers at risk of leaving.
- Improve customer retention strategies.
- Increase profitability.
- Reduce customer acquisition costs.
- Improve customer satisfaction.

---

## 🔮 Future Improvements

- Churn probability percentage.
- Interactive analytics dashboard.
- Explainable AI using SHAP.
- Customer retention recommendations.
- Cloud deployment.
- Advanced ensemble models.

---

## 👨‍💻 Author

**Kasturi Raskar**

Artificial Intelligence and Data Science Engineering Student

Areas of Interest:
- Machine Learning
- Artificial Intelligence
- Data Science
- Web Development

---

## 📜 License

This project is developed for educational and learning purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub.
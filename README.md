# 🛡️ ShieldMail — Spam Mail & SMS Detector

**ShieldMail** is a real-time web application that detects whether an email or SMS message is **Spam** or **Not Spam** using a **Multinomial Naive Bayes Classifier**. Built with **Python**, **scikit-learn**, and **Streamlit**, the application processes raw text input, vectorizes it using `CountVectorizer`, and performs instant classification.

🔗 **Live Preview:** [https://shieldmail.streamlit.app/](https://shieldmail.streamlit.app/)

## 📸 Screenshots

#### 🖼️ Main Interface  
![Main UI](https://github.com/Turja1347/shield_mail/blob/246f5e6b48069dd452838f4bc43b193e757e583e/Screenshot%202025-07-06%20035905.png?raw=true)

#### 🔍 Spam Detection Output  
![Spam Output 1](https://github.com/Turja1347/shield_mail/blob/246f5e6b48069dd452838f4bc43b193e757e583e/Screenshot%202025-07-06%20003255.png?raw=true)  
![Spam Output 2](https://github.com/Turja1347/shield_mail/blob/246f5e6b48069dd452838f4bc43b193e757e583e/Screenshot%202025-07-06%20003329.png?raw=true)

## 📦 Features
- 🧠 Spam detection powered by **Multinomial Naive Bayes**
- 📊 **Interactive Web UI** built with **Streamlit**
- 🧹 **Preprocessed dataset** with duplicates removed and labels normalized
- 📬 **Real-time text input** and live predictions
- 🧪 Trained on **real-world SMS spam dataset**

## 🧠 Model Workflow

### 1. Load Dataset
- CSV file (`spam.csv`) containing two columns: `Category` and `Message`.

### 2. Data Preprocessing
- Remove duplicate rows  
- Normalize labels:  
  - `ham` → `Not Spam`  
  - `spam` → `Spam`

### 3. Train/Test Split
- 80% Training data  
- 20% Testing data

### 4. Text Vectorization
- Uses `CountVectorizer` from `scikit-learn`
- Removes English stopwords

### 5. Model Training
- Model: **Multinomial Naive Bayes**
- Trained on vectorized feature data

### 6. Prediction Pipeline
- Accepts user input via Streamlit
- Vectorizes input using the same `CountVectorizer`
- Outputs prediction: **Spam** or **Not Spam**

## 🚀 Getting Started

### 📥 Clone the Repository
```bash
git clone https://github.com/Turja1347/shield_mail.git
cd shieldmail
```

### 🧪 Install Dependencies
```bash
pip install -r requirements.txt
```

### ▶️ Run the App
```bash
streamlit run SpamDetection.py
```

## 📝 Dataset
The dataset used is derived from the [SMS Spam Collection](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset).  
- Format: CSV  
- Columns: `Category` (`spam` or `ham`), `Message` (text content)

## 📊 Evaluation Metrics
- **Accuracy:** ~98% on test data  
- **Precision & Recall:** Evaluated using `sklearn.metrics.classification_report`  
> Note: These metrics are dependent on the specific preprocessing and dataset version used.

## 📁 Project Structure
```
shieldmail/
├── SpamDetection.py        # Streamlit application
├── spam.csv                # Raw dataset
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


## 🤝 Acknowledgments
- Dataset: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
- Libraries: `scikit-learn`, `pandas`, `Streamlit`

## 💬 Contact
For questions or collaboration inquiries, please reach out to [Turja Mondal](https://www.linkedin.com/in/turjamondal01/).

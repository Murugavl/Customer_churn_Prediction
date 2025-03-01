# Customer Churn Prediction

## 📌 Overview
Customer churn prediction is a crucial task in business analytics, helping companies identify customers who are likely to leave and take preventive actions. This project utilizes **Machine Learning (ML)** techniques to analyze customer behavior and predict churn.

## 🔍 Features
- **Data Preprocessing:** Handles missing values, encodes categorical variables, and scales numerical data.
- **Exploratory Data Analysis (EDA):** Visualizes key trends in customer churn.
- **Machine Learning Models:** Implements multiple ML algorithms (Logistic Regression, Random Forest, SVM, etc.).
- **Model Evaluation:** Uses accuracy, precision, recall, and F1-score to assess performance.
- **Deployment:** Deploys the model using **Streamlit** for an interactive user interface.

## 🛠️ Technologies Used
- **Python** 
- **Pandas, NumPy** (Data Manipulation)
- **Matplotlib, Seaborn** (Visualization)
- **Scikit-Learn** (Machine Learning)
- **Streamlit** (Deployment)

## 📂 Project Structure
```
Customer_churn_Prediction/
│── dataset/               # Contains the dataset (CSV file)
│── notebooks/             # Jupyter notebooks for EDA & training
│── app.py                 # Streamlit app for prediction
│── requirements.txt       # List of dependencies
│── README.md              # Project Documentation
```

## 📊 Dataset
- The dataset includes customer information such as **demographics, account details, and usage patterns**.
- The target variable is **Churn** (0: Not Churned, 1: Churned).

## 🚀 Installation & Usage
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Murugavl/Customer_churn_Prediction.git
   cd Customer_churn_Prediction
   ```
2. **Create a Virtual Environment** *(Optional but recommended)*
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   venv\Scripts\activate     # For Windows
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

## 📌 Model Training
To train the model, run the Jupyter notebook available in the `notebooks/` folder:
```bash
jupyter notebook notebooks/Customer Churn Prediction.ipynb
```

## 💡 Future Improvements
- Enhance feature engineering for better model performance.
- Implement deep learning models for improved accuracy.
- Integrate customer segmentation for targeted retention strategies.

## 🤝 Contributing
Contributions are welcome! If you’d like to improve the project, fork the repository and submit a pull request.

## 📜 License
This project is licensed under the MIT License.


# Social Media Addiction Score Predictor

This project predicts a student's **social media addiction score (1–10)** based on lifestyle factors such as daily usage, relationship status, sleep hours, and mental health score.  
It also classifies the score into **Low, Medium, or High** addiction levels.


#  Features
- Predicts a **numerical addiction score** (1–10)  
- Categorizes addiction level:
  - **Low** (1–4)  
  - **Medium** (5–7)  
  - **High** (8–10)  
- **Streamlit web app** for user-friendly predictions  
- **Command-line tool** for quick predictions  
- **Visualization notebook** with key insights  


# 📊 Dataset
- **Source:** [Kaggle – Social Media Addiction vs Relationships](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)  
- Includes details like:
  - Age  
  - Gender  
  - Relationship_Status  
  - Avg_Daily_Usage (hours)  
  - Sleep_Hours  
  - Mental_Health_Score  


#  Tech Stack
- **Python 3**  
- **Machine Learning:** Scikit-learn (Random Forest Regressor)  
- **Visualization:** Matplotlib, Seaborn  
- **Web App:** Streamlit  
- **Other:** Pandas, NumPy, Joblib  


##  How to Run

### 1️⃣ Install Dependencies

pip install -r requirements.txt
2️⃣ Train the Model
python train_model.py


This creates the model file → addiction_model.pkl

3️⃣ Predict via CLI
python predict.py


Enter inputs manually → get score + addiction category 

4️⃣ Run the Web App
streamlit run app.py


📈 Visualizations

Addiction Score Distribution

Score vs Relationship Status
Correlation Heatmap

📦 Requirements (requirements.txt)
pandas
scikit-learn
numpy
joblib
streamlit
seaborn
matplotlib

# You can access the app using : https://radhika-ingale-social-media-addiction-score-predicto-app-axndrm.streamlit.app/

🙋 Author : Radhika Ingale

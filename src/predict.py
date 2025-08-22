import joblib
import numpy as np

# Load trained model
model = joblib.load('addiction_model.pkl')

print("📱 Social Media Addiction Score Predictor")

# Take user inputs
try:
    Age = int(input("Enter your age: "))
    Avg_Daily_Usage_Hours = float(input("Enter your average daily usage of social media (in hours): "))
    relationship_status = input("Enter your relationship status (Single / In Relationship / Complicated): ").strip()

    if relationship_status not in ['Single', 'In Relationship', 'Complicated']:
        raise ValueError("Invalid relationship status")

    Mental_Health_Score = int(input("Enter your mental health score (1–10): "))
    Sleep_Hours_Per_Night = float(input("Enter your average sleep hours per night: "))

    # Convert relationship status to numeric features
    relationship_score = {"In Relationship": 1, "Single": 2, "Complicated": 3}[relationship_status]
    relstatus_single = 1 if relationship_status == "Single" else 0
    relstatus_complicated = 1 if relationship_status == "Complicated" else 0

    # Construct input vector
    input_data = np.array([[Age, Avg_Daily_Usage_Hours, relationship_score, Mental_Health_Score, Sleep_Hours_Per_Night,
                            relstatus_single, relstatus_complicated]])

    # Predict score
    predicted_score = model.predict(input_data)[0]

    # Categorize score
    if predicted_score < 5:
        category = "Low"
    elif predicted_score <= 7:
        category = "Medium"
    else:
        category = "High"

    # Show output
    print(f"\nPredicted Addiction Score: {predicted_score:.2f}")
    print(f"Category: {category}")

except Exception as e:
    print(f"Error: {e}")

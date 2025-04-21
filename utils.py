import joblib
model = joblib.load("email_classifier.pkl")

def classify_email(text):
    return model.predict([text])[0]

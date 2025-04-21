import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import joblib
from masking import mask_pii

def train_and_save_model():
    df = pd.read_csv("data/emails.csv")
    df['masked_text'] = df['text'].apply(mask_pii)

    model = Pipeline([
        ("tfidf", TfidfVectorizer(stop_words="english")),
        ("clf", LogisticRegression(max_iter=300))
    ])
    model.fit(df['masked_text'], df['label'])
    joblib.dump(model, "email_classifier.pkl")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_and_save_model()

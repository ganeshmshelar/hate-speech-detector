import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
df = pd.read_csv("hate_speech_dataset.csv")
df['tweet'] = df['tweet'].astype(str)

# Features and labels
X = df['tweet']
y = df['class']  # 0: hate, 1: offensive, 2: clean

# Vectorization using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Model training using Naive Bayes
model = MultinomialNB()
model.fit(X_vec, y)

# Save trained model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("✅ Model training complete.")
print("📦 'model.pkl' and 'vectorizer.pkl' saved.")

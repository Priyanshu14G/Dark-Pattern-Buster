import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load the csv file
df = pd.read_csv("fake reviews dataset.csv")

print(df.head())

# Select independent and dependent variable
review = df['text_']
label = df['label']

# Split the dataset into train and test
review_train, review_test, label_train, label_test = train_test_split(review, label, test_size=0.35)

# TF-IDF Vectorization
tfidf_vectorizer = TfidfVectorizer()
review_train_tfidf = tfidf_vectorizer.fit_transform(review_train)
review_test_tfidf = tfidf_vectorizer.transform(review_test)

# Instantiate the model
classifier = RandomForestClassifier()

# Fit the model
classifier.fit(review_train_tfidf, label_train)

# Make pickle file of our model
pickle.dump(classifier, open("model.pkl", "wb"))

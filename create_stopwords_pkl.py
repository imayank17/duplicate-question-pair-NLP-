import pickle
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already downloaded
nltk.download('stopwords')

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Save to stopwords.pkl in current folder
with open('stopwords.pkl', 'wb') as f:
    pickle.dump(stop_words, f)

print("✅ stopwords.pkl created successfully!")

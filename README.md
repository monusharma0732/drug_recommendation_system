# 💊 Drug Recommendation System

A content-based drug recommendation system using TF-IDF and cosine similarity. Built with Python and deployed using Streamlit.

## 📁 Project Structure

```
drug_recommendation_system/
├── app.py               ← Streamlit frontend
├── drugs.csv            ← Sample drug dataset
├── tfidf_cosine.pkl     ← Vectorizer and similarity matrix
├── requirements.txt         ← Python dependencies
├── README.md                ← GitHub instructions
```

## 🚀 How to Run

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/drug_recommendation_system.git
cd drug_recommendation_system
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App
```bash
cd app
streamlit run app.py
```

## 📦 Dataset
The system uses a small sample dataset of drugs and their descriptions from `data/drugs.csv`.

## 🧠 Model
The backend uses:
- TF-IDF vectorizer
- Cosine similarity for recommendation

Enjoy exploring drug similarities!

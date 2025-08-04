import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("drugs.csv")

# Compute TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Description'])

# Compute cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations
def get_recommendations(drug_name, top_n=3):
    if drug_name not in df['Drug_Name'].values:
        return []
    idx = df[df['Drug_Name'] == drug_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:top_n + 1]
    recommended = [df.iloc[i[0]]['Drug_Name'] for i in sim_scores]
    return recommended

# Streamlit UI
st.title("💊 Drug Recommendation System")

selected_drug = st.selectbox("Select a Drug", df['Drug_Name'].values)

if st.button("Recommend Similar Drugs"):
    recommendations = get_recommendations(selected_drug)
    st.write("### Recommended Drugs:")
    for rec in recommendations:
        st.write(f"- {rec}")

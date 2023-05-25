import pickle
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import json

with open("data.pkl", "rb") as file:
    df = pickle.load(file)

clothing_descriptions = pickle.load(open('clothing_descriptions.pkl','rb'))
model = pickle.load(open('tfidf1.pkl','rb'))
model.fit(clothing_descriptions)
tfidf_vectors = model.transform(clothing_descriptions)
cosine_sim_matrix = cosine_similarity(tfidf_vectors, tfidf_vectors)

def get_top_similar_items(query, k):
    query_vector = model.transform([query])
    cosine_sim_scores = cosine_similarity(query_vector, tfidf_vectors)[0]
    top_indices = cosine_sim_scores.argsort()[-k:][::-1]
    top_similar_items = df.iloc[top_indices]
    top_similar_items = top_similar_items[['product_name', 'product_url']]
    output = []
    for _, row in top_similar_items.iterrows():
        item = {
            'product_name': row['product_name'],
            'url': row['product_url']
        }
        output.append(item)
    
    return json.dumps(output)
st.title("Similar clothing")
input = st.text_input("Query")
k = st.number_input('Number of similar items required', min_value=1, max_value=500, value=5, step=1)

if st.button('search'):
    output = get_top_similar_items(input,k)
    st.json(output)


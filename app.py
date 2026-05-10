import streamlit as st

from src.fetch_news import get_financial_news
from src.embed_store import (
    store_articles,
    search_articles
)

st.set_page_config(
    page_title="AI News Terminal",
    layout="wide"
)

st.title("📈 AI News Terminal")

query = st.text_input(
    "Ask About Markets",
    value="What is happening with NVIDIA?"
)

articles = get_financial_news(
    query="stock market",
    page_size=20
)

store_articles(articles)

results = search_articles(query)

st.subheader("AI Semantic Search Results")

documents = results["documents"][0]

for doc in documents:

    st.markdown("### Relevant Insight")

    st.write(doc)

    st.divider()

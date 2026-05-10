import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.Client()

collection = client.get_or_create_collection(
    name="financial_news"
)


def store_articles(articles):

    documents = []
    ids = []

    for idx, article in enumerate(articles):

        title = article.get("title", "")
        description = article.get("description", "")

        content = f"{title}. {description}"

        documents.append(content)

        ids.append(str(idx))

    embeddings = model.encode(documents).tolist()

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )


def search_articles(query, n_results=5):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results

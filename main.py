
# from langchain_groq import ChatGroq
# 
# llm = ChatGroq(
#     model="llama-3.1-70b-versatile",
#     groq_api_key="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",
#     temperature=0,
# )
# 
# response = llm.invoke("who is the prime minister of india?")
# print(response.content)

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://www.espn.com/")
docs = loader.load().pop().page_content
print(docs)

# import chromadb
# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="my_collection")
#
# collection.add(
#     documents=[
#         "This is a document about pineapple",
#         "This is a document about oranges",
#         "iam dulquar salman his age is 30"
#     ],
#     ids=["id1", "id2", "id3"]
# )
# results = collection.query(
#     query_texts=["who is dulquer"], # Chroma will embed this for you
#     n_results=2 # how many results to return
# )
# print(results)

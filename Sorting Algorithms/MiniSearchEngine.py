from collections import defaultdict

documents = [
    "the quick brown fox jumps over the lazy dog",
    "never jump over the lazy dog quickly",
    "a fast brown fox leaps over a lazy dog",
    "the fox",
    "the dog",
    "the lazy dog",
    "quickly"
]

def create_index(docs):
    index = defaultdict(list)
    for i, doc in enumerate(docs):
        words = doc.split()
        for word in words:
            index[word].append(i)
    return index

def search(query, index):
    query_words = query.split()
    if not query_words:
        return []
    
    doc_lists = [set(index[word]) for word in query_words if word in index]
    
    if not doc_lists:
        return []
    
    result_docs = set.intersection(*doc_lists)
    return list(result_docs)

def rank_results(query, results, docs):
    query_words = query.split()
    ranked_results = []

    for doc_index in results:
        doc = docs[doc_index]
        word_count = sum(doc.split().count(word) for word in query_words)
        ranked_results.append((word_count, doc_index))
    
    ranked_results.sort(reverse=True, key=lambda x: x[0])
    return [doc_index for _, doc_index in ranked_results]

def main():
    index = create_index(documents)
    while True:
        query = input("Enter search query (or 'exit' to quit): ").strip()
        if query == 'exit':
            break
        results = search(query, index)
        ranked_results = rank_results(query, results, documents)
        print(f"Documents matching '{query}': {ranked_results}")
        for idx in ranked_results:
            print(documents[idx])

if __name__ == "__main__":
    main()

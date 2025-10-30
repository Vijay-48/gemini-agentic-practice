from ddgs import DDGS


def web_search(query, max_results=5):
    """
    Searches the web for a given query and returns a list of text snippets.
    Uses DuckDuckGo, which is privacy-friendly and free.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            results.append(r["body"])
    return results

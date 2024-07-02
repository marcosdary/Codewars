class Search:
    def __init__(self, arr) -> None:
        self.arr = arr

    def word_seq(self, query):
        return list(
            filter(
                lambda w: query.lower() in w.lower()
            ), self.arr
        )

def word_search(query, seq):
    
    return None if Search(seq).word_seq(query) == [] else Search(seq).word_seq(query)

print('ab' in 'abc')
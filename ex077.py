# A classe foi projetada para receber uma matriz de valores e um número inteiro indicando quantos itens serão permitidos por cada página

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection:list, items_per_page:int):
        self._collection = collection
        self._items_per_page = items_per_page
        

    # retorna o número de itens de toda a coleção
    def item_count(self):
        return len(self._collection)

    # retorna o número de páginas
    def page_count(self):
        s = 0
        for i in range(0, len(self._collection), self._items_per_page):
            s += 1
        return s
    
    # retorna o número de itens na página fornecida. page_index é baseado em zero
    # este método deve retornar -1 para valores page_index que estão fora do intervalo
    def page_item_count(self, page_index):

        t = 0
        for i in range(0, len(self._collection), self._items_per_page):
            t += 1

        if t > page_index and page_index >= 0: 
            s = 0
            for i in range(0, len(self._collection), self._items_per_page):
                subarray = self._collection[i:i+self._items_per_page]
                print(page_index, s)
                if page_index == s:
                    return len(subarray)
                s += 1
        return -1
    
    # determina em qual página um item de um determinado índice está. Índices baseados em zero.
    # este método deve retornar -1 para valores item_index que estão fora do intervalo
    def page_index(self, item_index):
        if len(self._collection) > item_index and item_index >= 0:
            s = 0
            l = 0
            for i in range(0, len(self._collection), self._items_per_page):
                subarray = self._collection[i:i+self._items_per_page]
                print(subarray, self._collection[item_index])
                if self._collection[item_index] in subarray:
                    l = s
                s += 1
            return l
        return -1

helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_index(2))

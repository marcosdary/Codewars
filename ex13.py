from collections import Counter

def duplicate_count(text:str) -> int:
    text = text.lower()
    caracters = set(
        filter(
            lambda x: text.count(x) >= 2,
            text
        )
    )
    return len(caracters)

print(duplicate_count("Indivisibilities"))

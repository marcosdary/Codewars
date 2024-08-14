def wave(string: str) -> list[str]:

    strings = [
        string[0:i]+string[i].upper()+string[i+1:] if string[i] != " " or i > 0
        else string[i].upper()+string[i+1:]
        for i in range(0, len(string))
    ]

    strings = list(
        filter(lambda strig: strig != string, strings)
    )
    return strings


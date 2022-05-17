def my_copy(one_name=True):
    d = [
        ("Hendrix", "1942"),
        ("Allman", "1946"),
        ("King", "1925"),
        ("Clapton", "1945"),
        ("Johnson", "1911"),
        ("Berry", "1926"),
        ("Vaughan", "1954"),
        ("Cooder", "1947"),
        ("Page", "1944"),
        ("Richards", "1943"),
        ("Hammett", "1962"),
        ("Cobain", "1967"),
        ("Garcia", "1942"),
        ("Beck", "1944"),
        ("Santana", "1947"),
        ("Ramone", "1948"),
        ("White", "1975"),
        ("Frusciante", "1970"),
        ("Thompson", "1949"),
        ("Burton", "1939"),
    ]

    if one_name:  
        dct = {year: musician for musician, year in d}
        for year in dct:
            print(year + " : " + dct[year])
    else:
        dct = {}
        for musician, year in d:
            if year not in dct:
                dct[year] = []
            dct[year].append(musician)
        for year in dct:
            print(year + " : " + ', '.join(dct[year]))


if __name__ == "__main__":
    # my_copy()
    my_copy(False)

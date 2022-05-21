import sys
from bs4 import BeautifulSoup
import requests

WIKI_URL = "https://en.wikipedia.org/wiki/"
TO_FIND = 'Philosophy'


def find_phylosofia(page, previuos=[]):
    try:
        res = requests.get(WIKI_URL + page)
        res.raise_for_status()
    except requests.HTTPError as e:
        if (res.status_code == 404):
            print("It's a dead end !")
        else:
            print(e)
        return False, 1
    soup = BeautifulSoup(res.text, "html.parser")
    title = soup.h1.text
    if title in previuos:
        print("Found loop")
        return False, 1
    else:
        previuos.append(title)
    if title == TO_FIND:
        return True, 1
    
    links = soup.find_all('a', href=True)
    for link in links:
        if link.get("href").startswith("/wiki/") and not link.get("class") and not link.find_parent("td"):
            new_page = link.get("href").replace("/wiki/", "")
            if "/" not in new_page: # found page

                # print("go to ", new_page)
                # print("previous: ", link.previous)
                ans, deep = find_phylosofia(new_page, previuos)
                return ans, deep + 1
    print("nothing found")
    return False, 1






    with open(f"res_{page}.html", "w") as f: # only for debugging
        f.write(str(soup))
    return page + "\n" + "piu", 1


def main():
    if (len(sys.argv) != 2):
        print("incorrect argumetns count")
        return
    page_name = sys.argv[1].replace('\\', '')
    previous = []
    ans, deep = find_phylosofia(page_name, previous)
    if ans:
        print('\n'.join(previous), f"deep ={deep}")




if __name__ == '__main__':
    main()
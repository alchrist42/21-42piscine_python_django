import requests
import json
import dewiki
import sys


def return_wiki_page(page_name: str):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": page_name,
        "prop": "wikitext",
        "format": "json",
        "redirects": "true"
    }
    res = requests.get(url, params=params)
    if res.status_code != 200:
        return Exception(f"request error code: {res.status_code}")
    data = json.loads(res.text)
    if data.get("error"):
        raise Exception(data["error"]["info"])
    # return json.dumps(data["parse"]["wikitext"])
    return dewiki.from_string(data["parse"]["wikitext"]["*"])


def main():
    if (len(sys.argv) != 2):
        print("incorrect argumetns count")
        return
    page_name = sys.argv[1]
    try:
        wiki_data = return_wiki_page(page_name)
        with open(f"{page_name}.wiki", "w") as f:
            f.write(wiki_data)
    except Exception as e:
        return print(e)



if __name__ == '__main__':
    main()
import sys
from antigravity import geohash


def main():
    if len(sys.argv) != 4:
        print("Use: python3 geohashing.py <latitude> <longtitude> <date>")
        exit()
    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
    except Exception as e:
        return print(e)
    try:
        date_dow = sys.argv[3].encode("utf-8")
    except:
        return print(e)
        
    geohash(latitude, longitude, date_dow)


if __name__ == "__main__":
    main()

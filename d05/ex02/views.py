import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def init(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES["default"]["NAME"],
            user=settings.DATABASES["default"]["USER"],
            password=settings.DATABASES["default"]["PASSWORD"],
            host=settings.DATABASES["default"]["HOST"],
            port=settings.DATABASES["default"]["PORT"],
        )
        with conn.cursor() as curs:
            curs.execute(
                """
            CREATE TABLE ex02_movies(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
                );
            """
            )
            curs.execute("commit")
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)


def populate(request):
    data = [
        [1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"],
        [2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"],
        [3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"],
        [4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"],
        [
            5,
            "The Empire Strikes Back",
            "Irvin Kershner",
            "Gary Kurtz, Rick McCallum",
            "1980-05-17",
        ],
        [
            6,
            "Return of the Jedi",
            "Richard Marquand",
            "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "1983-05-25",
        ],
        [
            7,
            "The Force Awakens",
            "J. J. Abrams",
            "Kathleen Kennedy, J. J. Abrams, Bryan Burk",
            "2015-12-11",
        ],
    ]
    results = []
    conn = psycopg2.connect(
        dbname=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        host=settings.DATABASES["default"]["HOST"],
        port=settings.DATABASES["default"]["PORT"],
    )
    for line in data:
        try:

            with conn.cursor() as cur:
                values_str = ", ".join(str(x) for x in line)
                print(values_str)
                req_str = """
        INSERT INTO ex02_movies
        (
            episode_nb,
            title,
            director,
            producer,
            release_date
        )
        VALUES
        (
            %s, %s, %s, %s, %s
        );
        """
                cur.execute(req_str, line)
                cur.execute("commit")
                results.append("OK")
        except Exception as e:
            results.append(e)
    return HttpResponse("\n<br>".join(map(str, results)))


def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES["default"]["NAME"],
            user=settings.DATABASES["default"]["USER"],
            password=settings.DATABASES["default"]["PASSWORD"],
            host=settings.DATABASES["default"]["HOST"],
            port=settings.DATABASES["default"]["PORT"],
        )
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM ex02_movies;")
            movies = cur.fetchall()
    except Exception as e:
        return HttpResponse(e)
    if movies:
        return render(request, "ex02/display.html", {"movies": movies})
    return HttpResponse(f"No data available")
    

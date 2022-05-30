import psycopg2
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UpdateForm

TABLE = "ex06_movies"

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
            CREATE TABLE {table}(
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb INT PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP NOT NULL DEFAULT NOW(),
                updated TIMESTAMP NOT NULL DEFAULT NOW()
                );

            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON {table} FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
            """.format(table=TABLE)
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
        INSERT INTO {table}
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
        """.format(table=TABLE)
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
            cur.execute(f"SELECT * FROM {TABLE};")
            movies = cur.fetchall()
    except Exception as e:
        return HttpResponse(e)
    if movies:
        return render(request, "ex06/display.html", {"movies": movies})
    return HttpResponse(f"No data available")


def update(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES["default"]["NAME"],
            user=settings.DATABASES["default"]["USER"],
            password=settings.DATABASES["default"]["PASSWORD"],
            host=settings.DATABASES["default"]["HOST"],
            port=settings.DATABASES["default"]["PORT"],
        )
        with conn.cursor() as cur:
            cur.execute(f"SELECT * FROM {TABLE};")
            movies = cur.fetchall()
    except Exception as e:
        return HttpResponse(e)
    titles = [(movie[0], movie[0]) for movie in movies]

    if request.method == 'POST':
        form = UpdateForm(titles, request.POST)
        if form.is_valid():
            movie_to_upd = form.cleaned_data['title']
            opening_crawl = form.cleaned_data['opening_crawl']
            sql_req = f"UPDATE {TABLE} SET opening_crawl = %s WHERE title = %s"
            try:
                with conn.cursor() as cur:
                    cur.execute(sql_req, [opening_crawl, movie_to_upd])
                    conn.commit()
                    msg = f"{movie_to_upd} updated"
                    print(msg)
                    cur.execute(f"SELECT * FROM {TABLE};")
                    movies = cur.fetchall()
            except Exception as e:
                print(e)
                msg = e
        else:    
            msg = "invalid form"

    elif request.method == 'GET':
        msg = ""
    return render(request, 'ex06/update.html', {'form': UpdateForm(titles), "movies": movies, "msg": msg})

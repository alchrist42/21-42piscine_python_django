#!/usr/bin/python3
import os
from pydoc import describe
import sys
import settings


def main():
    if len(sys.argv) != 2:
        return print("Wrong argument count")
    file_name = sys.argv[1]
    if not file_name.endswith(".template"):
        return print("Wrong extension <*.template>")
    try:
        with open(file_name) as f:
            template = f.read()
    except:
        return print("Cannot open template file")

    cv_html = template.format(
        name=settings.name.title(),
        surname=settings.surname.title(),
        profession=settings.profession.upper(),
        company=settings.company,
        description=settings.description,
        country=settings.country.title(),
        age=settings.age,
        email=settings.email
    )
    cv_file_name = f"CV_{settings.name.title()}_{settings.surname.title()}.html"
    with open(cv_file_name, "w") as f:
        f.write(cv_html)


if __name__ == "__main__":
    main()

class Element:
    def __init__(self, line):
        self.parse(line.rstrip("\n"))

    def parse(self, line):
        self.name, line = line.split(" = ")
        dct = {arg.split(":")[0]: arg.split(":")[1] for arg in line.split(", ")}
        self.small_name = dct.pop("small").lstrip()
        self.position: int = int(dct.pop("position"))
        self.number: int = int(dct.pop("number"))
        self.molar: float = float(dct.pop("molar"))
        self.electron: list[int] = [int(x) for x in dct.pop("electron").split()]


def main():
    HTML = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Periodic table</title>
    <link rel="stylesheet" href="periodic_table.css" />
</head>
<body>
    <table>
        <tr>
{body}
        </tr>
    </table>
</body>

</html>
"""

    TEMPLATE = """\
            <td class="filled{td_class}">
                <h4>{name}</h4>
                <ul>
                    <li class="number">{number}</li>
                    <li class="small">{small}</li>
                    <li>{molar}</li>
                    <li class="electron">Energy levels<br><span>{electron}</span></li>
                </ul>
            </td>
"""

    body = ""
    with open("periodic_table.txt") as f:
        elements = [Element(line) for line in f.readlines()]

    last_position = 0
    for el in elements:
        if el.position < last_position:
            body += "    </tr>\n        <tr>"
        body += "            <td></td>\n" * (el.position - last_position - 1)
        last_position = el.position
        body += TEMPLATE.format(
            name=el.name,
            number=el.number,
            small=el.small_name,
            molar=el.molar,
            electron=", ".join(map(str, el.electron)),
            td_class=" noble" * (el.position == 17),
        )
    with open("periodic_table.html", "w") as f:
        f.write(HTML.format(body=body))


if __name__ == "__main__":
    main()

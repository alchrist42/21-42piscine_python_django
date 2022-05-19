from elem import Elem, Text


def ClassFactory(name, argnames, BaseClass=Elem):
    def __init__(self, *args, **kwargs):
        if kwargs.keys() & argnames.keys():
            raise TypeError(
                f"Arguments {(kwargs.keys() & argnames.keys())} not valid for {self.__class__.__name__}"
            )
        merged_kwargs = kwargs | argnames
        BaseClass.__init__(self, *args, **merged_kwargs)

    newclass = type(name, (BaseClass,), {"__init__": __init__})
    return newclass


SIMPLE_CLASS_NAMES = ["Meta", "Img"]
DOUBLE_CLASS_NAMES = [
    "Html",
    "Head",
    "Body",
    "Title",
    "Table",
    "Th",
    "Tr",
    "Td",
    "Ul",
    "Ol",
    "Li",
    "H1",
    "H2",
    "P",
    "Div",
    "Span",
    "Hr",
    "Br",
]

# have to be in global scope
for name in SIMPLE_CLASS_NAMES:
    globals()[name] = ClassFactory("Body", {"tag": name.lower(), "tag_type": "simple"})

for name in DOUBLE_CLASS_NAMES:
    globals()[name] = ClassFactory("Body", {"tag": name.lower(), "tag_type": "double"})


def test():
    print(Html([Head(), Body()]))
    try:
        html = Html(Text("Hey, dude"), tag="div")
        print(html)
    except TypeError as e:
        print(e)


def simple_page():
    html = Html(
        [
            Head(Title(Text("Hello ground!"))),
            Body(
                [
                    H1(Text("Oh no, not again!")),
                    Img(attr={"src": "http://i.imgur.com/pfp3T.jpg"}),
                ]
            ),
        ]
    )
    print(html)


if __name__ == "__main__":
    test()
    simple_page()

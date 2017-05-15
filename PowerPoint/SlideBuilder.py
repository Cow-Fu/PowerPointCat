from bs4 import BeautifulSoup
from Slide import Slide

events = {}
class SlideBuilder:
    def traverseTree(self, markup):
        soup = markup
        if not isinstance(soup, BeautifulSoup):
            soup = BeautifulSoup(markup, "lxml")
        keys = events.keys()
        text = ""
        for node in soup.recursiveChildGenerator():
            if node.name in keys:
                text += events[node.name](node)
        return text

    def build(self, markup):
        soup = BeautifulSoup(markup, "lxml")
        sections = list(filter(lambda x: x.name == "p:sp", soup.recursiveChildGenerator()))

        title = traverseTree(sections[0])
        content = traverseTree(sections[1])

        return Slide(title, content)


def on(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print("hi " + name)
        events[name] = func
        return wrapper
    return decorator

if __name__ == '__main__':
    @on("Steve")
    def test():
        pass

    print(events)

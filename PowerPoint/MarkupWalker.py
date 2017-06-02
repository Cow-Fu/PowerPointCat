from bs4 import BeautifulSoup

class MarkupWalker:
    def traverseTree(self, markup):
        soup = markup
        if not isinstance(soup, BeautifulSoup):
            soup = BeautifulSoup(markup, "lxml")
        keys = self.events.keys()
        outputs = []
        for node in soup.recursiveChildGenerator():
            if node.name in keys:
                outputs.append(self.events[node.name](node))
        return outputs

    def on(self, name):
        def decorator(func):
            def wrapper(*args, **kwargs):
                pass
            self.events[name] = func
            return wrapper
        return decorator

    def getEvents(self):
        return self.events

    def __init__(self):
        self.events = {}

if __name__ == '__main__':
    mw = MarkupWalker()
    @mw.on("Steve")
    def test():
        pass

    print(mw.getEvents())

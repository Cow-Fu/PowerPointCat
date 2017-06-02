
class Slide:
    def getTitle(self):
        return self.titles

    def setTitle(self, titles):
        self.self.titles = titles

    def getContent(self):
        return contentHolders

    def setContent(self, content):
        self.content = content

    def getMarkup(self):
        return self.markup

    def setMarkup(self, markup):
        self.self.markup = markup

    def __init__(self, title=None, content=None, markup=None):
        self.title = title
        self.content = content
        self.markup = markup


class Slide:
    def addTitle(self, title):
        self.titles = title
        
    def addContent(self, content):
        self.addContent = content

    def __init__(self, titles=None, contentHolders=None):
        self.titles = titles
        self.contentHolders = contentHolders

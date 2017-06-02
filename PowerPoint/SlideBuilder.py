from .MarkupWalker import MarkupWalker
from .Slide import Slide
from bs4 import BeautifulSoup

mw = MarkupWalker()

class SlideBuilder:
    @staticmethod
    @mw.on("a:t")
    def handleTextNode(soup):
        return soup.text

    @staticmethod
    @mw.on("a:endpararpr")
    def handleNewLine(soup):
        return "\n"

    @staticmethod
    def build(markup):
        result = mw.traverseTree(markup)
        slideText = ""
        for x in result:
            if x == " ":
                slideText += "\\n"
            else:
                slideText += x
        slide = slideText.split("\n")

        title = slide[0].replace("\\n", "\n")
        content = slide[1:]
        content = list(map(lambda x: x.replace("\\n", "\n"), slide[1:]))


        return Slide(title="".join(title), content="".join(content), markup=markup)



    # def __init__(self):
    #     self.mw = MarkupWalker()

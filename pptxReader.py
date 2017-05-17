from zipfile import ZipFile
from bs4 import BeautifulSoup
from glob import iglob
import re

class PowerPointReader:
    _regex = re.compile(r".*?(\d+)\.xml")  # regex to extract the slide number
    _sorter = lambda x: int(PowerPointExtractor._regex.match(x).group(1))

    def findall(self, fp):
        return iglob("{}**/*.pptx".format(fp))

    def build(self, target):
        self.f = ZipFile(target)

    def _getSlides(self):
        slides = list(filter(lambda x: x.startswith("ppt/slides/") and x.endswith(".xml"),
            self.f.namelist()))
        return sorted(slides, key=lambda x: PowerPointExtractor._sorter(x))
    #
    # def __enter__(self):
    #     return self
    #
    # def __exit__(self, exc_type, exc_value, traceback):
    #     self.f.close()

# def readPptx(fp):
    # with ZipFile(fp) as f:
        # slides = list(filter(lambda x: x.startswith("ppt/slides/") and x.endswith(".xml"), f.namelist()))
        # slides = sorted(slides, key=PowerPointExtractor._sorter)
        # print(slides)
        # with f.open(slides[5]) as f:
            # bs = BeautifulSoup(f.read(), "lxml")
            # print(bs.prettify())
            # textBody = list(filter(lambda x: x.name == "p:txbody", bs.recursiveChildGenerator()))
            # text = []
            # for node in textBody:
            #     text.append(list(filter(lambda x: x.name == "a:t", node.recursiveChildGenerator())))
            # temp = []
            # for i in text:
            #     temp.extend(map(lambda x: x.text, i))
            # return "".join(temp)




targets = [x for x in iglob("**/*.pptx", recursive=True)]

powerpoints = []

from zipfile import ZipFile
from bs4 import BeautifulSoup
from glob import iglob
import re

class PowerPointCat:
    _regex = re.compile(r".*?(\d+)\.xml")  # regex to extract the slide number
    _sorter = lambda x: int(PowerPointCat._regex.match(x).group(1))

    def getFilePath(self):
        return self.fp

    def getSlides(self):
        return self.slides

    def _getSlides(self):
        slides = list(filter(lambda x: x.startswith("ppt/slides/") and x.endswith(".xml"),
            self.f.namelist()))
        return sorted(slides, key=lambda x: PowerPointCat._sorter(x))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()

    def __init__(self, fp):
        self.fp = fp
        self.f = ZipFile(self.fp)
        self.slides = self._getSlides()

# def readPptx(fp):
#     with ZipFile(fp) as f:
#         slides = list(filter(lambda x: x.startswith("ppt/slides/") and x.endswith(".xml"), f.namelist()))
#         slides = sorted(slides, key=PowerPointCat._sorter)
#         # print(slides)
#         with f.open(slides[5]) as f:
#             bs = BeautifulSoup(f.read(), "lxml")
#             print(bs.prettify())
#             textBody = list(filter(lambda x: x.name == "p:txbody", bs.recursiveChildGenerator()))
#             text = []
#             for node in textBody:
#                 text.append(list(filter(lambda x: x.name == "a:t", node.recursiveChildGenerator())))
#             temp = []
#             for i in text:
#                 temp.extend(map(lambda x: x.text, i))
#             return "".join(temp)

targets = [x for x in iglob("**/*.pptx", recursive=True)]
# print(targets[8])
readPptx(targets[8])

# with PowerPointCat(targets[1]) as p:
#     print(p.getSlides())

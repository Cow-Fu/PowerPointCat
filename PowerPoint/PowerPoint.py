
class PowerPoint:
    def getName(self):
        return self.name

    def getFp(self):
        return self.fp
        
    def getSlides(self):
        return self.slides
    # def readFromSlide(self, slideNumber):
    #      with self.f.open(self.slides[slideNumber - 1]) as f:
    #         soup = BeautifulSoup(f.read(), "lxml")
    #         textBody = list(filter(lambda x: x.name == "p:txbody", soup.recursiveChildGenerator()))
    #         text = []
    #         for node in textBody:
    #             text.append(list(filter(lambda x: x.name == "a:t", node.recursiveChildGenerator())))
    #         string = ""
    #         for x in [x for x in text]:
    #             for txt in [y.text for y in x]:
    #                 if txt in [".", "?", "!"]:
    #                     string = string[:len(string) - 1]
    #                 if not txt.endswith(" "):
    #                     string += txt + "\n"
    #                     continue
    #                 string += txt
    #         return string.strip()
    def __init__(self, name, fp, slides):
        self.name = name
        self.fp = fp
        self.slides = slides


class PowerPoint:
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        return self

    def getFp(self):
        return self.fp

    def setFp(self, fp):
        self.fp = fp
        return self

    def getSlides(self):
        return self.slides

    def setSlides(self, slides):
        self.slides = slides
        return self


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

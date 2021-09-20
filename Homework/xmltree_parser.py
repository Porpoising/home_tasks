from xml.etree.ElementTree import XMLParser


class ColorCounter:
    red, green, blue = 0, 0, 0
    count = 0

    def start(self, tag, attrib):
        self.count += 1
        if attrib['color'] == 'red':
            self.red += self.count
        elif attrib['color'] == 'green':
            self.green += self.count
        elif attrib['color'] == 'blue':
            self.blue += self.count

    def end(self, tag):
        self.count -= 1

    def data(self, data):
        pass

    def close(self):
        print(self.red, self.green, self.blue, sep=' ')


target = ColorCounter()
parser = XMLParser(target=target)
parser.feed(input().strip())
parser.close()

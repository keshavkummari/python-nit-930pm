#!/usr/bin/python3
import xml.sax

class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.author = ""
        self.title = ""
        self.genre = ""
        self.price = ""
        self.publish_date = ""
        self.description = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "book":
            title = attributes["id"]
            print(title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "author":
            print("was written by", self.author)

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = BookHandler()
    parser.setContentHandler(Handler)

    parser.parse("books.xml")
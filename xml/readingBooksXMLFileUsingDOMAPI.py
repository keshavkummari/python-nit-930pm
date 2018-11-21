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
            print("*****Books*****")
            title = attributes["id"]
            print("id:", title)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "author":
            print("Author:", self.author)
        elif self.CurrentData == "title":
            print("Title:", self.title)
        elif self.CurrentData == "genre":
            print("Genre:", self.genre)
        elif self.CurrentData == "price":
            print("Price:", self.price)
        elif self.CurrentData == "publish_date":
            print("Publish_date:", self.publish_date)
        elif self.CurrentData == "description":
            print("Description:", self.description)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "author":
            self.author = content
        elif self.CurrentData == "title":
            self.title = content
        elif self.CurrentData == "genre":
            self.genre = content
        elif self.CurrentData == "price":
            self.price = content
        elif self.CurrentData == "publish_date":
            self.publish_date = content
        elif self.CurrentData == "description":
            self.description = content


if (__name__ == "__main__"):
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # override the default ContextHandler
    Handler = BookHandler()
    parser.setContentHandler(Handler)

    parser.parse("books.xml")
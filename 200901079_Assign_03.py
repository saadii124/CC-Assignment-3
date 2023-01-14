import xml.etree.ElementTree as ET
import csv
class Dom2Parser:
    def __init__(self):
        self.xml_file = ET.parse("compiler.xml")
        self.root = self.xml_file.getroot()
        self.book_div = self.root.find("book")

    def print_parsed_data(self):
      with open("mycsv.csv" , "w",newline='') as file:
        csvreader = csv.writer(file)
        csvreader.writerow(["Book_Id","Author_Name","Title","Genre","Price", "Publish_date","Description"])
        for child in self.xml_file.getroot():
            print("Book_Id:", child.attrib)
            print("Author_Name:", child.find("author").text)
            print("Title:", child.find("title").text)
            print("Genre:", child.find("genre").text)
            print("Price:", child.find("price").text)
            print("Publish_date:", child.find("publish_date").text)
            print("Description:", child.find("description").text)
            print()
            csvreader.writerow([child.attrib['id'],
                                child.find("author").text,
                                child.find("title").text,
                               child.find("genre").text,child.find("price").text,
                               child.find("publish_date").text,
                               child.find("description").text]
                               )
            #self.book_div = self.book_div.find("book")

    def write_to_file(self):
        with open("parsed_data.txt", "w") as f:
            for child in self.xml_file.getroot():
                print("Book_Id:", child.attrib)
                print("author:", child.find("author").text)
                print("title:", child.find("title").text)
                print("genre:", child.find("genre").text)
                print("price:", child.find("price").text)
                print("publish_date:", child.find("publish_date").text)
                print("description:", child.find("description").text)
                print()

if __name__ == "__main__":
    parser = Dom2Parser()
    parser.print_parsed_data()
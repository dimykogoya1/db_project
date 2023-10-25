import os
from lxml import html
from xml.etree import ElementTree as ET

# Set the HTML file path
REPORTS = "/Users/dimy/Documents/Fall Class 2023/dimykogoya1:Dproject/db_project/html/adams-public-library.html"

def reader(doc):
    data = []
    for report in os.scandir(doc):
        data.append(report.path)
    return data

def read_html(file_path: str):
    parser = html.HTMLParser(remove_blank_text=True)
    with open(file_path, encoding="windows-1252") as file:
        return html.parse(file, parser)

def file_reader(docs):
    data = []
    for x in reader(doc=docs):
        data.append(read_html(x))
    return data

def extract_elements_from_html(file_path):
    with open(file_path, encoding="windows-1252") as file:
        tree = html.parse(file)
        root = tree.getroot()
        # Print the link elements for the institution class
        links = root.xpath('//a')
        for link in links:
            print(link.text, link.get('href'))        
       
        # Extract and print specific elements from the HTML file
        h3_elements = root.xpath('//h3')
        div_elements = root.xpath('//div')

        for h3_element in h3_elements:
            print("h3 Element:", h3_element.text)

        for div_element in div_elements:
            print("div Element:", div_element.text)

def main():
    # Iterate through all HTML files in the directory
    for filename in os.listdir(os.path.dirname(REPORTS)):
        if filename.endswith(".html"):
            file_path = os.path.join(os.path.dirname(REPORTS), filename)
            print("Extracting elements from:", file_path)
            extract_elements_from_html(file_path)
            print("\n")

if __name__ == "__main__":
    main()

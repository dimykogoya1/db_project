import os
from lxml import html, etree
from xml.etree import ElementTree as ET


REPORTS = "/Users/dimy/Documents/Fall Class 2023/dimykogoya1:Dproject/db_project/html"

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


def extract_attribute(element, tag, attribute, text, val):
    alpha = element.xpath(f"//{tag}[@{attribute}='{text}']")[0]
    return alpha.get(val, "Not Found")

def extract_municipality(root):
    municipality = root.xpath('//p[@class="institutionmunicipality"]/@value')
    if municipality:
        return municipality[0]
    else:
        return "Municipality not found"

def extract_elements_from_html(file_path):
    with open(file_path, encoding="windows-1252") as file:
        tree = read_html(file_path)
        root = tree.getroot()

        data = {}
        data['institution'] = root.xpath('//input[@name="institutionname"]/@value')[0]
        data['address'] = root.xpath('//input[@name="institutionaddress1"]/@value')[0]
        data['address2'] = root.xpath('//input[@name="institutionaddress2"]/@value')[0]
        data['code'] = root.xpath('//input[@id="instituticode"]/@value')[0]
        data['municipality'] = extract_municipality(root)
        data['zip_code'] = root.xpath('//input[@name="institutionzip"]/@value')[0]
        data['state'] = root.xpath('//input[@name="institutionstate"]/@value')[0]
              
        return data

def extract_select_elements(file_path):
    tree = read_html(file_path)
    root = tree.getroot()
    
    city = root.xpath("//select[@name='institutioncity']")[0]
    
    data = city.iterchildren("option")
    first = next(data)
    
    return first.text

def main():
    institution_data_list = []

    for filename in os.scandir(REPORTS):
        if filename.name.endswith(".html"):
            file_path = filename.path
            print("Extracting data:", file_path)

            institution_data = extract_elements_from_html(file_path)
            institution_data['city'] = extract_select_elements(file_path)
            institution_data_list.append(institution_data)

    for data in institution_data_list:
        print(data)

if __name__ == "__main__":
    main()
import os
from lxml import html, etree
from xml.etree import ElementTree as ET

# Set the HTML file path
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

  

def extract_elements_from_html(file_path):
    with open(file_path, encoding="windows-1252") as file:
        tree = html.parse(file)
        root = tree.getroot()
    
        data = {}
        data['entity'] = root.xpath('//input[@name="institutionname"]/@value')[0]
        data['institution'] = root.xpath('//input[@id="institutionname"]/@value')[0]
        data['address'] = root.xpath('//input[@id="institutionaddress1"]/@value')[0]
        data['address2'] = root.xpath('//input[@id="institutionaddress2"]/@value')[0]
        data['code'] = root.xpath('//input[@id="instituticode"]/@value')[0]
        data['municipality'] = root.xpath('//input[@id="institutionmunip"]/@value')[0]
        data['zip_code'] = root.xpath('//input[@id="institutionzip"]/@value')[0]
        data['state'] = root.xpath('//input[@id="institutionstate"]/@value')[0]
              
        return data

def extract_select_elements(file_path):
    tree = read_html(file_path)
    root = tree.getroot()
    
    city = root.xpath("//select[@name='institutioncity']")[0]
    
    data = city.iterchildren("option")
    first = next(data)
    
    return first.text

def extract_elements(file_path):
    tree = read_html(file_path)
    root = tree.getroot()
    
    data =[]
    data['contact'] = root.xpath('//input[@id="contactfirstname"]')[0]
    data['contact'] = root.path('//input@id=" contactlastname"]')[0]
    data['contact'] = root.path('//input@id=" contacttitle"]')[0]
    data['contact'] = root.path('//input@id=" contactphone"]')[0]
    data['contact'] = root.path('//input@id=" contactemail"]')[0]
    data['contact'] = root.path('//input@id=" contactemailconfirmation"]')[0]
    return data
    
                           

def main():
    institution_addresses = []
    contact_info = []
    cities = []

    for filename in os.scandir(REPORTS):
        if filename.name.endswith(".html"):
            file_path = filename.path
            print("Extracting data:", file_path)

            institution_data = extract_elements_from_html(file_path)
            institution_addresses.append(institution_data)

            contact_data = extract_elements(file_path)
            contact_info.append(contact_data)

            city = extract_select_elements(file_path)
            cities.append(city)

  
    for address in institution_addresses:
        print(address)

    for contact in contact_info:
        print(contact)

    
    for city in cities:
        print(city)

if __name__ == "__main__":
    main()

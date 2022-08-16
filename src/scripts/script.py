import json
import base64
import zlib
import csv
from datetime import datetime
import os.path
from pymkm.pymkmapi import PyMkmApi
from pymkm.pymkm_helper import PyMkmHelper, timeit


# Check if config file is found. If so open it and read it into a var for later use
try:
    with open("config.json", "r") as config_file:
        config = json.load(config_file)

    # Sync missing attributes to active config
    with open("config_template.json", "r") as template_config_file:
        template_config = json.load(template_config_file)
    # template_config.update(self.config)
    PyMkmHelper.update_recursive(config, template_config)
    # self.config = template_config
except FileNotFoundError:
    print(
        "You must copy config_template.json to config.json and populate the fields."
    )
    exit(0)

# Set const variables and names
today = datetime.utcnow().strftime('%Y-%m-%d')
productFilePath = "./product_files/{}-product-file.csv".format(today)


def __read_product_file():
    # If the product file of the corresponding day alredy exists, read that.
    product_list = []

    with open(productFilePath, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if("Magic" in row[3]):
                product_list.append(row)

    return product_list


def __download_product_file():
    # If the file of the day doesnt exist, download it and save it.
    cardmarketAPI = PyMkmApi(config=config)
    product_list = cardmarketAPI.get_product_list()
    csv_products = zlib.decompress(base64.b64decode(product_list["productsfile"]), 16 + zlib.MAX_WBITS).decode('utf-8')
    f = open(productFilePath, "a")
    f.write(csv_products)
    f.close()


if (os.path.isfile(productFilePath) == False):
    __download_product_file()

product_list = __read_product_file()

print(product_list)

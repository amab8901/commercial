# This script imports data from Stripe account and converts it into a convenient form for Python usage

import subprocess
import json

### Create Lists

# load stripe products into settings
output = subprocess.check_output('./stripe_data.sh') # import products from stripe account
output = output.decode('utf-8') # decode from bytes to str
output = output.split("\n")
STRIPE_PRODUCTS_DICT = json.loads(output[0]) # extract products dictionary from string
STRIPE_PRODUCTS_LIST = STRIPE_PRODUCTS_DICT.get('data') # extract relevant list from dictionary
STRIPE_PRICES_DICT = json.loads(output[1]) # extract prices dictionary from string
STRIPE_PRICES_LIST = STRIPE_PRICES_DICT.get('data') # extract relevant list from dictionary
STRIPE_PAYMENT_LINKS_DICT = json.loads(output[2]) # extract payment links dictionary from string
STRIPE_PAYMENT_LINKS_LIST = STRIPE_PAYMENT_LINKS_DICT.get('data') # extract relevant list from dictionary

print()

# Create url list
url_list = []
for i in range(len(STRIPE_PAYMENT_LINKS_LIST)):
    if STRIPE_PAYMENT_LINKS_LIST[i].get('url') is None:
        url_list += [""]
    else:
        url_list += [STRIPE_PAYMENT_LINKS_LIST[i].get('url')]

# Create prices list
prices_list = []
for i in range(len(STRIPE_PRICES_LIST)):
    if STRIPE_PRICES_LIST[i].get('unit_amount') is None:
        prices_list += [""]
    else:
        prices_list += [STRIPE_PRICES_LIST[i].get('unit_amount')]

# Create ID list
ID_list = []
for i in range(len(STRIPE_PRODUCTS_LIST)):
    if STRIPE_PRODUCTS_LIST[i].get('id') is None:
        ID_list += [""]
    else:
        ID_list += [STRIPE_PRODUCTS_LIST[i].get('id')]

# Create description list
description_list = []
for i in range(len(STRIPE_PRODUCTS_LIST)):
    if STRIPE_PRODUCTS_LIST[i].get('description') is None:
        description_list += [""]
    else:
        description_list += [STRIPE_PRODUCTS_LIST[i].get('description')]

# Create images list
images_list = []
for i in range(len(STRIPE_PRODUCTS_LIST)):
    if len(STRIPE_PRODUCTS_LIST[i].get('images')) == 0:
        images_list += [""]
    else:
        images_list += [STRIPE_PRODUCTS_LIST[i].get('images')[0]]

# Create name list
name_list = []
for i in range(len(STRIPE_PRODUCTS_LIST)):
    if len(STRIPE_PRODUCTS_LIST[i].get('name')) == 0:
        name_list += [""]
    else:
        name_list += [STRIPE_PRODUCTS_LIST[i].get('name')]


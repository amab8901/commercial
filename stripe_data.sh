#!/bin/bash

# import products from Stripe account
export STRIPE_PRODUCTS_LIST=$(stripe products list)
export STRIPE_PRICES_LIST=$(stripe prices list)
export STRIPE_PAYMENT_LINKS_LIST=$(stripe payment_links list)

echo $STRIPE_PRODUCTS_LIST
echo $STRIPE_PRICES_LIST
echo $STRIPE_PAYMENT_LINKS_LIST
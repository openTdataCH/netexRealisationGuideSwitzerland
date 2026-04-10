#!/bin/bash

# Validate XML files in the templates folder
python xml-validator.py --xml ../../templates --xsd ../../xsd/xsd/NeTEx_Publication.xsd

# Validate XML files in the examples folder
python xml-validator.py --xml ../../examples --xsd ../../xsd/xsd/NeTEx_Publication.xsd
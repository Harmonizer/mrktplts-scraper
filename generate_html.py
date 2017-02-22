#!/usr/bin/python3.4
from jinja2 import *
from jinja2 import Environment, FileSystemLoader
import yaml

ENV = Environment(loader=FileSystemLoader('./webpage'))

with open('data.yml') as yaml_file:
        items = yaml.load(yaml_file)

#print(items)

template = ENV.get_template("template")

a = template.render(config=items)

print(a)

template.stream(config=items).dump('webpage/index_result.html')

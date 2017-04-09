#!/usr/bin/python3.4
import yaml
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('./webpage'))

with open('data.yml') as yaml_file:
    items = yaml.load(yaml_file)

# print(items)

template = ENV.get_template("template")

a = template.render(config=items)

print(a)

template.stream(config=items).dump('webpage/index_result.html')

#!/usr/bin/env python3.7
import yaml
from jinja2 import Environment, FileSystemLoader

ENV = Environment(loader=FileSystemLoader('./webpage'))
WEBPAGE = 'webpage/index_result.html'

print("Ouput: {}".format(WEBPAGE))

with open('data.yml') as yaml_file:
    items = yaml.load(yaml_file)

template = ENV.get_template("template")

a = template.render(config=items)

template.stream(config=items).dump(WEBPAGE)

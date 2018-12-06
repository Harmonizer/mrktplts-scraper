# mrktplts-scraper

Decided to write a small web scraper that can be used to scrape a popular dutch secondhand-wares marketplace website. Script allows you to check if any individual users (that caught you're attention) have new stuff for sale.

Although the targeted website already allows users to get notified when there are new products added that match certain search criteria. It's unfortunately (up to this moment) not possible to add search definitions containing any user specific information. This makes getting notified when a individual user adds new items somewhat impossible. So that's why I had to make something myself.

For now the scraped results aren't stored in a database but in a serialized YAML file and will be read by the second script to generate the static HTML page based on jinja2 templating

How to use:
```
./run.py
./generate_html.py
```
Point browser to:
```
webpage/index_result.html
```

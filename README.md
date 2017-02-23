# mrktplts-scraper

Decided to write a small web scraper that can be used to scrape a popular dutch secondhand-wares marketplace website. Script allows you to check if any individual users (that caught you're attention) have new stuff for sale.

Although the targeted website already allows users to get notified when there are new products added that match certain search criteria. It's unfortunately (up to this moment) not possible to add search definitions containing any user specific information. This makes getting notified when a individual user adds new items somewhat impossible. So thats why I had to make something myself.

For now the scraped results aren't stored in a database but in a serialized YAML file. The solution to store scraped items is heavily influenced by this. Because now the items are stored in individual dictionaries, separated by a unique named list and then added to yet again a dictionary. By doing so the results that get dumped will automatically receive the spacing required for a properly  formatted yaml list.

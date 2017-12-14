import scrapy

class spider(scrapy.Spider):
    name="dmoz"
    allowed_domains=["dmoztools.net"]
    start_urls=[
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoztool.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        print(response.url.split("/"))
        filename = response.url.split("/")[-2]+".html"

        with open(filename, 'wb') as f:
            f.write(response.body)
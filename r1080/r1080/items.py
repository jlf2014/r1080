from scrapy.item import Item, Field

class R1080Item(Item):

    title = Field()
    createdate = Field()
    ingredients = Field()
    steps = Field()

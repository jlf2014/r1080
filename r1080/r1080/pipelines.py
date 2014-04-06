from scrapy import log
import sqlite3

class R1080Pipeline(object):

    def __init__(self):

        self.connection = sqlite3.connect('./recipes.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            'CREATE TABLE IF NOT EXISTS recipes (' 
                'title VARCHAR(256),'
                'createdate VARCHAR(80),'
                'ingredients TEXT,'
                'steps TEXT)')

    def process_item(self, item, spider):
        self.cursor.execute("select * from recipes where title=?", (item['title'],))
        result = self.cursor.fetchone()
        if result:
            log.msg("Item already in database, deleting: %s" % item, level=log.DEBUG)
            self.cursor.execute("delete from recipes where title=?", (item['title'],))
        else:
            self.cursor.execute(
                "insert into recipes (title,createdate,ingredients,steps) values (?,?,?,?)",
                (
                    item['title'], 
                    item['createdate'],
                    ",".join(item['ingredients']),
                    ",".join(item['steps'])
                ))
            self.connection.commit()

            log.msg("Item stored : " % item, level=log.DEBUG)
        return item

    def handle_error(self, e):
        log.err(e)

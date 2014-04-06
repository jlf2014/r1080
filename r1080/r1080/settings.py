# Scrapy settings for r1080 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'r1080'

SPIDER_MODULES = ['r1080.spiders']
NEWSPIDER_MODULE = 'r1080.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'r1080 (+http://www.yourdomain.com)'

ITEM_PIPELINES = {
    'r1080.pipelines.R1080Pipeline': 300,
}
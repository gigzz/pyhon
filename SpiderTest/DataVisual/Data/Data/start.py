from scrapy import cmdline
cmdline.execute('scrapy crawl PhoneData -o info.csv -t csv'.split())
# ccmdline.execute('scrapy crawl DsjjData -o info.csv -t csv'.split())
# cmdline.execute('scrapy crawl PhoneData'.split())
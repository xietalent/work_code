import scrapy.cmdline


def main():
    scrapy.cmdline.execute(['scrapy', 'crawl', 'huaxia'])

if __name__ == '__main__':
    main()

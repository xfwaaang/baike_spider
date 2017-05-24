import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.paser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, url):
        count = 1
        self.urls.add_new_url(url)
        while self.urls.has_new_url:
            try:
                new_url = self.urls.get_new_url();
                print("craw {0} : {1}".format(count, new_url.encode('utf-8')))
                html_cont = self.downloader.download(new_url)
                # print("html_cont: {}".format(html_cont))
                new_urls, new_data = self.paser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break

                count += 1
            except:
                print("craw failed")


        self.outputer.output_html()



if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)


from bs4 import BeautifulSoup
import re


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser')

        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        # http://baike.baidu.com/item/Python
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/[\w %]+"))

        for link in links:
            new_url = link['href']
            new_full_url = 'http://baike.baidu.com' + new_url
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        if title_node is not None:
            res_data['title'] = title_node.get_text()
        else:
            res_data['title'] = 'failed'

        # <div class="lemma-summary" label-module="lemmaSummary">
        brief_node = soup.find('div', class_ = 'lemma-summary')
        if brief_node is not None:
            res_data['brief'] = brief_node.get_text()
        else:
            res_data['brief'] = 'failed'


        return res_data

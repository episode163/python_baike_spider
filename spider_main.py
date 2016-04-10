import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
	def __init__(self):#初始化下载所需要的url管理器 下载器 解析器 输出器
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url) #获取url
		while self.urls.has_new_url():
			try:
				new_url = self.urls.get_new_url()#当前爬取的url
				print 'craw %d : %s' % (count, new_url) #记录当前爬取的第几个url
				html_cont = self.downloader.download(new_url)#下载好的数据
				new_urls, new_data = self.parser.parse(new_url, html_cont)#new_urls为解析后的新url数据
				self.urls.add_new_urls(new_urls)
				self.outputer.collect_data(new_data)

				if count == 1000:
					break

				count = count+1
			except:
				print 'craw failed'
		self.outputer.collect_html()


if __name__ == '__main__':
	root_url = "http://baike.baidu.com/view/21087.htm" #入口URL
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)#启动爬虫

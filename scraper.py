from requests_html import HTMLSession
from datetime import date
import csv

class RaffleScraper():
    def __init__(self):
        self.result = []
        self.now_date = date.today().strftime("%y.%m.%d")
        self.session = HTMLSession()

    def get_lucky_draw(self,):
        data = []
        url = "https://www.luck-d.com/"
        r = self.session.get(url)
        infos = r.html.find("div.agent_site_info")
        for info in infos:
            n_info = info.text.replace("\n", " ")
            link = "".join(info.absolute_links)
            data.append((n_info, link))
        self.result += data
        return data

    def get_shoe_prize(self):
        data = []
        url = "https://www.shoeprize.com/"
        r = self.session.get(url)
        r.html.render() 
        index = 0
        images = r.html.find("div.img_area")
        infos = r.html.find("div.info_area")
        for info, img in zip(infos, images):
            n_info = info.text.replace("\n", " ")
            link = "".join(img.absolute_links)
            index += 1
            data.append((n_info, link))
        self.result += data
        return data

    def get_mother_bird(self):
        data = []
        url = "https://eomisae.co.kr/dr"
        r = self.session.get(url)
        r.html.render()
        infos = r.html.find("div.card_content")
        for info in infos:
            link = "".join(info.find("h3", first=True).absolute_links)
            title = info.find("h3", first=True).text
            date = info.find("p", first=True).text
            if self.now_date == date:
                data.append((title, link))
        
        self.result += data
        return data

    def get_result(self):
        self.get_mother_bird()
        self.get_lucky_draw()
        self.get_shoe_prize()


        fields = ['text', 'link']
        rows = self.result
        file_name = self.now_date.replace(".", "")
        with open(f"{file_name}.csv", 'w') as f:
            write = csv.writer(f)
            write.writerow(fields)
            write.writerows(rows) 



if __name__ == '__main__':
    scraper = RaffleScraper()
    arr = scraper.get_result()
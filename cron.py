from apscheduler.schedulers.blocking import BlockingScheduler
from scraper import RaffleScraper


scraper = RaffleScraper()

sched = BlockingScheduler(timezone='Asia/Seoul')

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=9)
def scheduled_job():
    scraper.get_result()

sched.start()


from apscheduler.schedulers.background import BackgroundScheduler

from src.app.app import create_app
from src.cron_job.test_cron import test_cron_function

app = create_app()

@app.on_event('startup')
def init_data():
    scheduler = BackgroundScheduler()
    scheduler.add_job(test_cron_function, 'interval', seconds=120)
    scheduler.start()


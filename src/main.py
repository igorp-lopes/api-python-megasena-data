from apscheduler.schedulers.asyncio import AsyncIOScheduler

from src.app.app import create_app
from src.cron_job.test_cron import test_cron_function

app = create_app()

@app.on_event('startup')
def init_data():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(test_cron_function)
    scheduler.start()


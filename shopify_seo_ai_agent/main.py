from agent.seo_agent import SEOAIAgent
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
from datetime import datetime
import os

os.makedirs("logs", exist_ok=True)
log_filename = f"logs/seo_agent_{datetime.now().strftime('%Y%m%d')}.log"
logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

def run_agent_job():
    logging.info("Starting scheduled SEO Agent job...")
    agent = SEOAIAgent()
    agent.run()
    logging.info("SEO Agent job completed.")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(run_agent_job, 'interval', days=1)
    logging.info("Scheduler started. Running daily.")
    scheduler.start()
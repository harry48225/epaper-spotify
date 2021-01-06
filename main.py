from App import App

from apscheduler.schedulers.background import BackgroundScheduler

app = App()

scheduler = BackgroundScheduler(coalesce = True)
scheduler.start() # Should perform our update jobs in the background
scheduler.add_job(app.update, 'interval', seconds=2)

input("Press enter to quit") # Stop the application from shutting down
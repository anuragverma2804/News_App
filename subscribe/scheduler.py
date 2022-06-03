# import logging
# from apscheduler.schedulers.background import BackgroundScheduler
# from django.conf import settings
#
#
# def print2():
#     print("Scheduler Worked")
#
#
# scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


from apscheduler.schedulers.blocking import BlockingScheduler
import datetime


def maintask():
    print("blah")




scheduler = BlockingScheduler()

print("Scheduling Tasks")
start_time = (datetime.datetime.now()).replace(hour=6, minute=0, second=0, microsecond=0)
scheduler.add_job(maintask, 'interval', id="MainTaskid", name="mainTask", start_date=start_time, seconds=5, misfire_grace_time=60)
print("Tasks Scheduled")
print("Running Tasks")
scheduler.start()
print("Good Bye")


# if __name__ == "__main__":
#     main()



#
# def start():
#     if settings.DEBUG:
#         logging.basicConfig()
#         logging.getLogger('apscheduler').setLevel(logging.DEBUG)
#
#     scheduler.add_job(print2, 'interval', minutes=1)
#
#
# start()

from apscheduler.schedulers.blocking import BlockingScheduler
import relay as rl
import time as t
#from datetime import datetime, time

#now = datetime.now()
#now_time = now.time()

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=1800)
def timed_job():
    rl.relay_on_off(2,1)  
    t.sleep(300)
    rl.relay_on_off(2,0)
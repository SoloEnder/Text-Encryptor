import datetime
import os

lvls = ("CRITICAL", "ERROR", "WARNING", "INFO")

def formatte(src, lvl, msg):
    lvl = lvls[lvl - 1]
    actual_date = datetime.datetime.now()
    formated_date = actual_date.strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"{formated_date} [{lvl}] {src} : {msg}\n"
    
    return log_msg
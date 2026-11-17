import sqlite3
import datetime

def log_scraper_run(count, status="Success"):
    with sqlite3.connect("smart_scraper.db") as conn:
        cursor = conn.cursor( ) # IF NOT EXISTS 
        cursor.execute("CREATE TABLE IF NOT EXISTS scraper_logs (time TEXT, count INTEGER, status TEXT)")
        cursor.execute("INSERT INTO scraper_logs VALUES (?, ?, ?)", 
        	(datetime.datetime.now( ).strftime("%Y-%m-%d %H:%M:%S"), count, status))

log_scraper_run(50)

#!/usr/bin/env python
import subprocess
import psycopg2
from contextlib import contextmanager
import threading
import Queue
import db_connector

f = open("payload.txt", "r")
w = open("DATABASE4.txt", "a")
output = f.read()
lines = output.split("\n")[7:-2]
q = Queue.Queue(maxsize=0)

for x in lines:
    q.put(x)
def worker():
    while not q.empty() :
        try:
            line = q.get()
            payload = line[4:].split(' ')[0]
            output = subprocess.check_output(["sudo", "msfvenom", "-p", payload, "-f", "python"]).split('\n')[1:-1]
            code = ""
            for outline in output:
                code +=outline.split(" ")[2]
            code = code.encode("hex")
            db_connector.insert(code)
            q.task_done()
        except Exception as e:
            pass



for num in range(5):
    t = threading.Thread(target=worker)
    t.daemon = True
    t.start()

    
q.join()
f.close()
w.close()


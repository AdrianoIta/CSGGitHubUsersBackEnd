from flask_cors import CORS, cross_origin
import githubuserservice
import schedule
import time
import threading
import schedulertasks
from flask import Flask
from multiprocessing import Process

def parallelize_functions(*functions):
    processes = []
    for function in functions:
        p = Process(target=function)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def task_check_users():
    schedule.every(1).minutes.do(run_threaded, schedulertasks.task_update_users_data) 
    while True:
        schedule.run_pending()
        time.sleep(1)

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route("/get-user/<user_name>")
def get_user(user_name):
    return githubuserservice.get_user_by_name(user_name)

def run_app():
    app.run(debug=False)

if __name__ == '__main__':
    parallelize_functions(task_check_users, run_app)
    


  
    
  


    
   
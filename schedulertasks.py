import databasehelper
import githubuserservice
import itertools

def task_update_users_data():
    print("Task started")
    all_users = list(databasehelper.find_all_user_name())
    for name in itertools.groupby(all_users, lambda x: x["user_name"]):
        githubuserservice.get_user_by_name(name[0])
    print("Task ended")
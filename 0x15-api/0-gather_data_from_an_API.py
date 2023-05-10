#!/usr/bin/python3
"""Returns to do list information for a given employee ID"""
import requests
import sys

if __name__ =="__main":
        url = "https://jsonplaceholder.typicode.com/"
        user_id = int (sys.arg[1]) 
        user_endp = "{}/users/{}".format(url, user_id)
        name =requests.get(user_endp).json().get("name")
        tasks_endp = "{}/todos".format(url
        tasks = requests.get(tasks_endp).json()
        tasks_user = [task for task in tasks if task.get("userid") == user_id]
        completed_task = [dict for dict in tasks_user if dict.get("completed") == True
        
                print("Employee {} is done with tasks({}/{})":
            .format(name, len(tasks_completed), len(tasks_user)))
                for task in completed_task:       
                    print ("\t {}".format(task.get("TITLE")))

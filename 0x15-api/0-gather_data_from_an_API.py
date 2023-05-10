#!/usr/bin/python3
"""Returns to do list information for a given employee ID"""
import requests
import sys

if __name__ =="__main":
        url = "https://jsonplaceholder.typicode.com/"
        user_id = sys.arg[1]
        user_endp = "{}/users/{}".format(url, user_id)
        name =requests.get(user_endp).json().get("name")
        tasks_endp = "{}/todos".format(url
        tasks = requests.get(tasks_endp).json()
        tasks_user = [dict for dict in tasks if dict.get("userid") == user_id]
        tasks_completed = [dict for dict in tasks_user if dict.get("completed") == True
        
                print("Employee {} is done with tasks({}/{})":
            .format(name, len(tasks_completed), len(tasks_user)))

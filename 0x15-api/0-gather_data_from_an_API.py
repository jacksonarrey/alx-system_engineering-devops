#!/usr/bin/python3
"""Returns to do list information for a given employee ID"""
import requests
import sys

if __name__ =="__main":
        url = "https://jsonplaceholder.typicode.com/"
        user = requests.get(url +"users/{}".format(sys.argv[1])).json()
        todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

        completee = [t.get("tittle") for t in todos if t.get ("completed") is TRUE          print (Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)))
        [print"\t {}".format(c)) for c in completed] 

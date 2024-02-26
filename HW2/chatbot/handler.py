import urllib
import random
import requests
from datetime import datetime 

def handle(req):
    author_name = "Chi-Hsien Wu"
    question1 = ["name?\n", "what is your name?\n"]
    question2 = ["what is the current time?\n", "time?\n", "date?\n"]

    query = urllib.unquote(urllib.unquote(req).decode('utf8'))

    if query in question1:
        response1 = author_name + "!"
        response2 = "Hello! My name is " + author_name + "!"
        response3 = "Hey! I am " + author_name + "!"
        
        responses = [response1, response2, response3]
        
        return responses[random.randint(0, 2)]
    
    elif query in question2:
        date_time = datetime.now()
        date, time = datetime.date(date_time), datetime.time(date_time)
        if query == "time?\n":
            return time
        elif query == "date?\n":
            return date
        else:
            return str(date) + " " + str(time)
    
    elif 'figlet' in query:
        response = requests.post("http://10.62.0.4:8080/function/figlet", data=query.split('figlet', 1)[1].strip())
        return response.text

    else:
        return "ERROR!"

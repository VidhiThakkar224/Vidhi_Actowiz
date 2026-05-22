# Performs Request related operationsimport requests
import requests
import threading
from config import *


def make_requests(method, url, contains):
    response = requests.request(
        method=method, 
        url=url, 
        headers=DEFAULT_HEADERS
    )
    if response.status_code == 200:
        if contains in response.text.lower():
            return {
                "status": response.status_code,
                "is_success": True,
                "body": response.content,
                "error": None
            }
        else:
            return {
                "status": response.status_code,
                "is_success": False,
                "body": response.content,
                "error": "CONTAINS_DOES_NOT_MATCH"
            }
    else:
        return {
                "status": response.status_code,
                "is_success": False,
                "body": response.content,
                "error": "SOMETHING_WENT_WRONG"
            }

all_threads = []
def run_threads(thread_count: int, args: tuple):
    for _ in range(thread_count):
        thread = threading.Thread(make_requests, args=args)
        thread.start()
        all_threads.append(thread)
    
    for thread in all_threads:
        thread.join()
        
def save(content, path):
    try:
        with open(path, 'wb') as f:
            f.write(content)
        return {
            "status": 200,
            "error": None
        }
    except Exception as e:
        return {
            "status": 500,
            "error": str(e)
        }
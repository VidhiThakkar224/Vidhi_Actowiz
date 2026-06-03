# import requests
from curl_cffi import requests
import json
from rich import print

class CallRequests:
  def __init__(self, headers=None, path=None):
    self.headers = headers
    self.path = path

  def fetch_requests(self,url=None, method=None, params=None, cookies=None, data=None):
    if url:
      res = requests.request(method=method, url=url,params=params, headers=self.headers, cookies=cookies, data=data, impersonate="chrome120", timeout=20000)
      if res.status_code == 200:
        return {
          "status": res.status_code,
          "is_success": True,
          "body": res.content.decode('utf-8'),
          "error": None,
          "url": res.url
        }
      else:
        return {
          "status": res.status_code,
          "is_success": False,
          "body": "",
          "error": res.reason,
          "url": res.url
        }
    else:
      raise ValueError("url not given.")
  
  def save_data_into_file(self, content, file_name):
    try:
      full_path = self.path + file_name
      if file_name.split(".")[-1] == "json":
        with open(full_path, 'w', encoding="utf-8") as f:
          if type(content) == str:
            content = json.loads(content)
          json.dump(content, f, indent=4)
      else:
        with open(full_path, 'w', encoding="utf-8") as f:
          f.write(content)
      print(f"data saved into \"{full_path}\"")
    except Exception as e:
      print(str(e))



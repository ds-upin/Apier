import requests

class HttpClient:
    def __init__(self,payload):
        #print(payload)
        self.payload=payload
        self.method = payload["http_method"]["method"].strip()
        self.url = payload["url"].strip()
        self.params = payload["params"]
        self.body = payload["body"]
        self.headers = payload["headers"]
        self.cookies = payload["cookies"]
        self.test = payload["test"]
        self.autherization = payload["autherization"]
        #self.prerequest = payload["prerequest"]
        #self.json = payload["json"]
        
    
    def send_request(self):

        self.method = self.method.upper()
        if not self.headers:
            self.headers = {
                "User-Agent": "Apier/1.0",
                "Accept": "application/json, */*"
            }

        try:
            response = requests.request(
                method=self.method,
                url=self.url,
                headers=self.headers,
                params=None if len(self.params)==0 else self.params,
                data=None if len(self.body)==0 else self.body,
                cookies=None if len(self.cookies)==0 else cookies,
                auth=None if len(self.autherization)==0 else (self.autherization["user"],self.autherization["pass"]),
                timeout=20
            )
            return response

        except requests.exceptions.RequestException as e:
            return e 



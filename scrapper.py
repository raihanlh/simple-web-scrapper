import requests
from bs4 import BeautifulSoup

class scrapper:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def listToString(self, lst):  
        # initialize an empty string 
        string = ""  
        
        # traverse in the string   
        for ele in lst:  
            string += ele   
        
        # return string   
        return string 

    def run(self):
        with requests.Session() as s:
            login_url = "LOGIN_URL"

            # Get html of page
            r = s.get(login_url, headers=self.headers)
            soup = BeautifulSoup(r.content, 'html.parser')

            # Get hidden input from html, if needed
            lt = soup.find("input", {"name": "lt"}).get('value')
            execution = soup.find("input", {"name": "execution"}).get('value')
            _eventId = soup.find("input", {"name": "_eventId"}).get('value')

            # Login information, if needed
            username = "YOUR_USERNAME"
            password = "YOUR_PASSWORD"

            data = 'username='+username+'&password='+password+'&lt='+lt+'&execution='+execution+'&_eventId=submit'

            # Login
            r = s.post(url=login_url, data=data, headers=self.headers)

            post_url = "POST_URL" # Can be an URL extension of base URL or be not
            payload = "YOUR_PAYLOAD"

            response = s.post(post_url, data=payload, headers=self.headers)

            # Get user data from html
            user_data = []
            user = []
            
            soup = BeautifulSoup(response.content, "html.parser")
            user_table = soup.find("table", {'id':'tabel'})
            rows = user_table.find_all('tr')
            
            # Parse user data from table
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                user_data.append([ele for ele in cols if ele])
            
            for s in user_data:
                temp = self.listToString(s)
                user.append(temp)
                
            print(user)


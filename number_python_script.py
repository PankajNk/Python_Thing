import requests

url = "https://www.fast2sms.com/dev/bulk"

querystring = {"authorization":"P7vkROgY8CbFZKx9Turn3ol05AIMdXJ1qcySQfBs46wjzLEhW20hNTMtBYZQDlWPGz1agUmv3K4yb28",
               "sender_id":"FSTSMS",
               "language":"english",
               "route":"p",#promotn t for transcatn
               "numbers":"74062042",#number you sign in 
               "message":"YOUR_QT_TEMPLATE_ID",
               "variables":"{AA}|{CC}",
               "variables_values":"12345|asdaswdx"}

headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

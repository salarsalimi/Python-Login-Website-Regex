import requests
import re
import dns
import dns.resolver
import validators

with requests.Session() as s:
    p = s.get('login_url')
    text1 = p.text
    pattern = 'name="token" value="(.*)"'
    match = re.search(pattern, text1)
    token_text = match.group(1)
    payload = {
    'username': 'user',
    'password': 'pass',
    'token': token_text
    }
    A = s.post('post_url', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.

    # An authorised request.
    r = s.get('page_url')
    mytxt = r.text

    pattern2 = 'id=\d{1,4}">(.{1,30})</a>'
    match_dom = re.findall(pattern2, mytxt) 
        # etc...

    
    for i in match_dom:
        if validators.domain(i):
            print (i)
            try:
                result = dns.resolver.resolve(i, 'A')
                for ipval in result:
                    print('IP', ipval.to_text())
            except:
              print("An exception occurred")
            



    


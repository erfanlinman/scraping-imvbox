# -*- coding: utf-8 -*-
"""
Author: Erfan Rahnemoon(linman)
Data: Fri Mar 9 2017
Description: early copy first GET request for site in curl style
then find cookies and user agent part after that copy them here
Without the correct values, the script will not work
"""

__STR_COOKIES = """PHPSESSID=j4u42hbq8e46njat6jn3o18er2; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%228dfa1fcae88f90f0d088dddf96921483%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%2246.165.237.27%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A76%3A%22Mozilla%2F5.0+%28X11%3B+Ubuntu%3B+Linux+x86_64%3B+rv%3A58.0%29+Gecko%2F20100101+Firefox%2F58.0%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1520598095%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D899704ab727cbef92f74bd2119d76432d643485e; country_code=DE"""
__STR_USER_AGENT = """Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36"""

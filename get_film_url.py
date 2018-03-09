# -*- coding: utf-8 -*-
"""
Author: Erfan Rahnemoon(linman)
Data: Fri Mar 9 2017
Description: module now just get link but it's under developing and add features
"""

# TODO: add feature to get movies all data and store in file or db as user
#  request
# FIXME:
# PASSED:
# DEBUG: and TEST: Nothing has yet been tested
# NOTE:
# REVIEW:

import requests
from bs4 import BeautifulSoup
from cookies_and_user_agent import __STR_COOKIES, __STR_USER_AGENT
__STR_BASE_URL = 'https://www.imvbox.com/'


def get_all_movies_link():
    """
        method run get_each_page_link() method for all site's pages
        to store links in list Of course for now
    """
    split_cookie = __STR_COOKIES.split("; ")
    dic_cookies = {}
    for item in split_cookie:
        key_value = item.split("=")
        dic_cookies[key_value[0]] = key_value[1]

    list_all_movies_link = []
    for page_number in range(1, 36):
        list_all_movies_link.extend(
            get_each_page_link(page_number, dic_cookies))
    print list_all_movies_link


def get_each_page_link(page_number, dic_cookies):
    """[summary]
    Arguments:
        page_number {int} -- page number to get all movie's links in that page
        dic_cookies {dictionary} -- cookies to can get data from site
    """
    result = requests.get(url=__STR_BASE_URL+'movies/all/all/' +
                          repr(page_number) + '/all/all/1', cookies=dic_cookies,
                          headers={'User-Agent': __STR_USER_AGENT})
    content = result.content
    soup = BeautifulSoup(content, "html.parser")
    list_of_section = soup.select("div.item.item")
    list_movies_link = []
    for section in list_of_section:
        list_movies_link.append(section.a.get('href'))
    return list_movies_link


if __name__ == '__main__':
    get_all_movies_link()

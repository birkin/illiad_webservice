# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, pprint
import requests


## settings
API_URL = os.environ['ILLIAD_WS_SAMPLE_SCRIPT__API_URL']
API_AUTH_KEY = os.environ['ILLIAD_WS_SAMPLE_SCRIPT__API_AUTH_KEY']
USERNAME = os.environ['ILLIAD_WS_SAMPLE_SCRIPT__TEST_USERNAME']
REQUEST_ID = '1234'  # used to match webservice logging with easyborrow-controller logging


## openurl
"""
example:
- article: 'rft.jtitle=Facial plastic surgery : FPS&rft.atitle=Anatomy for blepharoplasty and brow-lift.&rft.pages=177-85&rft.date=2010&rft.volume=26&rft.end_page=85&ctx_ver=Z39.88-2004&rft.genre=article'
- book: 'sid=FirstSearch%3AWorldCat&genre=book&isbn=9780688002305&title=Zen+and+the+art+of+motorcycle+maintenance%3A+an+inquiry+into+values%2C&date=1974&aulast=Pirsig&aufirst=Robert&auinitm=M&id=doi%3A&pid=673595%3Cfssessid%3E0%3C%2Ffssessid%3E&url_ver=Z39.88-2004&rfr_id=info%3Asid%2Ffirstsearch.oclc.org%3AWorldCat&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook&rft.genre=book&req_dat=%3Csessionid%3E0%3C%2Fsessionid%3E&rfe_dat=%3Caccessionnumber%3E673595%3C%2Faccessionnumber%3E&rft_id=info%3Aoclcnum%2F673595&rft_id=urn%3AISBN%3A9780688002305&rft.aulast=Pirsig&rft.aufirst=Robert&rft.auinitm=M&rft.btitle=Zen+and+the+art+of+motorcycle+maintenance%3A+an+inquiry+into+values%2C&rft.date=1974&rft.isbn=9780688002305&rft.place=New+York&rft.pub=Morrow&rft.genre=book&checksum=8bf1504d891b0a2551ab879c3a555a8c&title=Brown University&linktype=openurl&detail=RBN'
"""
openurl = os.environ['ILLIAD_WS_SAMPLE_SCRIPT__TEST_OPENURL']


## hit api
params = {
    'auth_key': API_AUTH_KEY,
    'openurl': openurl,
    'request_id': REQUEST_ID,
    'username':USERNAME
    }
r = requests.post( API_URL, data=params )


## view response
print r.content

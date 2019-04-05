# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import xml.etree.ElementTree as ET

#put location to xml file here
root = ET.parse('/Users/jonathanschroeder/Documents/Data Research/samples_BSB_http/1115929_http.xml').getroot()

all_events = []
for child in root:
    all_events.append(child.attrib)

#removes duplicate events  
done = set()
unique_events = []
for d in all_events:
    if d['event_code_id'] not in done:
        done.add(d['event_code_id'])  
        unique_events.append(d)

#check
k = [x['event_code_id'] for x in all_events]
len(set(k))

#all unique events and corresponding descriptions
event_descriptions = []
for i in unique_events:
   event_descriptions.append(i['event_code'])


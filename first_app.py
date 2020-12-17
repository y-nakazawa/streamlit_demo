import streamlit as st

import numpy as np
import pandas as pd

st.title('My first app')

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [110, 200, 300, 400]
})

st.text('This is some text.')

st.markdown('```Streamlit is \
_really_ cool```.')

df

x=100

x

import requests
r = requests.get('https://connpass.com/api/v1/event/?series_id=2591')

titles = []
event_date_set = []
participants = []

for e in r.json()["events"]:
  titles.append(e["title"])
  event_date_set.append(e["started_at"])
  participants.append(e["accepted"])

df = pd.DataFrame({
  'タイトル': titles,
  '開催日': event_date_set,
  '参加者数': participants
})

df


# for idx, item in enumerate(r.json()["events"]):

#   row_items = [] 
#   row_items.append(item["title"])
#   row_items.append(item["started_at"])
#   row_items.append(item["accepted"])
  

#   if idx == 0:
#     df = pd.DataFrame(row_items, columns = ['タイトル' , '開催日', '参加者数'])
#     continue

# #   df.loc[idx] = row_items

# # df
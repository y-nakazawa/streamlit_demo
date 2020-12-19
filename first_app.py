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

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'

# aa = [15,30,45]
# option = st.selectbox(
#     'Which number do you like best?',
#      aa)

# 'You selected: ', option


import time



st.title('ギークラボイベント開催一覧')

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

today = datetime.today()
startdate = datetime.strftime(today, '%Y%m')
enddate = "201402"

yyyymm_list = ['全件'] 
yyyymm_list.append(startdate)

while startdate > enddate:
  date = datetime.strptime(startdate, '%Y%m') - relativedelta(months=1)
  startdate = date.strftime("%Y%m")
  yyyymm_list.append(startdate)

yyyymm = st.selectbox(
    'イベント開催年月',
    yyyymm_list
     )

count = st.slider('取得件数', 0, 100, 10)

import requests
r = requests.get(f'https://connpass.com/api/v1/event/?series_id=2591&count={count}&ym={yyyymm}')

titles = []
event_date_set = []
participants = []
owners_name = []

for e in r.json()["events"]:
  titles.append(e["title"])

  dt = datetime.fromisoformat(e["started_at"])
  event_date_set.append(datetime.strftime(dt, '%Y/%m/%d'))
  participants.append(e["accepted"])
  owners_name.append(e["owner_display_name"])

df = pd.DataFrame({
  'タイトル': titles,
  '開催日': event_date_set,
  '参加者数': participants,
  '管理者':  owners_name
})
df.style.set_properties(**{'text-align': 'center'})

df



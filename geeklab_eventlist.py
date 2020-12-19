
import streamlit as st

import pandas as pd
import requests, io
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
from PIL import Image

st.title('ギークラボ開催イベント')

image_url = 'https://connpass-tokyo.s3.amazonaws.com/thumbs/72/9d/729d521ab794e98b4427e9040e8f2fe9.png'
image = Image.open(io.BytesIO(requests.get(image_url).content))
st.image(image, use_column_width=True)

today = datetime.today()
startdate = datetime.strftime(today, '%Y%m')
enddate = "201402"

target_date_set = ['全件'] 
target_date_set.append(startdate)

while startdate > enddate:
  dt = datetime.strptime(startdate, '%Y%m') - relativedelta(months=1)
  startdate = dt.strftime("%Y%m")
  target_date_set.append(startdate)

yyyymm = st.selectbox(
    'イベント開催年月',
    target_date_set
     )

count = st.slider('取得件数', 0, 100, 10)
keyword = st.text_input('キーワード', '')

r = requests.get(f'https://connpass.com/api/v1/event/?series_id=2591&count={count}&ym={yyyymm}&keyword={keyword}')

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



import streamlit as st
# import numpy as np
# import pandas as pd

import time

st.title("Streamlit超入門")

latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done !!!!!!!'

expander = st.expander('といあわせ')
expander.write('表示されるよ')
expander.write('表示されるよ')
expander.write('表示されるよ')
expander.write('表示されるよ')
expander.write('表示されるよ')
expander.write('表示されるよ')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右からむだよ。')
text = st.text_input('あなたの趣味は？')
option = st.selectbox(
    '好きな数字は？',
    list(range(1, 11))
)
condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'あなたの趣味：', text

'あなたの好きな数字は', option, 'です。'
'コンディション：', condition



st.write("DataFrame")

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write(df)

st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)

st.table(df)

"""
# 章
## 節
### 項目

```python
import pandas as pd
import numpy as np
import streamit as st
from PIL import Image
```
"""

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
st.map(df)

############################################################
# PIL ヴァージョンにあうライブラリがない
############################################################

if st.checkbox('Show Moji'):
    st.write('見えてる？')

"""
---
"""


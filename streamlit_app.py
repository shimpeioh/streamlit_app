import io
import random
from datetime import datetime

import pandas as pd
import streamlit as st

# 固体２級用の出題内容

sq1 = [
    {
        "n": 101,
        "q": "1-1 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 102,
        "q": "1-2 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 103,
        "q": "1-3 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 3
    },
    {
        "n": 104,
        "q": "1-4 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 4
    },
    {
        "n": 105,
        "q": "1-5 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 106,
        "q": "1-6 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 107,
        "q": "1-7 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 108,
        "q": "1-8 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 109,
        "q": "1-9 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 110,
        "q": "1-10 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
]

sq2 = [
    {
        "n": 201,
        "q": "2-1 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 202,
        "q": "2-2 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 203,
        "q": "2-3 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 3
    },
    {
        "n": 204,
        "q": "2-4 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 4
    },
    {
        "n": 205,
        "q": "2-5 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 206,
        "q": "2-6 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 207,
        "q": "2-7 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 208,
        "q": "2-8 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 209,
        "q": "2-9 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 210,
        "q": "2-10 を参照してください",
        "s": [1, 2, 3, 4],
        "c": 1
    },
]

# 振動2級用の出題内容

vq1 = [
    {
        "n": 101,
        "q": "1-1",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 102,
        "q": "1-2",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 103,
        "q": "1-3",
        "s": [1, 2, 3, 4],
        "c": 3
    },
    {
        "n": 104,
        "q": "1-4",
        "s": [1, 2, 3, 4],
        "c": 4
    },
    {
        "n": 105,
        "q": "1-5",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 106,
        "q": "1-6",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 107,
        "q": "1-7",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 108,
        "q": "1-8",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 109,
        "q": "1-9",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 110,
        "q": "1-10",
        "s": [1, 2, 3, 4],
        "c": 1
    },
]

vq2 = [
    {
        "n": 201,
        "q": "2-1",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 202,
        "q": "2-2",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 203,
        "q": "2-3",
        "s": [1, 2, 3, 4],
        "c": 3
    },
    {
        "n": 204,
        "q": "2-4",
        "s": [1, 2, 3, 4],
        "c": 4
    },
    {
        "n": 205,
        "q": "2-5",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 206,
        "q": "2-6",
        "s": [1, 2, 3, 4],
        "c": 2
    },
    {
        "n": 207,
        "q": "2-7",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 208,
        "q": "2-8",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 209,
        "q": "2-9",
        "s": [1, 2, 3, 4],
        "c": 1
    },
    {
        "n": 210,
        "q": "2-10",
        "s": [1, 2, 3, 4],
        "c": 1
    },
]

test_class = ["振動2級", "固体2級"]


def question_create(seed: int, qclass: str):

  if seed != 0:

    random.seed(seed)

  q = []

  if qclass == test_class[0]:

    q = q + random.sample(vq1, 7)

    q = q + random.sample(vq2, 5)

  elif qclass == test_class[1]:

    q = q + random.sample(sq1, 7)

    q = q + random.sample(sq2, 5)

  title = []

  for row in q:

    title.append(row["n"])

  title.sort()

  q_sort = []

  for row in title:

    for row_q in q:

      if row == row_q["n"]:

        q_sort.append(row_q)

        break

  return q_sort


def main():

  st.title("アプリ")

  #st.set_option()

  if "qclass" not in st.session_state:

    st.header("ユーザー名を入力してください")

    user = st.text_input(label="username", label_visibility="collapsed")

    st.markdown("")

    st.header("出題分野を選択してください")

    qclass = st.selectbox(label="classselect",
                          label_visibility="collapsed",
                          options=test_class)

    st.markdown("")

    seed = st.number_input(label="出題固定用番号", step=1)

    st.markdown("")

    if st.button(label="確定 / 試験開始"):

      st.session_state.qclass = qclass

      st.session_state.seed = seed

      st.session_state.user = user

      st.rerun()

    st.stop()

  if "pages" not in st.session_state:

    st.session_state.pages = 1

    st.session_state.q = question_create(st.session_state.seed,
                                         st.session_state.qclass)

    st.session_state.answer = {}

  def increase():

    st.session_state.pages += 1

  def decrease():

    st.session_state.pages -= 1

  def select(page: int):

    st.session_state.pages = page

  def finish_test():

    st.session_state.pages = 0

  def rerun():

    st.rerun()

  size = 12

  if st.session_state.pages >= 1:

    with st.sidebar:

      for row in list(range(1, size + 1)):

        st.button(label=f"第{row}問",
                  key=f"{row}",
                  on_click=select,
                  args=(row, ),
                  use_container_width=True)

    q = st.session_state.q

    i = st.session_state.pages - 1

    st.header(f"第{st.session_state.pages}問")

    def index_update():

      if st.session_state.answer.get(st.session_state.pages) != None:

        for s, j in enumerate(q[i]["s"]):

          if j == st.session_state.answer[st.session_state.pages][0]:

            return s

      else:

        return None

    select_index = index_update()

    st.subheader(f"問題 : {q[i]['q']}")

    def radio_answer():

      radio = st.session_state.radio_key

      if radio == q[i]["c"]:

        st.session_state.answer[st.session_state.pages] = [radio, 1]

      else:

        st.session_state.answer[st.session_state.pages] = [radio, 0]

    current_q = st.radio(label=f"問題 : {q[i]['q']}",
                         options=q[i]["s"],
                         index=select_index,
                         horizontal=True,
                         label_visibility="collapsed",
                         key="radio_key",
                         on_change=radio_answer)

    col_1, _, col_2 = st.columns([2, 6, 2])

    with col_1:

      if st.session_state.pages == 1:

        st.button("戻る", disabled=True)

      else:

        st.button("戻る", on_click=decrease)

    with col_2:

      if st.session_state.pages == size:

        st.button("進む", disabled=True)

      else:

        st.button("進む", on_click=increase)

    if size == len(st.session_state.answer):

      st.button("回答", on_click=finish_test)

  elif st.session_state.pages == 0:

    st.header("回答")

    score = 0

    for row in st.session_state.answer:

      score += st.session_state.answer[row][1]

    st.subheader(f"点数 : {str(score)} / {size}")

    # 結果をCSVファイルでダウンロード

    if st.button("結果をCSVファイルでダウンロード"):

      csv_data = generate_csv_data(size)

      cla = st.session_state.qclass

      user = st.session_state.user

      st.download_button(
          label="Download CSV",
          data=csv_data,
          file_name=
          f"results_{cla}_{user}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
          mime="text/csv")

    col_1, col_2, col_3 = st.columns(3)

    with col_1:

      st.subheader("問題")

    with col_2:

      st.subheader("選択")

    with col_3:

      st.subheader("正誤")

    for row in list(range(1, size + 1)):

      with col_1:

        st.markdown(f"第{row}問 {st.session_state.q[row-1]['q']}")

      with col_2:

        st.markdown(st.session_state.answer[row][0])

      with col_3:

        if st.session_state.answer[row][1] == 1:

          st.markdown("*〇*")

        else:

          st.markdown("*✕*")


def generate_csv_data(size):

  # CSVデータを生成

  data = []

  for i in list(range(1, size + 1)):

    data.append({
        "Q_number":
        i,
        "Question":
        st.session_state.q[i - 1]["n"],
        "Answer":
        st.session_state.answer[i][0],
        "Correct":
        st.session_state.q[i - 1]["c"],
        "Correct/Incorrect":
        "Correct" if st.session_state.answer[i][1] == 1 else "Incorrect"
    })

  # DataFrameを作成し、CSVに変換

  df = pd.DataFrame(data)

  csv_buffer = io.StringIO()

  df.to_csv(csv_buffer, index=False)

  return csv_buffer.getvalue()


if __name__ == "__main__":

  main()

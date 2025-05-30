import streamlit as st
import random

# セッション状態に a, b を保存（初回のみ）
if "a" not in st.session_state:
    st.session_state.a = random.randint(1, 10)
if "b" not in st.session_state:
    st.session_state.b = random.randint(1, 10)

a = st.session_state.a
b = st.session_state.b
answer = a + b

st.write("認証のために、以下の計算をしてください。")
user_input = st.number_input(f"{a} + {b} = ?", min_value=0, step=1)

if st.button("認証する"):
    if user_input == answer:
        st.success("認証成功！（人間と判定）")
    else:
        st.error("認証失敗。もう一度試してください。")

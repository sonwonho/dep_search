import streamlit as st
import pandas as pd


df = pd.read_csv('deptCode.csv', encoding = "utf-8")
tab1, tab2 = st.tabs(["관련 법령", "기관 전화번호"])

results = eval(st.query_params.lawList)
deptcode_list = eval(st.query_params.deptCodeList)
phone_df = pd.DataFrame()

with tab1:
    st.title("관련 법령")
    try:
        if results:
            for r in results:
                st.text(r["fullName"])
                st.write(f"{r['lwrdUrl']}")
        else:
            raise Exception()
    except:
        st.text("관련 법률을 찾을 수 없어요")

with tab2:
    st.title("기관 전화번호")
    try:
        for deptcode in deptcode_list:
            phone_df = pd.concat([phone_df, df[df["기관코드"]==str(deptcode)]], ignore_index=True)
        del phone_df['기관코드']
        phone_df = phone_df.reset_index(drop=True)
        st.table(phone_df.head())
    except:
        st.text("관련 기관을 찾을 수 없어요.")
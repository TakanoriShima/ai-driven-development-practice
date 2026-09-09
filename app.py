import streamlit as st

# アプリケーションのタイトルを設定
st.title("AI Training Support")

# アプリケーションの概要説明を表示
st.write("このアプリケーションは、AI研修を支援するためのツールです。")

# サイドバーにナビゲーションの仮メニューを配置
st.sidebar.title("ナビゲーション")
st.sidebar.write("新機能は近日公開予定です！")

# 研修情報入力フォーム
st.header("研修情報入力")

with st.form("training_form"):
    training_title = st.text_input("研修タイトル")
    target_audience = st.text_input("対象者")
    training_theme = st.text_input("研修テーマ")
    training_duration = st.text_input("研修時間")
    notes = st.text_area("備考")

    submitted = st.form_submit_button("入力内容を確認")

# 入力内容を確認
if submitted:
    # 必須項目の入力チェック
    if not training_title.strip() or not training_theme.strip():
        st.error("研修タイトルと研修テーマは必須項目です。")
    else:
        st.subheader("入力内容")

        st.write(f"**研修タイトル:** {training_title}")
        st.write(f"**対象者:** {target_audience}")
        st.write(f"**研修テーマ:** {training_theme}")
        st.write(f"**研修時間:** {training_duration}")
        st.write(f"**備考:** {notes}")
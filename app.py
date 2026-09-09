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

    col1, col2 = st.columns(2)

    with col1:
        confirm_submitted = st.form_submit_button("入力内容を確認")

    with col2:
        summary_submitted = st.form_submit_button("研修概要を生成")

# 入力内容確認ボタン押下時の処理
if confirm_submitted:
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

# 研修概要生成ボタン押下時の処理
if summary_submitted:
    # 必須項目の入力チェック
    if not training_title.strip() or not training_theme.strip():
        st.error("研修タイトルと研修テーマは必須項目です。")
    else:
        # 入力内容をもとに研修概要文を生成
        summary_parts = [
            f"「{training_title}」は、{training_theme}をテーマとした企業向け研修です。"
        ]

        if target_audience.strip():
            summary_parts.append(
                f"主な対象者は{target_audience}です。"
            )

        if training_duration.strip():
            summary_parts.append(
                f"研修時間は{training_duration}を予定しています。"
            )

        if notes.strip():
            summary_parts.append(
                f"備考として「{notes}」が設定されています。"
            )

        summary_parts.append(
            "本研修を通じて、業務に活用できる知識やスキルの習得を目指します。"
        )

        training_summary = "".join(summary_parts)

        st.subheader("生成された研修概要")
        st.write(training_summary)

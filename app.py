import streamlit as st
from google import genai

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

    col1, col2, col3 = st.columns(3)

    with col1:
        confirm_submitted = st.form_submit_button("入力内容を確認")

    with col2:
        summary_submitted = st.form_submit_button("研修概要を生成")

    with col3:
        ai_summary_submitted = st.form_submit_button("AIで研修概要を生成")

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

# ルールベースによる研修概要生成ボタン押下時の処理
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

# 生成AIによる研修概要生成ボタン押下時の処理
if ai_summary_submitted:
    # 必須項目の入力チェック
    if not training_title.strip() or not training_theme.strip():
        st.error("研修タイトルと研修テーマは必須項目です。")
    else:
        # Streamlit SecretsからGemini APIキーを取得
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
        except KeyError:
            api_key = None

        if not api_key:
            st.error(
                "Gemini APIキーが設定されていません。"
                ".streamlit/secrets.toml を確認してください。"
            )
        else:
            # Geminiに渡すプロンプトを作成
            prompt = f"""
あなたは企業研修の企画担当者です。
以下の研修情報をもとに、企業向け研修の案内文として自然な日本語の
研修概要を作成してください。

文章は簡潔で分かりやすく、2〜4文程度にしてください。
入力されていない任意項目については、無理に補完しないでください。

研修タイトル: {training_title}
対象者: {target_audience}
研修テーマ: {training_theme}
研修時間: {training_duration}
備考: {notes}

研修概要本文だけを出力してください。
"""

            try:
                # Gemini APIクライアントを作成
                client = genai.Client(api_key=api_key)

                # Gemini APIを利用して研修概要文を生成
                response = client.models.generate_content(
                    model="gemini-3.7-flash",
                    contents=prompt,
                )

                ai_training_summary = response.text

                if ai_training_summary:
                    st.subheader("AIが生成した研修概要")
                    st.write(ai_training_summary)
                else:
                    st.error(
                        "AIから研修概要文を取得できませんでした。"
                    )

            except Exception:
                st.error(
                    "AIによる研修概要の生成に失敗しました。"
                    "APIキーやネットワーク接続を確認してください。"
                )
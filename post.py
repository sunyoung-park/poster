from openai import OpenAI
import streamlit as st

OPENAI_API_KEY = st.secrets['OPENAI_API_KEY']
client = OpenAI(api_key=OPENAI_API_KEY)

st.title('🎁 제품 홍보 포스터 생성기')

keyword = st.text_input('키워드를 입력하세요.')
if st.button('생성하기🔥') :
    with st.spinner('생성 중입니다.') :
        chat_response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role":"system",
                    "content":"입력받은 키워드에 대한 150자 이내의 솔깃한 제품 홍보 문구를 제작해줘"
                },
                {
                    "role":"user",
                    "content":keyword
                }
            ]
        )

        # ChatGPT 응답 가져오기
        ad_text = chat_response.choices[0].message.content

        # DALL-E로 이미지 생성
        image_response = client.images.generate(
            # model="dall-e-3",
            prompt=keyword,
            size="512x512",  # 지원되는 크기: "256x256", "512x512", "1024x1024"
            n=1
        )

        # 생성된 이미지 URL 가져오기
        image_url = image_response.data[0].url

        # 결과 표시
        st.write(ad_text)
        # st.write(image_url)
        st.image(image_url)

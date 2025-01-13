import openai

# OpenAI API 키 설정
openai.api_key = 'your-api-key'

# 1. 요약문 생성 함수
def generate_summary(news_data):
    prompt = f"Summarize the following news articles into one concise summary:\n{news_data}"

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200
    )

    summary = response.choices[0].text.strip()
    return summary

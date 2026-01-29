# from openai import OpenAI
# from app.core.config import OPENAI_API_KEY

# client = OpenAI(api_key=OPENAI_API_KEY)

def summarize_text(text: str) -> str:
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {
    #             "role": "system",
    #             "content": "You are a helpful assistant that summarizes text."
    #         },
    #         {
    #             "role": "user",
    #             "content": f"Summarize the following text in a concise way:\n{text}"
    #         }
    #     ],
    #     temperature=0.3,
    # )

    # return response.choices[0].message.content
    #-----------------------------------------------------
    # Mock AI logic 
    sentences = text.split(".")
    return sentences[0].strip() + "..."
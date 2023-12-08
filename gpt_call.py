from openai import OpenAI
import keys

client = OpenAI(api_key=keys.get_openai_key())

system_instruction = (
    "You are a helpful coding assistant. You'll be given code written by a beginner developer, "
    "your task is to concisely explain any errors, faults or apparant issues in the code. "
    "Start it with 'Your error is...'"
    "Then provide the corrected code. "
    "Provide one tip for the beginner developer so that they can avoid this mistake in the future. "
    "If the text provided is not code, do not respond. If there are no errors, praise the beginner developer. "
)


def get_improved_code(code):

    user_input = f"Code:\n{code}"

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": user_input}
        ]
    )
    print(response)
    # Return the entire response object
    return response


old_system_instruction = (
    "You are a helpful coding assistant. When given code written by a beginner developer, "
    "your task is to concisely suggest up to three specific improvements that could be made, focusing on "
    "readability, performance, and adherence to best practices. But if the code contains errors, "
    "provide concise corrections instead of improvements. If the text provided is not code, do not respond. "
    "If the code is already well-written, simply confirm that no changes are necessary. "
    "Additionally, provide one concise tip to help the beginner developer improve their coding skills. "
)

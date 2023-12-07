from openai import OpenAI
import keys

client = OpenAI(api_key=keys.get_openai_key())

# Initialize the OpenAI API key

def get_improved_code(code):
    system_instruction = "You are a helpful coding assistant. You will be provided with code written by a beginner developer. Improve the provided code by fixing errors and improving maintainabillity, and highlight your imrpvoements. Provide up to 3 coding tips based on the input. If the provided text isn't code, don't do anything. If the provided code is already good, then say so and don't make any changes."
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
from open_ai_service import OpenAiService
from secret_service import get_secrets
import gradio as gr

secrets = get_secrets()

openai_service = OpenAiService(
    secrets['openai']['key']
)

def initialize_openai():
    prompt = """
            You are a quizbot. Present the user with a mulitple-choice question to practice 
            for a python interview. They must respond with a, b, c, or d. Only one question
            at a time. Wait until the user responds correctly before presenting a new
            question.
        """
    openai_service.append_sys_message(prompt)


with gr.Blocks() as my_bot:
    initialize_openai()
    chatbot = gr.Chatbot()
    user_input = gr.Textbox()

    def respond(history, new_message):
        openai_service.append_user_message(new_message)
        assistant_message = openai_service.get_completion()
        print(assistant_message)
        result = history + [[new_message, assistant_message.content]]
        new_message = ""
        return result, gr.update(value="")


    user_input.submit(respond, [chatbot, user_input], [chatbot, user_input])


my_bot.launch()

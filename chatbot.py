import openai
import gradio

openai.api_key = "YourAPIkey"
prompt="Entrez votre requête"
messages = [{"role": "system", "content": "You are a medical assistant; you will: Guide people when they have symptoms of an illness, or everything that concerns their health (nutrition, dermeto, cosmetics etc etc),If possible, guide them towards a solution or medication without going to a doctor or specialist (for example in the case of a fever, tell the patient to wash with lukewarm water),Indicate the nearest health center or pharmacy,In all cases advise the person to consult a doctor or specialis"}]



def CustomChatGPT(prompt):
    messages.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


def message_and_history(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = CustomChatGPT(inp)
    history.append((input, output))
    return history, history
block = gradio.Blocks(theme=gradio.themes.Monochrome())
with block:
    gradio.Markdown("""<h1><center>Docteur Keneya</center></h1>
    """)
    chatbot = gradio.Chatbot()
    message = gradio.Textbox(placeholder=prompt)
    state = gradio.State()
    submit = gradio.Button("Parlez")
    submit.click(message_and_history, 
                 inputs=[message, state], 
                 outputs=[chatbot, state])
block.launch(auth=('user', 'kabakoo'), auth_message='Regarder le read_me',debug = True,share=True)



"""Hugging Games · interactive web edition for Hugging Face Spaces."""
import gradio as gr
from game import new_game, play

def start():
    state, output = new_game()
    return state, output

def step(message, state):
    if state is None:
        state, _ = new_game()
    result, output = play(state, message or "")
    return result, output, ""

with gr.Blocks(title="Mastermind — Hugging Games") as demo:
    gr.Markdown("# 🎮 Mastermind\n**Hugging Games** · CAN YILDIRIM\n\nDört haneli gizli kodu bul.")
    state = gr.State(None)
    output = gr.Textbox(label="Game screen", lines=12, interactive=False)
    message = gr.Textbox(label="Your move", placeholder="Komut / cevap yaz ve Enter'a bas")
    with gr.Row():
        send = gr.Button("Oyna", variant="primary")
        reset = gr.Button("Yeni oyun")
    send.click(step, inputs=[message,state], outputs=[state,output,message])
    message.submit(step, inputs=[message,state], outputs=[state,output,message])
    reset.click(start, outputs=[state,output])
    demo.load(start,outputs=[state,output])
if __name__ == '__main__':
    demo.launch()

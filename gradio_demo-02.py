import gradio as gr

def combine(a, b):
    return a+" "+b

demo=gr.Interface(
    fn=combine,
    inputs=[gr.Textbox(label="input 1"),
            gr.Textbox(label="input 2")
    ],
    outputs=gr.Textbox(label="Output")
)
demo.launch(server_name="127.0.0.1", server_port=8080)
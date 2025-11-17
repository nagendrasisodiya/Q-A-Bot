import gradio as gr


def add_numbers(a, b):
    return a + b

# Define interface
demo=gr.Interface(
    fn=add_numbers,
    inputs=[gr.Number(), gr.Number()],
    outputs=gr.Number()
)

demo.launch(server_name="127.0.0.1", server_port=8080)
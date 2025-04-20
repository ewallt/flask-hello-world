import gradio as gr
import os

# Define the function for the Gradio interface
# It doesn't need inputs for this simple case
def hello_world():
    return "Hello from Codespaces!"

# Create the Gradio interface
# inputs=None since our function doesn't use any
# outputs="text" to display the string result
demo = gr.Interface(
    fn=hello_world,
    inputs=None,
    outputs="text", # Or "textbox"
    title="Simple Hello World"
)

# Get the port from Render's environment variable
# Default to Gradio's default 7860 if not set (though Render usually sets PORT)
port = int(os.environ.get("PORT", 7860))

# Launch the Gradio app
# server_name="0.0.0.0" is crucial for Render to access the app in the container
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=port)

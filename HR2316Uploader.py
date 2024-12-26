import gradio as gr
import os
import shutil  # For copying files

def save_file(filename, file_path):
    # Define the local folder to save the uploaded file
    save_folder = "uploads"
    os.makedirs(save_folder, exist_ok=True)
    
    # Construct the full path to save the file
    destination_path = os.path.join(save_folder, filename)
    
    # Copy the uploaded file to the destination
    shutil.copy(file_path, destination_path)
    
    return f"File saved as {destination_path}"

# Gradio interface
with gr.Blocks() as interface:
    with gr.Row():
        filename_input = gr.Textbox(label="Enter Filename (with .pdf extension)")
        file_input = gr.File(label="Upload PDF File", type="filepath")
    with gr.Row():
        submit_button = gr.Button("Upload")
    output = gr.Textbox(label="Output")
    
    submit_button.click(save_file, inputs=[filename_input, file_input], outputs=output)

# Launch the interface
interface.launch(server_name="0.0.0.0", server_port=8080)

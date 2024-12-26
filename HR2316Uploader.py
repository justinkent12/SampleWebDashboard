import gradio as gr
import os
import shutil

# Function to save data and file
def save_data(name, number, file_path):
    # Create the uploads folder if it doesn't exist
    save_folder = "uploads"
    current_dir = os.getcwd()
    os.makedirs(save_folder, exist_ok=True)

    # Generate the filename based on name and number
    filename = f"{name}_{number}_12312024.pdf"

    # Construct the destination path and save the file locally
    destination_path = os.path.join(save_folder, filename)
    if os.path.exists(file_path):
        shutil.copy(file_path, destination_path)
    else:
        return f"Error: File {file_path} not found."
    
    print(f"Working directory: {current_dir}")
    print(f"File saved at: {destination_path}")
    
    # Save data to PostgreSQL database
    return f"Data saved successfully! File uploaded as {filename}"

# Gradio interface
with gr.Blocks(title="BIR 2316 Upload") as interface:
    with gr.Row():
        name_input = gr.Textbox(label="Legal Name (Last Name, First Name, Middle Name)(Must be all in CAPITAL LETTER)", placeholder="Enter your Legal Name: ")
        number_input = gr.Textbox(label="TIN ID Number", placeholder="Enter your TIN ID: ")
    file_input = gr.File(label="Upload PDF File", type="filepath")  
    submit_button = gr.Button("Submit")
    output = gr.Textbox(label="Output")
    title="BIR 2316 Uploader"
    
    submit_button.click(
        save_data,
        inputs=[name_input, number_input, file_input],
        outputs=output
    )

# Launch the interface
interface.launch(server_name="0.0.0.0",server_port=8080,show_api=False)

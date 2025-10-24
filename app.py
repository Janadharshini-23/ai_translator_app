import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyperclip

# Main window
root = tk.Tk()
root.title("AI Translator")
root.geometry("600x500")

# Language mapping
languages = {
    'Auto': 'auto',
    'English': 'en',
    'Hindi': 'hi',
    'Tamil': 'ta',
    'French': 'fr',
    'Spanish': 'es',
    'German': 'de',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Chinese': 'zh-CN'
}

# Function to translate text
def translate_text():
    src_lang_name = src_lang_var.get()
    tgt_lang_name = tgt_lang_var.get()
    
    src_lang_code = languages[src_lang_name]
    tgt_lang_code = languages[tgt_lang_name]
    
    text = input_text.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Warning", "Please enter text!")
        return
    
    try:
        translated = GoogleTranslator(source=src_lang_code, target=tgt_lang_code).translate(text)
        output_text.config(state=tk.NORMAL)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
        output_text.config(state=tk.DISABLED)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")

# Function to clear both text boxes
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)

# Function to copy translated text
def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text:
        pyperclip.copy(text)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# Input text
tk.Label(root, text="Enter text:").pack(pady=5)
input_text = tk.Text(root, height=8, width=60)
input_text.pack(pady=5)

# Source language dropdown
src_lang_var = tk.StringVar(value='Auto')
tk.Label(root, text="Source language:").pack(pady=5)
src_dropdown = ttk.Combobox(root, textvariable=src_lang_var, values=list(languages.keys()), state="readonly")
src_dropdown.pack(pady=5)

# Target language dropdown
tgt_lang_var = tk.StringVar(value='English')
tk.Label(root, text="Target language:").pack(pady=5)
tgt_dropdown = ttk.Combobox(root, textvariable=tgt_lang_var, values=list(languages.keys()), state="readonly")
tgt_dropdown.pack(pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

translate_btn = tk.Button(button_frame, text="Translate", command=translate_text)
translate_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_text)
clear_btn.grid(row=0, column=1, padx=10)

copy_btn = tk.Button(button_frame, text="Copy", command=copy_text)
copy_btn.grid(row=0, column=2, padx=10)

# Output text
tk.Label(root, text="Translated text:").pack(pady=5)
output_text = tk.Text(root, height=8, width=60, state=tk.DISABLED)
output_text.pack(pady=5)

root.mainloop()







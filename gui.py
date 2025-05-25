import tkinter as tk
from tkinter import messagebox
from mail_logic import *

def create_gui():
    window = tk.Tk()
    window.title("Temporary Mail App")
    window.geometry("600x500")
    window.resizable(False, False)
    window.configure(bg='#f5f5f5')
    
    bg_color = "#f5f5f5"
    primary_color = "#4a6fa5"
    secondary_color = "#166088"
    text_color = "#333333"


    title_font = ('Helvetica', 12, 'bold')
    normal_font = ('Helvetica', 10)
    log_font = ('Consolas', 9)
    
    main_frame = tk.Frame(window, bg=bg_color, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    

    domain_frame = tk.LabelFrame(main_frame, text=" Domain Information ", 
                                bg=bg_color, fg=secondary_color, 
                                font=title_font, padx=10, pady=10)
    domain_frame.pack(fill=tk.X, pady=5)
    
    tk.Label(domain_frame, 
            text=f"Server Domain: {get_domain()}",
            font=normal_font,
            fg=text_color,
            bg=bg_color).pack()
    

    control_frame = tk.LabelFrame(main_frame, text=" Email Controls ", 
                                bg=bg_color, fg=secondary_color, 
                                font=title_font, padx=10, pady=10)
    control_frame.pack(fill=tk.X, pady=10)
    

    generate_btn = tk.Button(control_frame, 
                            text="🔄 Generate New Email",
                            font=normal_font,
                            bg=primary_color,
                            fg='white',
                            activebackground=secondary_color,
                            command=lambda: generate_email_action())
    generate_btn.pack(side=tk.LEFT, padx=5)
    

    listen_btn = tk.Button(control_frame,
                            text="👂 Start Listening",
                            font=normal_font,
                            bg=primary_color,
                            fg='white',
                            activebackground=secondary_color,
                            command=lambda: start_listener_action())
    listen_btn.pack(side=tk.LEFT, padx=5)
    

    email_frame = tk.LabelFrame(main_frame, text=" Current Email ", 
                                bg=bg_color, fg=secondary_color, 
                                font=title_font, padx=10, pady=10)
    email_frame.pack(fill=tk.X, pady=5)
    
    email_label = tk.Label(email_frame,
                            text="No email generated yet",
                            font=normal_font,
                            fg=text_color,
                            bg=bg_color)
    email_label.pack()
    

    log_frame = tk.LabelFrame(main_frame, text=" Activity Log ", 
                            bg=bg_color, fg=secondary_color, 
                            font=title_font, padx=10, pady=10)
    log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
    

    log_inner_frame = tk.Frame(log_frame, bg='white')
    log_inner_frame.pack(fill=tk.BOTH, expand=True)
    
    log_text = tk.Text(log_inner_frame,
                        height=12,
                        bg="white",
                        fg=text_color,
                        font=log_font,
                        padx=10,
                        pady=10,
                    wrap=tk.WORD)
    
    scrollbar = tk.Scrollbar(log_inner_frame, orient=tk.VERTICAL, command=log_text.yview)
    log_text.configure(yscrollcommand=scrollbar.set)
    
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    log_text.pack(fill=tk.BOTH, expand=True)
    

    current_email = None
    

    def log_action(message, type='info'):
        if type == 'success':
            log_text.insert(tk.END, message + "\n", 'success')
        elif type == 'error':
            log_text.insert(tk.END, message + "\n", 'error')
        else:
            log_text.insert(tk.END, message + "\n")
        log_text.see(tk.END)
    
    
    log_text.tag_configure('success', foreground='#2e7d32')
    log_text.tag_configure('error', foreground='#c62828')
    
    def generate_email_action():
        nonlocal current_email
        try:
            current_email = generate_new_email()
            email_label.config(text=current_email)
            log_action(f"✓ Success: New email generated - {current_email}", 'success')
        except Exception as e:
            log_action(f"✗ Error: Failed to generate email - {str(e)}", 'error')
    
    def start_listener_action():
        nonlocal current_email
        if not current_email:
            messagebox.showwarning("Warning", "Please generate an email first!")
            log_action("✗ Error: No email address available for listening", 'error')
        else:
            try:
                start_listening(email_received_handler)
                log_action("✓ Started listening for incoming emails...", 'success')
            except Exception as e:
                log_action(f"✗ Error: Failed to start listening - {str(e)}", 'error')
    
    def email_received_handler(message):
        window.after(0, lambda: display_email(message))
    
    def display_email(message):
        log_action("\n════════ New Email ════════")
        log_action(f"From: {message['from']}")
        log_action(f"Subject: {message['subject']}")
        log_action(f"Content: {message['text'][:200]}...")
        log_action("══════════════════════════")
    
    return window
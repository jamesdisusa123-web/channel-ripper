import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import threading
import subprocess
import os
from pathlib import Path

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class FuturisticChannelRipper:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("🌌 CHANNELRIPPER 2.0")
        self.root.geometry("900x700")
        self.root.configure(fg_color="#0a0a0f")
        
        self.downloads = []  # IDM-style download list
        self.process = None
        
        self.setup_futuristic_ui()
    
    def setup_futuristic_ui(self):
        # Header
        header = ctk.CTkFrame(self.root, fg_color="transparent")
        header.pack(fill="x", padx=20, pady=(20,10))
        
        title = ctk.CTkLabel(header, text="🌌 CHANNELRIPPER 2.0", 
                           font=ctk.CTkFont("Arial", 28, "bold"),
                           text_color="#00d4ff")
        title.pack()
        
        # URL Input (Glassmorphism)
        url_frame = ctk.CTkFrame(self.root, fg_color="#1a1a2e", 
                               border_width=2, border_color="#00d4ff")
        url_frame.pack(fill="x", padx=20, pady=10)
        
        ctk.CTkLabel(url_frame, text="🔗 TARGET URL", font=ctk.CTkFont("Arial", 14),
                    text_color="#a0a0ff").pack(pady=(15,5))
        
        self.url_entry = ctk.CTkEntry(url_frame, height=45, font=ctk.CTkFont("Arial", 14),
                                    placeholder_text="https://youtube.com/@channelname")
        self.url_entry.pack(fill="x", padx=20, pady=(0,15))
        
        # Output + Options
        options_frame = ctk.CTkFrame(self.root, fg_color="#1a1a2e")
        options_frame.pack(fill="x", padx=20, pady=10)
        
        # Output path
        ctk.CTkLabel(options_frame, text="📂 OUTPUT VAULT", 
                    font=ctk.CTkFont("Arial", 14), text_color="#a0a0ff").grid(row=0, column=0, padx=20, pady=15, sticky="w")
        self.output_path = ctk.CTkLabel(options_frame, text="./CyberVault", 
                                      text_color="#ffffff", font=ctk.CTkFont("Arial", 12))
        self.output_path.grid(row=0, column=1, padx=10, pady=15, sticky="w")
        
        # Quality selector
        quality_frame = ctk.CTkFrame(options_frame, fg_color="transparent")
        quality_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        ctk.CTkLabel(quality_frame, text="⚙️ RESOLUTION", text_color="#a0a0ff").pack(side="left")
        self.quality_var = ctk.CTkComboBox(quality_frame, values=["720p", "1080p", "Best"], width=120)
        self.quality_var.set("1080p")
        self.quality_var.pack(side="left", padx=20)
        
        # RIP BUTTON (Hero)
        self.rip_btn = ctk.CTkButton(self.root, text="🔥 RIP THE MATRIX", 
                                   height=60, font=ctk.CTkFont("Arial", 20, "bold"),
                                   fg_color=("#ff0080", "#ff4444"), hover_color="#ff6666",
                                   command=self.start_rip)
        self.rip_btn.pack(pady=30)
        
        # Progress Bar (Holographic)
        self.progress_frame = ctk.CTkFrame(self.root, fg_color="#1a1a2e", height=60)
        self.progress_frame.pack(fill="x", padx=20, pady=10)
        self.progress_frame.pack_propagate(False)
        
        self.overall_progress = ctk.CTkProgressBar(self.progress_frame, height=30, 
                                                 progress_color="#00ff88")
        self.overall_progress.pack(fill="x", padx=20, pady=10)
        self.overall_progress.set(0)
        
        self.progress_label = ctk.CTkLabel(self.progress_frame, text="0% | 0/0 | ETA: --:--",
                                         font=ctk.CTkFont("Arial", 14, "bold"))
        self.progress_label.pack()
        
        # IDM-style Download List
        list_frame = ctk.CTkScrollableFrame(self.root, fg_color="#1a1a2e")
        list_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        ctk.CTkLabel(list_frame, text="📱 ACTIVE DOWNLOADS", 
                    font=ctk.CTkFont("Arial", 16, "bold"), text_color="#00d4ff").pack(pady=10)
        
        self.download_listbox = tk.Listbox(list_frame, bg="#0f0f1a", fg="#00ff88",
                                        font=("Consolas", 11), selectbackground="#ff4444",
                                        height=12, relief="flat", bd=0)
        self.download_listbox.pack(fill="both", expand=True, padx=10, pady=(0,20))
    
    def start_rip(self):
        url = self.url_entry.get()
        if not url:
            return
        
        self.rip_btn.configure(state="disabled", text="🔥 BREACHING...")
        threading.Thread(target=self.rip_thread, daemon=True).start()
    
    def rip_thread(self):
        try:
            cmd = [
                "yt-dlp",
                "--yes-playlist", "--flat-playlist",
                f"--output '{self.output_path.cget('text')}/%(uploader)s/%(title)s.%(ext)s'",
                "--print", "%(id)s|%(title)s|%(duration)s",
                self.url_entry.get()
            ]
            
            self.process = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                                          text=True, bufsize=1, universal_newlines=True)
            
            self.root.after(0, lambda: self.update_download_list())
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
        finally:
            self.root.after(0, self.cleanup)
    
    def update_download_list(self):
        if self.process.poll() is None:
            line = self.process.stdout.readline()
            if line:
                self.download_listbox.insert(tk.END, f"› {line.strip()}")
                self.download_listbox.see(tk.END)
            self.root.after(100, self.update_download_list)
    
    def cleanup(self):
        self.rip_btn.configure(state="normal", text="🔥 RIP THE MATRIX")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FuturisticChannelRipper()
    app.run()

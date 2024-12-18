import tkinter as tk
from tkinter import ttk, filedialog
import os
import random
import time

class EmuAIHUD:
    def __init__(self, root):
        self.root = root
        self.root.title("EmuAI - MIPS Emulator HUD")
        self.root.geometry("800x600")
        
        self.emulation_running = False
        self.loaded_rom = None
        
        self.setup_hud()

    def setup_hud(self):
        # Status Bar
        self.status_var = tk.StringVar(value="Status: Idle")
        ttk.Label(self.root, textvariable=self.status_var, font=("Arial", 14)).pack(side=tk.TOP, anchor=tk.W, pady=5)
        
        # ROM Information
        self.rom_info = tk.StringVar(value="ROM: No ROM loaded")
        ttk.Label(self.root, textvariable=self.rom_info, font=("Arial", 12)).pack(side=tk.TOP, anchor=tk.W, pady=5)
        
        # Performance Metrics
        self.fps_var = tk.StringVar(value="FPS: 0")
        self.memory_var = tk.StringVar(value="Memory: 0 MB / 4 MB")
        ttk.Label(self.root, textvariable=self.fps_var, font=("Arial", 12)).pack(side=tk.TOP, anchor=tk.W, pady=5)
        ttk.Label(self.root, textvariable=self.memory_var, font=("Arial", 12)).pack(side=tk.TOP, anchor=tk.W, pady=5)
        
        # Buttons
        ttk.Button(self.root, text="Load ROM", command=self.load_rom).pack(side=tk.TOP, pady=10)
        self.start_stop_button = ttk.Button(self.root, text="Start Emulation", command=self.toggle_emulation)
        self.start_stop_button.pack(side=tk.TOP, pady=10)
        
        # Console Output
        self.console = tk.Text(self.root, height=20, width=80)
        self.console.pack(side=tk.BOTTOM, pady=10)
        self.console.config(state=tk.DISABLED)
        
    def update_status(self, status):
        self.status_var.set(f"Status: {status}")

    def update_rom_info(self, rom_name):
        self.rom_info.set(f"ROM: {rom_name}")
        
    def update_performance(self, fps, memory_usage):
        self.fps_var.set(f"FPS: {fps}")
        self.memory_var.set(f"Memory: {memory_usage:.2f} MB / 4 MB")
        
    def log_message(self, message):
        self.console.config(state=tk.NORMAL)
        self.console.insert(tk.END, f"{message}\n")
        self.console.see(tk.END)
        self.console.config(state=tk.DISABLED)
        
    def load_rom(self):
        filetypes = [("N64 ROMs", "*.z64")]
        filename = filedialog.askopenfilename(filetypes=filetypes)
        if filename:
            self.loaded_rom = os.path.basename(filename)
            self.update_rom_info(self.loaded_rom)
            self.log_message(f"Loaded ROM: {self.loaded_rom}")
            self.update_status("ROM Loaded")
        else:
            self.log_message("No ROM selected")
            
    def toggle_emulation(self):
        if not self.loaded_rom:
            self.log_message("Please load a ROM first")
            return
        
        self.emulation_running = not self.emulation_running
        if self.emulation_running:
            self.update_status("Running")
            self.start_stop_button.config(text="Stop Emulation")
            self.log_message(f"Starting emulation of {self.loaded_rom} using SixtyForcePlus engine")
            self.root.after(100, self.simulate_emulation)
        else:
            self.update_status("Stopped")
            self.start_stop_button.config(text="Start Emulation")
            self.log_message("Emulation stopped")
            
    def simulate_emulation(self):
        if self.emulation_running:
            fps = random.randint(55, 60)
            memory_usage = random.uniform(2.0, 3.5)
            self.update_performance(fps, memory_usage)
            self.root.after(1000, self.simulate_emulation)
        
if __name__ == "__main__":
    root = tk.Tk()
    hud = EmuAIHUD(root)
    root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pathlib import Path
import os
import sys
import time
from main import read_specifications, generate_in_file

class DesStructApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DesStruct IN File Generator")
        self.root.geometry("400x200")  # Increased height for progress bar
        
        # Set output directory based on whether we're running as executable or script
        if getattr(sys, 'frozen', False):
            # Running as executable
            self.output_dir = (Path(sys.executable).parent.parent / "output").resolve()
        else:
            # Running as script
            self.output_dir = (Path(__file__).parent.parent / "output").resolve()
            
        self.output_dir.mkdir(exist_ok=True)
        
        # Create main frame
        main_frame = tk.Frame(root, padx=20, pady=20)
        main_frame.grid(row=0, column=0, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)
        
        # File selection frame
        file_frame = tk.Frame(main_frame)
        file_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        
        self.file_label = tk.Label(
            file_frame,
            text="No file selected",
            fg='#7f8c8d'
        )
        self.file_label.grid(row=0, column=0, sticky="w")
        
        self.select_button = tk.Button(
            file_frame,
            text="Select CSV File",
            command=self.select_file,
            bg='#3498db',
            fg='white',
            padx=10
        )
        self.select_button.grid(row=0, column=1, padx=5)
        
        # Progress bar frame
        self.progress_frame = tk.Frame(main_frame)
        self.progress_frame.grid(row=1, column=0, sticky="ew", pady=(0, 10))
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            orient="horizontal",
            length=300,
            mode="determinate"
        )
        self.progress_bar.grid(row=0, column=0, sticky="ew")
        
        self.progress_label = tk.Label(
            self.progress_frame,
            text="",
            fg='#7f8c8d'
        )
        self.progress_label.grid(row=1, column=0, sticky="w")
        
        # Status label
        self.status_label = tk.Label(
            main_frame,
            text="Please select a CSV file to begin",
            fg='#7f8c8d'
        )
        self.status_label.grid(row=2, column=0, sticky="w")
        
        self.selected_file = None
        
    def select_file(self):
        """Handle file selection and automatically generate IN file"""
        file_path = filedialog.askopenfilename(
            title="Select CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            self.selected_file = file_path
            self.file_label.config(
                text=Path(file_path).name,
                fg='#2c3e50'
            )
            self.status_label.config(
                text="Processing file...",
                fg='#2c3e50'
            )
            self.show_progress()
    
    def show_progress(self):
        """Show progress bar animation for 3 seconds"""
        self.progress_frame.grid()  # Show progress frame
        self.progress_bar["value"] = 0
        self.progress_label.config(text="Generating IN file...")
        
        def update_progress():
            current = self.progress_bar["value"]
            if current < 100:
                self.progress_bar["value"] = current + 2
                self.root.after(60, update_progress)  # Update every 60ms
            else:
                self.progress_frame.grid_remove()  # Hide progress frame
                self.generate_in_file()
        
        self.root.after(60, update_progress)  # Start progress animation
    
    def generate_in_file(self):
        """Generate IN file from selected CSV"""
        if not self.selected_file:
            return
        
        try:
            # Read specifications from selected CSV
            data_dict = read_specifications(self.selected_file)
            
            # Generate IN file content
            in_content = generate_in_file(data_dict)
            
            # Generate output filename based on input filename
            input_filename = Path(self.selected_file).stem
            output_filename = f"{input_filename}_DESCTRL.IN"
            output_path = self.output_dir / output_filename
            
            # Write the generated content
            with open(output_path, 'w') as f:
                f.write(in_content)
            
            # Show success message
            messagebox.showinfo(
                "Success",
                f"IN file generated successfully!\nSaved to: {output_path}"
            )
            
            # Automatically open the generated file
            os.startfile(str(output_path))
            
            # Reset status
            self.status_label.config(
                text="Please select a CSV file to begin",
                fg='#7f8c8d'
            )
            self.file_label.config(
                text="No file selected",
                fg='#7f8c8d'
            )
            self.selected_file = None
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"An error occurred:\n{str(e)}"
            )

def main():
    root = tk.Tk()
    app = DesStructApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 
import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Hızlı Yazma Testi")
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        
        # Örnek metinler
        self.sample_texts = [
            "Bilgisayar teknolojisi hayatımızın vazgeçilmez bir parçası haline geldi.",
            "İnternet sayesinde dünyanın her yerindeki bilgiye anında ulaşabiliyoruz.",
            "Yapay zeka teknolojileri her geçen gün daha da gelişiyor ve hayatımızı kolaylaştırıyor.",
            "Programlama öğrenmek günümüzde çok önemli bir yetenek haline geldi.",
            "Teknoloji ile birlikte iletişim şeklimiz de sürekli değişiyor ve gelişiyor."
        ]
        
        self.current_text = ""
        self.start_time = None
        self.test_started = False
        
        self.create_widgets()
        self.reset_test()
        
    def create_widgets(self):
        # Başlık
        self.title_label = tk.Label(self.root, text="Hızlı Yazma Testi", 
                                  font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)
        
        # Örnek metin gösterimi
        self.text_display = tk.Label(self.root, text="", wraplength=700,
                                   font=("Arial", 14))
        self.text_display.pack(pady=20, padx=50)
        
        # Yazı giriş alanı
        self.text_input = tk.Text(self.root, height=5, font=("Arial", 12))
        self.text_input.pack(pady=20, padx=50)
        self.text_input.bind("<KeyPress>", self.on_key_press)
        
        # Sonuçlar
        self.result_frame = tk.Frame(self.root)
        self.result_frame.pack(pady=20)
        
        # WPM göstergesi
        self.wpm_label = tk.Label(self.result_frame, text="WPM: 0",
                                font=("Arial", 12, "bold"))
        self.wpm_label.pack(side=tk.LEFT, padx=20)
        
        # Doğruluk göstergesi
        self.accuracy_label = tk.Label(self.result_frame, text="Doğruluk: 0%",
                                     font=("Arial", 12, "bold"))
        self.accuracy_label.pack(side=tk.LEFT, padx=20)
        
        # Yeniden başlat butonu
        self.restart_button = tk.Button(self.root, text="Yeniden Başlat",
                                      command=self.reset_test,
                                      font=("Arial", 12))
        self.restart_button.pack(pady=20)
        
    def reset_test(self):
        self.current_text = random.choice(self.sample_texts)
        self.text_display.config(text=self.current_text)
        self.text_input.delete(1.0, tk.END)
        self.text_input.config(state=tk.NORMAL)
        self.start_time = None
        self.test_started = False
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Doğruluk: 0%")
        
    def calculate_wpm(self, time_taken, typed_text):
        words = len(typed_text.split())
        minutes = time_taken / 60
        wpm = round(words / minutes)
        return wpm
        
    def calculate_accuracy(self, original_text, typed_text):
        if len(typed_text) == 0:
            return 0
            
        correct_chars = sum(1 for a, b in zip(original_text, typed_text) if a == b)
        accuracy = (correct_chars / len(original_text)) * 100
        return round(accuracy, 1)
        
    def on_key_press(self, event):
        if not self.test_started:
            self.start_time = time.time()
            self.test_started = True
            
        # Enter tuşuna basıldığında testi bitir
        if event.keysym == "Return":
            if self.start_time:
                self.end_test()
                
    def end_test(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        
        typed_text = self.text_input.get(1.0, tk.END).strip()
        
        wpm = self.calculate_wpm(time_taken, typed_text)
        accuracy = self.calculate_accuracy(self.current_text, typed_text)
        
        self.wpm_label.config(text=f"WPM: {wpm}")
        self.accuracy_label.config(text=f"Doğruluk: {accuracy}%")
        
        self.text_input.config(state=tk.DISABLED)
        
        if accuracy >= 90:
            messagebox.showinfo("Tebrikler!", f"Harika bir sonuç!\nWPM: {wpm}\nDoğruluk: {accuracy}%")
        
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()

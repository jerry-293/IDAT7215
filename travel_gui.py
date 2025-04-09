# travel_gui.py (改進版)
import tkinter as tk
from tkinter import messagebox, ttk
import dest
import recommend
import os
from PIL import Image, ImageTk  # 用於處理圖片
import pygame  # 用於播放音效
import json

class TravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Japan Travel Expert System")
        self.root.geometry("600x700")
        
        self.answers = []
        self.current_question = 0
        self.language = "en"  # 預設英文
        self.started = False
        
        # 圖片資料夾路徑
        self.photo_dir = os.path.join(os.path.dirname(__file__), "photo")
        
        # 初始化聲音
        pygame.mixer.init()
        self.click_sound = pygame.mixer.Sound("click.wav")  # 確保有一個 click.wav 文件
        
        # 語言字典，集中管理所有文字
        self.texts = {
            "en": {
                "welcome": "Welcome to the Japan Travel Expert System!",
                "language": "Language:",
                "theme": "Theme:",
                "start": "Start",
                "previous": "Previous",
                "next": "Next",
                "restart": "Restart",
                "warning": "Warning",
                "select_option": "Please select an option!",
                "incomplete": "Incomplete Answers",
                "incomplete_msg": "Please answer all questions before proceeding!",
                "recommendation": "Recommendation",
                "based_on": "Based on your preferences, we recommend:",
                "no_recommendation": "No specific recommendation based on your preferences.",
                "introduction": "Introduction:",
                "attractions": "Attractions:",
                "recommended_days": "Recommended Days:",
                "transportation": "Transportation:",
                "estimated_cost": "Estimated Daily Cost:"
            },
            "cn": {
                "welcome": "歡迎使用日本旅行專家系統！",
                "language": "語言：",
                "theme": "主題：",
                "start": "開始",
                "previous": "上一題",
                "next": "下一題",
                "restart": "重新開始",
                "warning": "警告",
                "select_option": "請選擇一個選項！",
                "incomplete": "未完成回答",
                "incomplete_msg": "請回答所有問題！",
                "recommendation": "推薦結果",
                "based_on": "根據你的偏好，我們推薦：",
                "no_recommendation": "根據你的偏好，沒有特定的推薦。",
                "introduction": "介紹：",
                "attractions": "景點：",
                "recommended_days": "建議停留天數：",
                "transportation": "交通建議：",
                "estimated_cost": "每日預估費用："
            }
        }
        
        self.themes = {
            "Sakura": {"bg": "#ffe4e1", "fg": "#c71585", "btn_bg": "#ff1493", "btn_hover": "#ff42a1"},
            "Wafu": {"bg": "#e0f7e9", "fg": "#2f4f4f", "btn_bg": "#3cb371", "btn_hover": "#66cdaa"},
            "Modern": {"bg": "#f5f5f5", "fg": "#333333", "btn_bg": "#4682b4", "btn_hover": "#6495ed"}
        }
        self.current_theme = "Sakura"
        self.root.configure(bg=self.themes["Sakura"]["bg"])
        
        # 快捷鍵綁定
        self.root.bind("<Return>", lambda event: self.next_question())
        self.root.bind("<BackSpace>", lambda event: self.prev_question())
        
        self.control_frame = tk.Frame(root, bg="#ffffff")
        self.control_frame.pack(pady=5)
        
        tk.Label(self.control_frame, text=self.texts[self.language]["language"], bg="#ffffff", font=("MS Gothic", 12)).pack(side=tk.LEFT)
        self.lang_var = tk.StringVar(value="English")
        tk.OptionMenu(self.control_frame, self.lang_var, "English", "中文", command=self.change_language).pack(side=tk.LEFT, padx=5)
        
        tk.Label(self.control_frame, text=self.texts[self.language]["theme"], bg="#ffffff", font=("MS Gothic", 12)).pack(side=tk.LEFT)
        self.theme_var = tk.StringVar(value="Sakura")
        tk.OptionMenu(self.control_frame, self.theme_var, *self.themes.keys(), command=self.change_theme).pack(side=tk.LEFT)
        
        self.top_frame = tk.Frame(root, bg="#ffffff")
        self.top_frame.pack(pady=20)
        self.label = tk.Label(self.top_frame, text=self.texts[self.language]["welcome"], 
                            font=("MS Gothic", 18, "bold"), bg="#ffffff", fg=self.themes["Sakura"]["fg"])
        self.label.pack()
        
        self.start_frame = tk.Frame(root, bg="#ffffff")
        self.start_frame.pack(pady=30)
        self.start_btn = tk.Button(self.start_frame, text=self.texts[self.language]["start"], command=self.start_questions, 
                                 font=("Helvetica", 12), bg=self.themes["Sakura"]["btn_bg"], fg="white", width=10)
        self.start_btn.pack()
        self.start_btn.bind("<Enter>", lambda e: self.start_btn.config(bg=self.themes[self.current_theme]["btn_hover"]))
        self.start_btn.bind("<Leave>", lambda e: self.start_btn.config(bg=self.themes[self.current_theme]["btn_bg"]))
        
        self.middle_frame = tk.Frame(root, bg="#ffffff", bd=2, relief="groove")
        self.progress = ttk.Progressbar(self.middle_frame, length=400, maximum=len(dest.questions))
        self.question_label = tk.Label(self.middle_frame, text="", font=("MS Gothic", 18, "bold"), 
                                     bg="#ffffff", fg=self.themes["Sakura"]["fg"], wraplength=450)
        self.option_var = tk.StringVar()
        self.options_frame = tk.Frame(self.middle_frame, bg="#ffffff")
        
        self.bottom_frame = tk.Frame(root, bg="#ffffff")
        self.prev_btn = tk.Button(self.bottom_frame, text=self.texts[self.language]["previous"], command=self.prev_question, 
                                font=("Helvetica", 12), bg=self.themes["Sakura"]["btn_bg"], fg="white", width=10)
        self.next_btn = tk.Button(self.bottom_frame, text=self.texts[self.language]["next"], command=self.next_question, 
                                font=("Helvetica", 12), bg=self.themes["Sakura"]["btn_bg"], fg="white", width=10)
        
        self.prev_btn.bind("<Enter>", lambda e: self.prev_btn.config(bg=self.themes[self.current_theme]["btn_hover"]))
        self.prev_btn.bind("<Leave>", lambda e: self.prev_btn.config(bg=self.themes[self.current_theme]["btn_bg"]))
        self.next_btn.bind("<Enter>", lambda e: self.next_btn.config(bg=self.themes[self.current_theme]["btn_hover"]))
        self.next_btn.bind("<Leave>", lambda e: self.next_btn.config(bg=self.themes[self.current_theme]["btn_bg"]))
        
        style = ttk.Style()
        style.configure("pink.Horizontal.TProgressbar", troughcolor="#fff0f5", background=self.themes["Sakura"]["btn_bg"])

    def play_sound(self):
        self.click_sound.play()

    def change_theme(self, theme):
        self.current_theme = theme
        self.root.configure(bg=self.themes[theme]["bg"])
        self.label.config(bg=self.themes[theme]["bg"], fg=self.themes[theme]["fg"])
        self.start_btn.config(bg=self.themes[theme]["btn_bg"])
        if self.started:
            self.question_label.config(bg=self.themes[theme]["bg"], fg=self.themes[theme]["fg"])
            self.options_frame.config(bg=self.themes[theme]["bg"])
            self.next_btn.config(bg=self.themes[theme]["btn_bg"])
            self.prev_btn.config(bg=self.themes[theme]["btn_bg"])
            style = ttk.Style()
            style.configure("pink.Horizontal.TProgressbar", troughcolor="#fff0f5", background=self.themes[theme]["btn_bg"])
            self.show_question()

    def change_language(self, lang):
        self.language = "en" if lang == "English" else "cn"
        self.label.config(text=self.texts[self.language]["welcome"])
        self.start_btn.config(text=self.texts[self.language]["start"])
        if self.started:
            self.prev_btn.config(text=self.texts[self.language]["previous"])
            self.next_btn.config(text=self.texts[self.language]["next"])
            self.show_question()

    def start_questions(self):
        if not self.started:
            self.started = True
            self.start_frame.pack_forget()
            self.middle_frame.pack(pady=10, padx=20, fill="x")
            self.progress.pack(pady=10)
            self.question_label.pack(pady=15)
            self.options_frame.pack(pady=10)
            self.bottom_frame.pack(pady=30)
            self.prev_btn.pack(side=tk.LEFT, padx=20)
            self.next_btn.pack(side=tk.RIGHT, padx=20)
            self.show_question()

    def prev_question(self):
        print(f"Previous button clicked, current_question: {self.current_question}")
        self.play_sound()  # 播放音效
        if self.current_question > 0:
            if self.option_var.get() and self.option_var.get() != "UNSELECTED":
                if self.current_question < len(self.answers):
                    self.answers[self.current_question] = self.option_var.get()
                else:
                    self.answers.append(self.option_var.get())
            self.current_question -= 1
            print(f"Moving to question {self.current_question + 1}")
            self.show_question()
        else:
            print("Already at the first question!")

    def next_question(self):
        print(f"Next button clicked, current_question: {self.current_question}")
        self.play_sound()  # 播放音效
        if not self.option_var.get() or self.option_var.get() == "UNSELECTED":
            messagebox.showwarning(self.texts[self.language]["warning"], 
                                 self.texts[self.language]["select_option"])
            return
        if self.current_question < len(self.answers):
            self.answers[self.current_question] = self.option_var.get()
        else:
            self.answers.append(self.option_var.get())
        self.current_question += 1
        print(f"Moving to question {self.current_question + 1}")
        print(self.option_var.get()) # 確認選擇的答案
        self.show_question()

    def show_question(self):
        print(f"Showing question {self.current_question + 1}")
        for widget in self.options_frame.winfo_children():
            widget.destroy()
        
        if self.current_question < len(dest.questions):
            q = dest.questions[self.current_question]
            q_text = q['question_en'] if self.language == "en" else q['question_cn']
            options = q['options_en'] if self.language == "en" else q['options_cn']
            # 添加進度百分比
            percentage = (self.current_question + 1) / len(dest.questions) * 100
            self.question_label.config(text=f"Question {self.current_question + 1} of {len(dest.questions)} ({percentage:.0f}%): {q_text}")
            
            self.option_var.set("UNSELECTED")
            
            for option, text in options.items():
                btn = tk.Radiobutton(self.options_frame, text=f"{option}. {text}", 
                                   variable=self.option_var, value=text, font=("MS Gothic", 12, "bold"))
                btn.pack(anchor="w")
            
            if self.current_question < len(self.answers) and self.answers[self.current_question] in options.values():
                print(f"Setting option_var to previous answer: {self.answers[self.current_question]}")
                self.option_var.set(self.answers[self.current_question])
            else:
                print("No previous answer, keeping option_var as UNSELECTED")
                self.option_var.set("UNSELECTED")
            
            self.progress['value'] = self.current_question
        else:
            self.show_result()

    def show_result(self):
        # 檢查是否所有問題都已回答，且答案不為空
        if len(self.answers) != len(dest.questions):
            messagebox.showwarning(self.texts[self.language]["incomplete"],
                                  self.texts[self.language]["incomplete_msg"])
            self.current_question = len(self.answers)  # 跳轉到第一個未回答的問題
            self.show_question()
            return
        
        # 檢查是否有空答案
        for i, answer in enumerate(self.answers):
            if not answer or answer == "UNSELECTED":
                messagebox.showwarning(self.texts[self.language]["incomplete"],
                                      self.texts[self.language]["incomplete_msg"])
                self.current_question = i  # 跳轉到未回答的問題
                self.show_question()
                return
        if self.language == "cn":
            self.answers = dest.translate_answers_to_english(self.answers)
        print(f"Final answers: {self.answers}")
        recommendation = recommend.recommend_city(self.answers, dest.destinations)
        if recommendation:
            # 限制最多顯示 3 個推薦地點
            recommendation = recommendation[:3]
            
            result_window = tk.Toplevel(self.root)
            result_window.title(self.texts[self.language]["recommendation"])
            result_window.geometry("600x600")
            
            canvas = tk.Canvas(result_window)
            scrollbar = tk.Scrollbar(result_window, orient="vertical", command=canvas.yview)
            scrollable_frame = tk.Frame(canvas)
            
            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            
            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
            tk.Label(scrollable_frame, text=self.texts[self.language]["based_on"], font=("MS Gothic", 16, "bold")).pack(pady=10)
            
            self.photo_references = []
            
            # 載入默認圖片
            default_image_path = os.path.join(self.photo_dir, "default.jpg")
            
            for city, reasons in recommendation:
                tk.Label(scrollable_frame, text=city, font=("MS Gothic", 14, "bold")).pack(anchor="w", padx=10)
                for reason in reasons:
                    tk.Label(scrollable_frame, text=f"  - {reason}", font=("MS Gothic", 12)).pack(anchor="w", padx=20)
                
                for intro in dest.introduction:
                    if intro['name'] == city:
                        image_path = os.path.join(self.photo_dir, intro['image_url'])
                        if os.path.exists(image_path):
                            try:
                                image = Image.open(image_path)
                                image = image.resize((300, 200), Image.Resampling.LANCZOS)
                                photo = ImageTk.PhotoImage(image)
                                self.photo_references.append(photo)
                                tk.Label(scrollable_frame, image=photo).pack(pady=5)
                            except Exception as e:
                                if os.path.exists(default_image_path):
                                    image = Image.open(default_image_path)
                                    image = image.resize((300, 200), Image.Resampling.LANCZOS)
                                    photo = ImageTk.PhotoImage(image)
                                    self.photo_references.append(photo)
                                    tk.Label(scrollable_frame, image=photo).pack(pady=5)
                                else:
                                    tk.Label(scrollable_frame, text=f"Error loading image: {e}", font=("MS Gothic", 10), fg="red").pack()
                        else:
                            if os.path.exists(default_image_path):
                                image = Image.open(default_image_path)
                                image = image.resize((300, 200), Image.Resampling.LANCZOS)
                                photo = ImageTk.PhotoImage(image)
                                self.photo_references.append(photo)
                                tk.Label(scrollable_frame, image=photo).pack(pady=5)
                            else:
                                tk.Label(scrollable_frame, text="Image not found", font=("MS Gothic", 10), fg="red").pack()
                        
                        intro_text = intro['intro_en'] if self.language == "en" else intro['intro_cn']
                        tk.Label(scrollable_frame, text=f"{self.texts[self.language]['introduction']} {intro_text}", font=("MS Gothic", 12), wraplength=500).pack(anchor="w", padx=10, pady=5)
                        attractions = intro['attractions_en'] if self.language == "en" else intro['attractions_cn']
                        tk.Label(scrollable_frame, text=f"{self.texts[self.language]['attractions']} {', '.join(attractions)}", font=("MS Gothic", 12)).pack(anchor="w", padx=10, pady=5)
                        tk.Label(scrollable_frame, text=f"{self.texts[self.language]['recommended_days']} {intro['recommended_days']}", font=("MS Gothic", 12)).pack(anchor="w", padx=10, pady=5)
                        
                        # 添加交通建議和費用預估（假設 dest.py 已更新）
                        transportation = intro.get('transportation_en' if self.language == "en" else 'transportation_cn', "Not available")
                        estimated_cost = intro.get('estimated_cost', "Not available")
                        tk.Label(scrollable_frame, text=f"{self.texts[self.language]['transportation']} {transportation}", font=("MS Gothic", 12)).pack(anchor="w", padx=10, pady=5)
                        tk.Label(scrollable_frame, text=f"{self.texts[self.language]['estimated_cost']} {estimated_cost}", font=("MS Gothic", 12)).pack(anchor="w", padx=10, pady=5)
        else:
            messagebox.showinfo(self.texts[self.language]["recommendation"], 
                               self.texts[self.language]["no_recommendation"])
        
        self.next_btn.config(text=self.texts[self.language]["restart"], command=self.restart)

    def restart(self):
        self.answers = []
        self.current_question = 0
        self.started = False
        self.middle_frame.pack_forget()
        self.bottom_frame.pack_forget()
        self.start_frame.pack(pady=30)
        self.next_btn.config(text=self.texts[self.language]["next"], command=self.next_question)

if __name__ == "__main__":
    root = tk.Tk()
    app = TravelApp(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["London", "Berlin", "Paris", "Madrid"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Mars", "Venus", "Jupiter", "Mercury"],
                "correct_answer": "Mars"
            }
            # Add more questions
        ]

        self.score = 0
        self.current_question = 0

        self.label = tk.Label(root, text="Welcome to the Quiz Game!\nAnswer the following questions:")
        self.label.pack()

        self.question_label = tk.Label(root, text="")
        self.question_label.pack()

        self.radio_var = tk.IntVar()
        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.radio_var, value=i)
            self.radio_buttons.append(rb)
            rb.pack()

        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack()
        self.next_button.pack_forget()

        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        for i in range(4):
            self.radio_buttons[i].config(text=question_data["choices"][i])
        self.radio_var.set(-1)
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.pack_forget()

    def check_answer(self):
        selected_choice = self.radio_var.get()
        if selected_choice == -1:
            return
        question_data = self.questions[self.current_question]
        if question_data["choices"][selected_choice] == question_data["correct_answer"]:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            correct_index = question_data["choices"].index(question_data["correct_answer"])
            messagebox.showinfo("Result", f"Incorrect. The correct answer is: {question_data['choices'][correct_index]}")
        self.submit_button.config(state=tk.DISABLED)
        self.next_button.pack()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score: {self.score}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()

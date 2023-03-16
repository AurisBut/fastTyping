import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

import tkinter as tk
import random
import time
import nltk
import markovify

nltk.download('words')


class TypingPracticeApp:
    def __init__(self, master):
        self.master = master
        master.title("Typing Practice")

        self.words = nltk.corpus.words.words()
        self.sentences = self.generate_sentences()

        self.current_word = random.choice(self.words)
        self.current_sentence = random.choice(self.sentences)

        self.label_text = tk.StringVar()
        self.label_text.set(f"Type this word: {self.current_word}")
        self.label = tk.Label(master, textvariable=self.label_text)
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.bind("<Return>", self.check_input)
        self.entry.pack()

        self.result_text = tk.StringVar()
        self.result = tk.Label(master, textvariable=self.result_text)
        self.result.pack()

        self.start_time = time.time()

    @staticmethod
    def generate_sentences():
        with open("corpus.txt", "r") as f:
            text = f.read()
        text_model = markovify.Text(text)
        return [text_model.make_sentence() for _ in range(100)]

    def check_input(self, _):
        user_input = self.entry.get()
        if user_input == self.current_word:
            elapsed_time = time.time() - self.start_time
            self.result_text.set(f"Correct! Time taken: {elapsed_time:.2f} seconds")
            self.start_time = time.time()
        else:
            self.result_text.set("Incorrect, try again!")

        self.current_word = random.choice(self.words)
        self.current_sentence = random.choice(self.sentences)
        self.label_text.set(f"Type this word: {self.current_word}")
        self.entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TypingPracticeApp(root)
    root.mainloop()

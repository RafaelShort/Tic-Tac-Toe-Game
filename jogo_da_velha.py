import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.player_names = ["Jogador 1", "Jogador 2"]
        self.create_name_entry()

    def create_name_entry(self):
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(pady=20)

        title_label = tk.Label(self.entry_frame, text="Jogo da Velha", font=('Arial', 24))
        title_label.grid(row=0, columnspan=2)

        tk.Label(self.entry_frame, text="Nome do Jogador 1 (X):").grid(row=1, column=0)
        self.player1_entry = tk.Entry(self.entry_frame)
        self.player1_entry.grid(row=1, column=1)

        tk.Label(self.entry_frame, text="Nome do Jogador 2 (O):").grid(row=2, column=0)
        self.player2_entry = tk.Entry(self.entry_frame)
        self.player2_entry.grid(row=2, column=1)

        start_button = tk.Button(self.entry_frame, text="Iniciar Jogo", command=self.start_game)
        start_button.grid(row=3, columnspan=2, pady=10)

    def start_game(self):
        self.player_names[0] = self.player1_entry.get() or "Jogador 1"
        self.player_names[1] = self.player2_entry.get() or "Jogador 2"
        self.entry_frame.pack_forget()
        self.player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_symbols()

    def create_symbols(self):
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.game_frame, text="", font=('normal', 40), width=5, height=2,
                                               command=lambda i=i, j=j: self.click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, i, j):
        if self.buttons[i][j]["text"] == "" and not self.check_winner():
            self.buttons[i][j]["text"] = self.player
            if self.check_winner():
                messagebox.showinfo("Jogo da Velha", f"{self.player_names[0] if self.player == 'X' else self.player_names[1]} venceu!")
                self.show_restart_options()
            elif self.check_tie():
                messagebox.showinfo("Jogo da Velha", "Empate!")
                self.show_restart_options()
            else:
                self.player = "O" if self.player == "X" else "X"

    def show_restart_options(self):
        self.restart_frame = tk.Frame(self.root)
        self.restart_frame.pack(pady=20)

        restart_button = tk.Button(self.restart_frame, text="Reiniciar Jogo", command=self.reset_game)
        restart_button.pack(side=tk.LEFT, padx=10)

        new_game_button = tk.Button(self.restart_frame, text="Voltar à Tela Inicial", command=self.return_to_start)
        new_game_button.pack(side=tk.LEFT, padx=10)

    def check_winner(self):
        for i in range(3):
            if self.buttons[i][0]["text"] == self.buttons[i][1]["text"] == self.buttons[i][2]["text"] != "":
                return True
            if self.buttons[0][i]["text"] == self.buttons[1][i]["text"] == self.buttons[2][i]["text"] != "":
                return True
        if self.buttons[0][0]["text"] == self.buttons[1][1]["text"] == self.buttons[2][2]["text"] != "":
            return True
        if self.buttons[0][2]["text"] == self.buttons[1][1]["text"] == self.buttons[2][0]["text"] != "":
            return True
        return False

    def check_tie(self):
        return all(button["text"] for row in self.buttons for button in row)

    def reset_game(self):
        for row in self.buttons:
            for button in row:
                button["text"] = ""
        self.player = "X"
        self.restart_frame.pack_forget()  # Remove o frame de reinício

    def return_to_start(self):
        self.restart_frame.pack_forget()  # Remove o frame de reinício
        self.game_frame.pack_forget()  # Remove o frame do jogo
        self.create_name_entry()  # Volta para a tela de escolha de nomes

if __name__ == "__main__":
    root = tk.Tk()
    game = JogoDaVelha(root)
    root.mainloop()

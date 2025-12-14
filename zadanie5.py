class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = [] 
        self.solutions = []

    def place(self, row, col):
        self.queens.append((row, col))

    def remove(self, row, col):
        if self.queens and self.queens[-1] == (row, col):
             self.queens.pop()

    def is_safe(self, row, col):
        for q_row, q_col in self.queens:
            if q_col == col:
                return False
            if abs(q_row - row) == abs(q_col - col):
                return False
        return True

    def _solve_recursive(self, row=0):
        if row == self.n:
            self.solutions.append(list(self.queens))
            return

        for col in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                self._solve_recursive(row + 1)
                self.remove(row, col)

    def solve(self):
        self.solutions = []
        self._solve_recursive(row=0)
        return self.solutions
    
    def __str__(self):
        output = []
        queen_cols = {r: c for r, c in self.queens}
        for r in range(self.n):
            row_str = ""
            for c in range(self.n):
                if queen_cols.get(r) == c:
                    row_str += " Q "
                else:
                    row_str += " . "
            output.append(row_str.strip())
        
        header = f"Szachownica {self.n}x{self.n} (Królowe: {len(self)}):"
        return f"{header}\n" + "\n".join(output)

    def __repr__(self):
        return f"Board(n={self.n}, queens={self.queens})"

    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        yield from self.queens

    def __contains__(self, pos):
        return pos in self.queens

# --- Funkcja Uruchamiająca ---

def solve_n_queens(n=8):
    board = Board(n)
    solutions = board.solve()
    return solutions

# --- Sekcja Testowa ---

if __name__ == "__main__":
    
    print("### Testowanie Algorytmu N Królowych ###")
    print("---------------------------------------")

    test_cases = [1, 2, 3, 4, 8]
    expected_results = {1: 1, 2: 0, 3: 0, 4: 2, 8: 92}
    
    for n in test_cases:
        solutions = solve_n_queens(n)
        count = len(solutions)
        expected = expected_results[n]
        status = "PASSED" if count == expected else "FAILED"
        
        print(f"solve({n}) -> Znaleziono: {count} rozwiązań (Oczekiwano: {expected}) [{status}]")

    print("\n---------------------------------------")
    print("### Przykład Rozwiązania i Użycia Magicznych Metod (N=4) ###")
    
    solutions_4 = solve_n_queens(4)
    if solutions_4:
        example_board = Board(4)
        example_board.queens = solutions_4[0]
        
        print("\n1. Reprezentacja __str__ (print(board)):")
        print(example_board)
        
        print(f"\n2. Metoda __len__: Liczba królowych: {len(example_board)}")
        
        print("\n3. Metoda __iter__: Iteracja po pozycjach:")
        print(list(example_board))
        
        pos_to_check = (0, 1) # Pozycja, która jest królową w tym rozwiązaniu (dla N=4)
        print(f"\n4. Metoda __contains__: Czy zawiera królową na {pos_to_check}? {pos_to_check in example_board}")
        
        print(f"\n5. Metoda __repr__: Reprezentacja dla programisty:\n{repr(example_board)}")

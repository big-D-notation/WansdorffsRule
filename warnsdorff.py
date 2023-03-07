import numpy as np


class Warnsdorf():
    '''
        Клас для розв'язання задачі
        "Хід конем" за Правилом Вансдорфа
    '''

    EMPTY   = 0
    VISITED = 1
    KNIGHT  = 7

    MOVES = (
        (2, 1), (-2, -1), (-2, 1), (2, -1),
        (1, 2), (-1, -2), (-1, 2), (1, -2)
    )


    def __init__(self, board_size, knight_pos):
        self.chessboard = np.zeros(board_size)
        self.knight_pos = knight_pos
        self.chessboard[knight_pos] = self.KNIGHT
        self.chessboard_path = np.zeros(board_size)
        self.move_number = 0
        self.has_next_move = True
    
    def solve(self):
        '''
            Знаходить розв'язок

            Повертає кортеж з трьох елементів:
            - результуюча шахівниця
            - шлях
            - True, якщо вся шахівниця відвідана, інакше False
        '''
        while self.__has_next():
            _ = self.__next()
        return (
            self.chessboard,
            self.chessboard_path,
            self.__is_all_visited()
        )

    def __is_all_visited(self):
        '''
            Перевіряє, чи всі клітинки відвідані
        '''
        return not self.EMPTY in self.chessboard
    

    def __has_next(self):
        '''
            Перевіряє, чи є наступний хід
        '''
        return self.has_next_move


    def __next(self):
        '''
            Повертає наступний хід
        '''
        moves = self.__find_moves(self.knight_pos)
        self.chessboard[self.knight_pos] = self.VISITED
        next_cell = self.__find_next_cell(moves)
        self.chessboard_path[(self.knight_pos)] = self.move_number
        self.move_number += 1 

        if next_cell is None:
            self.chessboard[self.knight_pos] = self.KNIGHT
            self.has_next_move = False
        else:
            self.knight_pos = next_cell
            self.chessboard[next_cell] = self.KNIGHT

        return next_cell


    def __find_moves(self, start_pos):
        '''
            Повертає координати можливих ходів
        '''
        legal_moves = []

        for move in self.MOVES:
            new_cell = (
                start_pos[0] + move[0],
                start_pos[1] + move[1],
            )

            if self.__is_cell_legal(new_cell):
                legal_moves.append(new_cell)


        return legal_moves


    def __find_next_cell(self, cells):
        '''
            Серед ходів знаходить той, 
            що має найменше можливих майбутніх ходів
        '''
        weight = float('inf')
        index = None

        for i, cell in enumerate(cells):
            new_weight = len(self.__find_moves(cell))
            if new_weight < weight:
                weight = new_weight
                index = i
        if index == None:
            return None

        return cells[index]
    

    def __is_cell_legal(self, cell):
        '''
            Перевіряє, чи клітинка відвідана та
            чи не виходить за межі шахівниці
            
        '''
        if cell[0] < 0 or cell[1] < 0:
            return False
        
        if cell[0] > len(self.chessboard[0]) - 1 or cell[1] > len(self.chessboard) - 1:
            return False
        
        if self.chessboard[cell] == self.VISITED:
            return False
        
        return True

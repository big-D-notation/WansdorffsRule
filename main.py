from warnsdorff import Warnsdorf
from config import board_config

'''
    05-07 Бер 2023, Андрій С.
    Розв'язання задачі "Хід конем" за Правилом Вансдорфа
'''

if __name__ == '__main__':
    board_size = board_config['size']
    knight_pos = board_config['knight']
   
    solver = Warnsdorf(
        board_size,
        knight_pos
    )

    _, path, res = solver.solve()

    with open('res.txt', mode='w') as f:
        f.write('Path finded\n' if res else 'Path not finded\n')
        for row in path:
            f.write(str(row) + '\n')

    

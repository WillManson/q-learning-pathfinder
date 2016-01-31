class FileManager:
    def load_map(self, file_name):
        board = []
        with open('maps/' + file_name, 'r') as f:
            for y, line in enumerate(f.readlines()):
                board.append([])
                for x, cell in enumerate(line):
                    if cell != '\n':
                        board[y].append(cell)
        return board

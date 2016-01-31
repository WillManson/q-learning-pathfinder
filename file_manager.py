class FileManager:
    def load_map(self, file_name):
        game_map = []
        with open('maps/' + file_name, 'r') as f:
            for y, line in enumerate(f.readlines()):
                game_map.append([])
                for x, cell in enumerate(line):
                    if cell != '\n':
                        game_map[y].append(cell)
        return game_map

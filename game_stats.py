class GameStats():
    '''Armazena dados estatísticos da Invasão Alienígena.'''
    
    def __init__(self, ai_settings):
        '''Inicializa os dados estatísticos.'''
        self.ai_settings = ai_settings
        self.reset_stats()

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0
        self.read_high_score()

        # Inicia o jogo em um estado inativo
        self.game_active = False
        
    def reset_stats(self):
        '''Inicializa os dados estatísticos que podem mudar durante o jogo.'''
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    def read_high_score(self):
        '''Lê a pontuação máxima do arquivo score.txt'''
        try:
            with open('score.txt', 'r') as file:
                n = int(file.readline())
                if type(n) == int:
                    self.high_score = n
        except: pass

    def write_high_score(self):
        '''Escreve a pontuação máxima no arquivo score.txt'''
        with open('score.txt', 'w') as file:
            file.write(str(self.high_score))

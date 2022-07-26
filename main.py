from programas import Filme, Serie
from playlists import Playlist

# Declaração de filmes e séries
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

# Simulação de sistema de likes
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

# criação da playlist
listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

# Exibição da playlist e seu tamanho
for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho da lista: {len(minha_playlist.listagem)}')


class SongRegisterView:
    def register_song_initial(self):
        print("Implementar nova Musica \n\n")

        title = input("Determine o nome da musica: ")
        artist = input("Determine o nome do artista: ")
        year = input("Determine o ano de publicação: ")

        new_song_informations = {
            "title": title,
            "artist": artist,
            "year": year
        }

        return new_song_informations
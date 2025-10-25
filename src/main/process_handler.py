
def start() -> None:
    while True:
        
        command = input()
        if command == "1": print("Inserindo música")
        elif command == "2": print("Criando Playlist")
        elif command == "5": exit()
        else: print("\n Comando não encontrado, tente novamente! \n\n")
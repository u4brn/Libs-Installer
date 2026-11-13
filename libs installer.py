import os, subprocess, sys, time

usuario = os.path.expanduser("~")
info = sys.version
if info[3] != ".":
    py = info[0] + info[2] + info[3]
else:
    py = info[0] + info[2]
sq_bit = f"{usuario}\\AppData\\Local\\Programs\\Python\\Python{py}\\Lib\\site-packages"
td_bit = f"{usuario}\\AppData\\Local\\Programs\\Python\\Python{py}-32\\Lib\\site-packages"

def dig(texto, delay=0.03):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(delay)
    print()
def ler(texto, delay=0.01):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(delay)
    return input()
def linha(x):
    dig("=" * x)
def lmp():
    os.system("cls" if os.name == "nt" else "clear")
def entrada_invalida():
    lmp()
    dig("Entrada inválida.")
    time.sleep(1)
    lmp()
def menu():
    lmp()
    sem_entrada = True
    while sem_entrada:
        try:
            opcao = int(ler("[1] Instalar biblioteca\n[2] Reparar biblioteca\n[3] Desinstalar biblioteca\n[4] Sair\n> "))
            if opcao == 1:
                lmp()
                parar = False
                while not parar:
                    lmp()
                    biblioteca = ler("Digite o nome da biblioteca, /r para voltar ou /e para sair:\n> ").strip().lower()
                    if biblioteca == "/r" or biblioteca == "/return":
                        lmp()
                        parar = True
                    elif biblioteca == "/e" or biblioteca == "/exit":
                        exit()
                    else:
                        lmp()
                        if not os.path.exists(f"{sq_bit}\\{biblioteca}") and not os.path.exists(f"{td_bit}\\{biblioteca}"):
                            try:
                                subprocess.run([sys.executable, "-m", "pip", "install", f"{biblioteca}"], check=True)
                                dig(f'"{biblioteca.upper()}" foi instalada com sucesso!')
                            except Exception as erro:
                                input(f"Ocorreu um erro. Possíveis causas: biblioteca inexistente ou conexão instável.\nSaída: {erro}")
                        else:
                            dig(f'"{biblioteca.upper()}" já está instalada.')
            elif opcao == 2:
                lmp()
                parar = False
                while not parar:
                    lmp()
                    biblioteca = ler("Digite o nome da biblioteca, /r para voltar ou /e para sair:\n> ").strip().lower()
                    if biblioteca == "/r" or biblioteca == "/return":
                        lmp()
                        parar = True
                    elif biblioteca == "/e" or biblioteca == "/exit":
                        exit()
                    else:
                        lmp()
                        if os.path.exists(f"{sq_bit}\\{biblioteca}") or os.path.exists(f"{td_bit}\\{biblioteca}"):
                            try:
                                subprocess.run([sys.executable, "-m", "pip", "install", "--force-reinstall", f"{biblioteca}"], check=True)
                                dig(f'"{biblioteca.upper()}" foi reparada com sucesso!')
                            except Exception as erro:
                                input(f"Ocorreu um erro. Possível causa: conexão instável.\nSaída: {erro}")
                        else:
                            dig(f'"{biblioteca.upper()}" não está instalada.')
            elif opcao == 3:
                lmp()
                parar = False
                while not parar:
                    lmp()
                    biblioteca = ler("Digite o nome da biblioteca, /r para voltar ou /e para sair:\n> ").strip().lower()
                    if biblioteca == "/r" or biblioteca == "/return":
                        lmp()
                        parar = True
                    elif biblioteca == "/e" or biblioteca == "/exit":
                        exit()
                    else:
                        lmp()
                        if os.path.exists(f"{sq_bit}\\{biblioteca}") or os.path.exists(f"{td_bit}\\{biblioteca}"):
                            try:
                                subprocess.run([sys.executable, "-m", "pip", "uninstall", f"{biblioteca}", "-y"], check=True)
                                dig(f'"{biblioteca.upper()}" foi desinstalada com sucesso!')
                            except Exception as erro:
                                input(f"Ocorreu um erro desconhecido.\nSaída: {erro}")
                        else:
                            dig(f'"{biblioteca.upper()}" não está instalada.')
            elif opcao == 4:
                exit()
            else:
                entrada_invalida()
        except ValueError:
            entrada_invalida()
                           
linha(14)
dig("Libs Installer")
linha(14)
time.sleep(1)

menu()
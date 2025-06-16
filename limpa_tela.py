def limpa_tela():
    import subprocess
    import platform

    # Limpa o terminal
    subprocess.run('cls' if platform.system() == 'Windows' else 'clear', shell=True)
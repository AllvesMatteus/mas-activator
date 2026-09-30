import os
import sys
import ctypes
import subprocess
import platform

# ─── Resolve diretorio base (funciona em .py e .exe gerado pelo PyInstaller) ─────
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))

# ─── Definicao dos scripts de ativacao ───────────────────────────────────────────
SCRIPTS = {
    "1": {
        "titulo":  "Ativar WINDOWS",
        "subtitulo": "Windows 10 / 11",
        "descricao": "Ativacao PERMANENTE vinculada ao hardware do PC. Nao precisa de internet.",
        "detalhe": "Metodo: HWID (Digital License)",
        "file": os.path.join(SCRIPT_DIR, "MAS", "Separate-Files-Version", "Activators", "HWID_Activation.cmd"),
        "arg":   "/HWID",
        "cor_titulo": "\033[92m",
        "cor_badge":  "\033[42m\033[30m",
        "badge": " PERMANENTE ",
    },
    "2": {
        "titulo":  "Ativar OFFICE",
        "subtitulo": "Word, Excel, PowerPoint, Outlook...",
        "descricao": "Ativacao PERMANENTE de qualquer versao do Office. Funciona offline.",
        "detalhe": "Metodo: Ohook",
        "file": os.path.join(SCRIPT_DIR, "MAS", "Separate-Files-Version", "Activators", "Ohook_Activation_AIO.cmd"),
        "arg":   "/Ohook",
        "cor_titulo": "\033[93m",
        "cor_badge":  "\033[42m\033[30m",
        "badge": " PERMANENTE ",
    },
    "3": {
        "titulo":  "Ativar WINDOWS + OFFICE + ESU",
        "subtitulo": "Todas as versoes do Windows e Office",
        "descricao": "Ativacao PERMANENTE de tudo. Suporta Windows 7, 8, 8.1, 10 e 11.",
        "detalhe": "Metodo: TSforge (mais avancado)",
        "file": os.path.join(SCRIPT_DIR, "MAS", "Separate-Files-Version", "Activators", "TSforge_Activation.cmd"),
        "arg":   "/Z-WindowsESUOffice",
        "cor_titulo": "\033[94m",
        "cor_badge":  "\033[42m\033[30m",
        "badge": " PERMANENTE ",
    },
    "4": {
        "titulo":  "Ativar com KMS Online",
        "subtitulo": "Windows + Office (requer internet)",
        "descricao": "Ativacao por 180 dias com renovacao automatica. Ideal se os outros falharem.",
        "detalhe": "Metodo: Online KMS",
        "file": os.path.join(SCRIPT_DIR, "MAS", "Separate-Files-Version", "Activators", "Online_KMS_Activation.cmd"),
        "arg":   "/K-WindowsOffice",
        "cor_titulo": "\033[96m",
        "cor_badge":  "\033[43m\033[30m",
        "badge": " 180 DIAS   ",
    },
}

# ─── Constantes de cor ANSI ──────────────────────────────────────────────────────
R     = "\033[0m"
BOLD  = "\033[1m"
DIM   = "\033[2m"
RED   = "\033[91m"
GREEN = "\033[92m"
YEL   = "\033[93m"
BLUE  = "\033[94m"
CYAN  = "\033[96m"
WHITE = "\033[97m"
GRAY  = "\033[90m"
BG_D  = "\033[100m"

# ─── Detecta melhor opcao para este PC ──────────────────────────────────────────
def detectar_melhor_opcao():
    try:
        major = sys.getwindowsversion().major
        return "1" if major >= 10 else "3"
    except Exception:
        return "1"

# ─── Habilita cores ANSI no Windows ──────────────────────────────────────────────
def enable_ansi():
    if platform.system() == "Windows":
        os.system("")
        try:
            ctypes.windll.kernel32.SetConsoleMode(
                ctypes.windll.kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

# ─── Verifica se o processo e administrador ───────────────────────────────────────
def is_admin():
    try:
        return bool(ctypes.windll.shell32.IsUserAnAdmin())
    except Exception:
        return False

# ─── Eleva privilegios ───────────────────────────────────────────────────────────
def elevar_admin():
    script = os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else sys.argv[0])
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", script, " ".join(sys.argv[1:]), None, 1)
    except Exception as e:
        print(f"\n{RED}  Erro ao solicitar permissao de Administrador: {e}{R}")
        input("\n  Pressione Enter para sair...")
    sys.exit(0)

# ─── Checa existencia dos scripts ────────────────────────────────────────────────
def verificar_scripts():
    return [v["titulo"] for v in SCRIPTS.values() if not os.path.isfile(v["file"])]

# ─── Linha separadora ────────────────────────────────────────────────────────────
SEP = GRAY + "  " + chr(8212)*54 + R

# ─── Cabecalho ───────────────────────────────────────────────────────────────────
def cabecalho():
    os.system("cls")
    print()
    print(f"  {BOLD}{WHITE}  Microsoft Activation Scripts  v3.12{R}")
    print(f"  {GRAY}  Baseado no projeto MAS | massgrave.dev{R}")
    print(f"  {GRAY}  Launcher por AllvesMatteus (github.com/AllvesMatteus){R}")
    print()
    print(SEP)
    print()

# ─── Renderiza uma opcao do menu ────────────────────────────────────────────────
def render_opcao(k, v, melhor):
    eh_recomendado = (k == melhor)
    cor = v["cor_titulo"]
    badge_cor = v["cor_badge"]
    badge = v["badge"]

    # Linha principal: numero + titulo + badge + RECOMENDADO
    recom_str = ""
    if eh_recomendado:
        recom_str = f"  {BOLD}{YEL}[RECOMENDADO PARA VOCE]{R}"

    print(f"  {cor}{BOLD}  {k}.  {v['titulo']}{R}{recom_str}")
    print(f"      {WHITE}{v['subtitulo']}{R}")
    print()
    print(f"      {v['descricao']}")
    print(f"      {GRAY}{v['detalhe']}{R}   {badge_cor}{BOLD}{badge}{R}")
    print()

# ─── Menu principal ──────────────────────────────────────────────────────────────
def menu():
    melhor = detectar_melhor_opcao()

    while True:
        cabecalho()
        print(f"  {BOLD}  O que voce quer ativar?{R}")
        print()

        for k, v in SCRIPTS.items():
            render_opcao(k, v, melhor)
            print(SEP)
            print()

        print(f"  {RED}  5.  Sair{R}")
        print()
        print(f"  {GRAY}  Dica: se nao souber qual escolher, pressione Enter.{R}")
        print(f"  {GRAY}  A opcao recomendada sera selecionada automaticamente.{R}")
        print()

        opcao = input(f"  {BOLD}  Digite o numero e pressione Enter [{melhor}]: {R}").strip() or melhor

        if opcao == "5":
            print(f"\n  {GRAY}  Ate mais!{R}\n")
            break

        if opcao not in SCRIPTS:
            print(f"\n  {RED}  Opcao invalida. Digite um numero de 1 a 5.{R}")
            input(f"  {GRAY}  Pressione Enter para tentar novamente...{R}")
            continue

        info     = SCRIPTS[opcao]
        cmd_path = info["file"]
        cmd_arg  = info["arg"]

        if not os.path.isfile(cmd_path):
            print(f"\n  {RED}  Arquivo nao encontrado:{R}")
            print(f"  {GRAY}  {cmd_path}{R}")
            print(f"\n  {YEL}  O EXE precisa estar na mesma pasta que a pasta MAS.{R}")
            input(f"\n  {GRAY}  Pressione Enter para voltar...{R}")
            continue

        # ── Confirmacao antes de executar ──
        os.system("cls")
        print()
        print(f"  {BOLD}  Voce escolheu:{R}")
        print()
        print(f"  {info['cor_titulo']}{BOLD}  {info['titulo']}{R}")
        print(f"      {info['descricao']}")
        print()
        print(SEP)
        print()
        confirmar = input(f"  {BOLD}  Confirmar e iniciar a ativacao? (S/N) [{YEL}S{R}{BOLD}]: {R}").strip().upper() or "S"

        if confirmar != "S":
            continue

        print()
        print(f"  {GREEN}  Iniciando ativacao...{R}")
        print(f"  {GRAY}  Nao feche esta janela. Aguarde o processo terminar.{R}")
        print()

        try:
            subprocess.run(["cmd.exe", "/c", cmd_path, cmd_arg])
        except Exception as e:
            print(f"\n  {RED}  Erro ao executar:{R} {e}")

        print()
        print(SEP)
        input(f"\n  {GRAY}  Pronto! Pressione Enter para voltar ao menu...{R}")

# ─── Entry-point ─────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    enable_ansi()

    # 1. Garante admin
    if not is_admin():
        print("Solicitando permissao de Administrador...")
        elevar_admin()

    # 2. Checa scripts
    faltando = verificar_scripts()
    if faltando:
        os.system("cls")
        print(f"\n  {RED}{BOLD}  ERRO: Arquivos nao encontrados!{R}\n")
        for nome in faltando:
            print(f"  {GRAY}  - {nome}{R}")
        print(f"\n  {YEL}  Certifique-se de que o EXE esta na mesma pasta que a pasta MAS.{R}")
        print(f"  {GRAY}  Estrutura correta:{R}")
        print(f"  {GRAY}    Ativador KMS/{R}")
        print(f"  {GRAY}      MAS - Ativador Windows e Office.exe  <-- este arquivo{R}")
        print(f"  {GRAY}      MAS/  <-- esta pasta deve existir aqui{R}\n")
        input("  Pressione Enter para sair...")
        sys.exit(1)

    # 3. Exibe menu
    menu()

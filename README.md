<p align="center">
  <img src="activate_office.png" alt="MAS Logo" width="80">
</p>

<h1 align="center">MAS — Ativador Windows e Office</h1>

<p align="center">
  <strong>Launcher criado por <a href="https://github.com/AllvesMatteus">AllvesMatteus</a></strong><br>
  Baseado no projeto open-source <a href="https://github.com/massgravel/Microsoft-Activation-Scripts">Microsoft Activation Scripts (MAS)</a> de massgravel.
</p>

<p align="center">
  <a href="https://github.com/AllvesMatteus/mas-activator/releases"><img src="https://img.shields.io/github/v/release/AllvesMatteus/mas-activator?label=versao&color=4caf50" alt="Versao"></a>
  <img src="https://img.shields.io/badge/Windows-10%20%7C%2011-blue" alt="Windows">
  <img src="https://img.shields.io/badge/Office-Todas%20as%20vers%C3%B5es-orange" alt="Office">
  <img src="https://img.shields.io/badge/Licenca-MIT-lightgrey" alt="Licenca">
</p>

---

## O que e isso?

Este repositorio e um **launcher** (`.exe`) que simplifica o uso do [MAS (Microsoft Activation Scripts)](https://massgrave.dev), um ativador open-source para Windows e Office.

> **Aviso:** Este projeto foi criado por mim, **AllvesMatteus**, mas e totalmente baseado no trabalho original do time [massgravel](https://github.com/massgravel). Todo o credito pelos scripts de ativacao vai para eles.

---

## Como usar

1. Baixe o `MAS - Ativador Windows e Office.exe` na pagina de [Releases](https://github.com/AllvesMatteus/mas-activator/releases)
2. Mantenha o `.exe` na **mesma pasta** que a pasta `MAS/`
3. Clique duas vezes no `.exe`
4. Aceite a solicitacao de **Administrador** quando aparecer
5. Escolha o que voce quer ativar no menu e pressione Enter

---

## Metodos de Ativacao

| # | O que ativa | Duracao | Requer internet? |
|---|-------------|---------|-----------------|
| **1** | Windows 10 / 11 | Permanente | Nao |
| **2** | Office (qualquer versao) | Permanente | Nao |
| **3** | Windows + Office + ESU (todas as versoes) | Permanente | Nao |
| **4** | Windows + Office via KMS | 180 dias (auto-renovavel) | Sim |

---

## Estrutura do Projeto

```
Ativador KMS/
├── MAS - Ativador Windows e Office.exe   <- execute este arquivo
├── launcher.py                            <- codigo-fonte do launcher
├── launcher.spec                          <- configuracao do PyInstaller
├── icon.ico                               <- icone do executavel
└── MAS/
    └── Separate-Files-Version/
        └── Activators/
            ├── HWID_Activation.cmd
            ├── Ohook_Activation_AIO.cmd
            ├── TSforge_Activation.cmd
            └── Online_KMS_Activation.cmd
```

---

## Como recompilar o EXE

```bash
pip install pyinstaller
pyinstaller launcher.spec --distpath . --workpath build_tmp --noconfirm
```

---

## Creditos

- **Launcher / Interface:** [AllvesMatteus](https://github.com/AllvesMatteus)
- **Scripts de ativacao:** [massgravel/Microsoft-Activation-Scripts](https://github.com/massgravel/Microsoft-Activation-Scripts)

---

## Aviso Legal

Este projeto e disponibilizado **apenas para fins educacionais e de pesquisa**.  
O uso de ativadores pode violar os Termos de Servico da Microsoft.  
Use por sua conta e risco.

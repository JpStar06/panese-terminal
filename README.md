# --{[Panese Terminal]}--

> Pequeno assistente pessoal de terminal com personalidade, memória e emoções.

---

## --{[Sobre]}--

**Panese** (também chamada de **Aiko**) é uma assistente pessoal que roda direto no terminal. Ela aprende com você, reage com emoções e responde de forma personalizada, tudo por linha de comando.

Escrita só com a biblioteca padrão do Python, com arquitetura modular (núcleo, serviços, decoradores e plugins).

---

## --{[Funcionalidades]}--

- 💬 **Conversa** — encontra a resposta mais parecida (ignora maiúsculas, acentos e pontuação; tolera pequenos erros de digitação)
- 🧠 **Aprendizado** — quando não entende, pergunta e memoriza a resposta **na memória do seu usuário**
- 💗 **Emoções** — modos de personalidade que mudam o jeito de responder (`/modo`)
- 🔐 **Contas** — login com senha protegida por hash (PBKDF2) e memória separada por usuário
- 🎨 **Cores** — interface colorida via ANSI (`/color`)
- ⌨️ **Comandos com `/`** — registrados por decorador; plugins na pasta `plugins/` são carregados sozinhos
- 🎬 **Banner animado** linha a linha

---

## --{[Como usar]}--

Requisitos: Python 3.8+ (Linux, macOS ou Windows). Não há dependências externas.

```
git clone https://github.com/JpStar06/panese-terminal.git
cd panese-terminal
python main.py
```

Na primeira execução, escolha **[2] Criar conta**. O username aceita 3 a 20 letras, números ou `_`, e a senha precisa de pelo menos 6 caracteres.

### Comandos

| Comando | O que faz |
| --- | --- |
| `/help [comando]` | lista os comandos ou detalha um deles |
| `/modo <normal\|femboy\|tsundere>` | muda a personalidade |
| `/color <cor>` | muda a cor das respostas |
| `/horario` | mostra a hora atual |
| `/ping` | teste rápido |
| `/exit` | sai do programa |

### Exemplo

```
você: oi aiko
Panese: Oii! Como você tá? 💗

você: qual meu filme favorito?
Panese: Não entendi...
Ensinar? (s/n): s
Resposta: Interestelar
Panese: Aprendi isso 💗
```

---

## --{[Estrutura]}--

```
panese-terminal/
├── main.py              # login, carga da memória e loop de conversa
├── core/
│   ├── bot.py           # comandos principais (color, help, modo, exit)
│   ├── chat.py          # busca de respostas e entrada/saída da conversa
│   ├── state.py         # estado da sessão (AikoState)
│   └── ui.py            # painéis de comandos e de ajuda
├── services/
│   ├── auth.py          # contas, hash de senha e login
│   ├── banner.py        # banners animados
│   ├── emotions.py      # efeitos dos modos de personalidade
│   ├── io.py            # print_lento e leitura com timeout
│   ├── learning.py      # normalização, carga e aprendizado de respostas
│   └── storage.py       # JSON atômico e caminhos de dados
├── decorators/          # @comando e @aiko_responde
├── plugins/             # um arquivo = um comando novo
├── data/
│   ├── aiko_dados.json  # respostas base (versionado)
│   ├── users/           # contas (NÃO versionado)
│   └── memoria/         # o que cada usuário ensinou (NÃO versionado)
└── tests/               # testes com pytest
```

### Criando um plugin

```python
# plugins/dado.py
import random
from decorators.aiko import aiko_responde
from decorators.commands import comando

@comando("dado", "rola um dado", "Sorteia um número de 1 a 6")
@aiko_responde()
def dado(args, ctx=None, state=None):
    return f"saiu {random.randint(1, 6)}!"
```

---

## --{[Dados e privacidade]}--

- `data/aiko_dados.json`: respostas padrão. Use `{usuario}` para citar o nome de quem está logado.
- `data/memoria/<usuario>.json`: o que cada usuário ensinou; é somado às respostas padrão ao entrar.
- `data/users/<usuario>.json`: guarda só o hash da senha. Contas antigas em texto puro são convertidas no primeiro login.
- Se um JSON estiver corrompido, ele é movido para `*.corrompido-<timestamp>` em vez de ser sobrescrito.
- As pastas `users/` e `memoria/` estão no `.gitignore` — não envie senhas ao GitHub.

---

## --{[Testes]}--

```
pip install -r requirements-dev.txt
python -m pytest
```

---

## 🤝 Contribuindo

1. Faça um fork e crie uma branch: `git checkout -b feat/minha-feature`
2. Commit: `git commit -m "feat: minha feature"`
3. Abra um Pull Request

## 📄 Licença

Ainda não definida.

---

Feito com 💗 por [JpStar06](https://github.com/JpStar06)

# --{[Panese Terminal]}--

> Pequeno assistente pessoal de terminal com personalidade, memória e emoções.

---

## --{[Sobre]}--

**Panese** (também chamada de **Aiko**) é uma assistente pessoal que roda direto no terminal. Ela aprende com você, reage com emoções e responde de forma personalizada — tudo via linha de comando, sem interface gráfica.

O projeto é escrito inteiramente em **Python** e segue uma arquitetura modular com separação entre núcleo, serviços e decoradores.

---

## --{[Funcionalidades]}--

- 💬 **Conversa natural** — responde perguntas e frases do usuário
- 🧠 **Aprendizado** — quando não entende algo, pergunta e memoriza a resposta para o futuro
- 💗 **Emoções** — aplica estados emocionais nas respostas para deixá-las mais expressivas
- 🎨 **Cores personalizáveis** — interface colorida no terminal via ANSI
- ⌨️ **Comandos com `/`** — sistema de comandos registrados acessíveis com barra
- 📦 **Persistência de dados** — salva e carrega memória de um arquivo JSON
- 🎬 **Banner animado** — tela de boas-vindas animada ao iniciar

---

## --{[Estrutura do Projeto]}--

```
panese-terminal/
├── main.py              # Ponto de entrada principal
├── core/
│   ├── bot.py           # Registro e execução de comandos
│   ├── chat.py          # Processamento da conversa
│   ├── state.py         # Estado global da Aiko (AikoState)
│   └── ui.py            # Geração do painel de comandos
├── services/
│   ├── banner.py        # Banner animado de boas-vindas
│   ├── emotions.py      # Sistema de emoções
│   ├── io.py            # Saída lenta (print_lento)
│   ├── learning.py      # Lógica de aprendizado
│   └── storage.py       # Leitura/escrita de JSON
├── decorators/          # Decoradores auxiliares
├── data/
│   └── aiko_dados.json  # Memória persistida da Aiko
└── README.md
```

---

## --{[Como usar]}--

### Pré-requisitos

- Python 3.8+

### --{Instalação}--

```bash
git clone https://github.com/JpStar06/panese-terminal.git
cd panese-terminal
```

> Não há dependências externas — o projeto usa apenas a biblioteca padrão do Python.

### --{Executando}--

```bash
python main.py
```

---

## --{[Interagindo com a Aiko]}--

Após iniciar, você verá o banner e o painel de comandos. A partir daí, é só digitar:

**Conversa normal:**
```
Você: oi aiko
Panese: Oii! Como você tá? 💗
```

**Quando ela não entende:**
```
Você: qual meu filme favorito?
Panese: Não entendi...
Ensinar? (s/n): s
Resposta: Interestelar
Panese: Aprendi isso 💗
```

**Comandos com barra:**
```
Você: /ajuda
```

---

## --{[Dados e Memória]}--

As respostas aprendidas ficam salvas em `data/aiko_dados.json`. Esse arquivo é carregado toda vez que o programa inicia, então a Aiko mantém memória entre sessões.

```json
{
  "respostas": {
    "qual meu filme favorito?": "Interestelar"
  }
}
```

---

## 🛠️ Arquitetura

| Camada | Responsabilidade |
|---|---|
| `core/` | Lógica central: estado, chat, comandos e UI |
| `services/` | Serviços de suporte: emoções, I/O, storage, aprendizado |
| `decorators/` | Decoradores reutilizáveis |
| `data/` | Persistência em JSON |

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

1. Faça um fork do repositório
2. Crie uma branch para sua feature: `git checkout -b minha-feature`
3. Commit suas mudanças: `git commit -m 'feat: minha feature'`
4. Push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📄 Licença

Este projeto não possui licença definida ainda. Entre em contato com o autor para mais informações.

---

<div align="center">
  Feito com 💗 por <a href="https://github.com/JpStar06">JpStar06</a>
</div>

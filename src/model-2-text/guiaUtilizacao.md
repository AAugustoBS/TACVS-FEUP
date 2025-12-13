# BESSER Web UI Generator

Template-Based Model-to-Text Generator usando **BESSER Framework + Jinja2** para transformar modelos GUI em aplicações web (HTML+CSS+Vanilla JavaScript).

## 🚀 Quick Start

### 1. Instalação de Dependências

```bash
pip install jinja2>=3.0.0
```

### 2. Criar seu Modelo GUI

Crie um arquivo Python (ex: `meu_app.py`) com o modelo da sua aplicação:

```python
from gui_model import GUIModel, Module, Screen

# Criar modelo
gui = GUIModel(
    name="MeuApp",
    package="com.example.app",
    versionCode="1",
    versionName="1.0",
    description="Minha aplicação web gerada",
    screenCompatibility=True,
    modules=set()
)

# Criar módulo
modulo = Module(name="Principal", screens=set())
gui.modules.add(modulo)

# Criar telas
tela_principal = Screen(
    name="HomeScreen",
    x_dpi="xdpi",
    y_dpi="ydpi",
    screen_size="Medium",
    view_elements=set(),
    is_main_page=True
)
modulo.screens.add(tela_principal)

tela_login = Screen(
    name="LoginScreen",
    x_dpi="xdpi",
    y_dpi="ydpi",
    screen_size="Medium",
    view_elements=set(),
    is_main_page=False
)
modulo.screens.add(tela_login)
```

### 3. Gerar a Aplicação Web

```bash
python3 generate_app.py meu_app.py ./meu_app_web
```

Isso criará a pasta `meu_app_web/` com a aplicação completa.

### 4. Executar o Servidor

```bash
cd meu_app_web
python3 -m http.server 8000
```

Abra seu navegador em: **http://localhost:8000**

---

## 📁 Estrutura do Projeto

```
model-2-text/
├── besser_web_ui_generator.py    # Generator principal
├── gui_model.py                  # Classes do modelo GUI
├── generate_from_besser_gui.py   # Exemplo de uso
├── templates/                    # Templates Jinja2
│   ├── index.html.j2            # Template HTML principal
│   ├── app.js.j2                # Template JavaScript da app
│   ├── router.js.j2             # Template do router
│   ├── components.js.j2         # Template de componentes
│   ├── api.js.j2                # Template do serviço de API
│   ├── page.js.j2               # Template das páginas
│   ├── styles.css.j2            # Template CSS global
│   ├── components.css.j2        # Template CSS de componentes
│   └── README.md.j2             # Template de documentação
└── output_besser/               # Aplicação gerada (exemplo)
```

---

## 🎯 Exemplo Completo

### 1. Criar `community_app.py`

```python
from gui_model import GUIModel, Module, Screen

def create_gui_model():
    gui = GUIModel(
        name="CommunityPlatform",
        package="com.example.community",
        versionCode="1",
        versionName="1.0",
        description="Plataforma comunitária de marketplace",
        screenCompatibility=True,
        modules=set()
    )

    # Módulo principal
    main_module = Module(name="MainModule", screens=set())
    gui.modules.add(main_module)

    # Tela de lista de itens
    items_list = Screen(
        name="ItemsListScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=True
    )
    main_module.screens.add(items_list)

    # Tela de login
    login = Screen(
        name="LoginScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(login)

    # Tela de detalhes do item
    details = Screen(
        name="ItemDetailsScreen",
        x_dpi="xdpi",
        y_dpi="ydpi",
        screen_size="Medium",
        view_elements=set(),
        is_main_page=False
    )
    main_module.screens.add(details)

    return gui

if __name__ == "__main__":
    model = create_gui_model()
```

### 2. Gerar a aplicação

```bash
python3 generate_app.py community_app.py ./my_community_app
```

### 3. Executar

```bash
cd my_community_app
python3 -m http.server 8000
# Abra http://localhost:8000
```

---

## 📝 Referência da API GUI Model

### Classe `GUIModel`

```python
GUIModel(
    name: str,              # Nome da aplicação
    package: str,           # Pacote/namespace
    versionCode: str,       # Código de versão
    versionName: str,       # Nome da versão
    description: str = "",  # Descrição
    screenCompatibility: bool = True,
    modules: Set[Module] = set()
)
```

### Classe `Module`

```python
Module(
    name: str,
    screens: Set[Screen] = set()
)
```

### Classe `Screen`

```python
Screen(
    name: str,              # Nome único da tela
    x_dpi: str = "xdpi",
    y_dpi: str = "ydpi",
    screen_size: str = "Medium",
    view_elements: Set = set(),
    is_main_page: bool = False  # True para tela inicial
)
```

---

## 🛠️ Usando o Generator Programaticamente

```python
from gui_model import GUIModel, Module, Screen
from besser_web_ui_generator import WebUIGenerator

# Criar seu modelo
gui = GUIModel(...)

# Criar generator
generator = WebUIGenerator(model=gui, output_dir="./meu_app")

# Gerar aplicação
generator.generate()
```

---

## 📦 Estrutura Gerada

Cada aplicação gerada terá:

```
meu_app/
├── index.html              # Página principal
├── css/
│   ├── styles.css         # Estilos globais
│   └── components.css     # Estilos de componentes
├── js/
│   ├── app.js             # Lógica da aplicação
│   ├── router.js          # Roteador SPA
│   ├── components.js      # Registro de componentes
│   ├── api.js             # Serviço de API
│   └── pages/             # Páginas específicas
│       ├── itemslistscreen.js
│       ├── loginscreen.js
│       └── itemdetailsscreen.js
├── README.md              # Documentação da app gerada
└── .gitignore
```

---

## 🎨 Personalização

### Mudar Cores

Edite `css/styles.css`:

```css
:root {
    --primary-color: #2196F3;      /* Azul */
    --secondary-color: #FFC107;    /* Amarelo */
}
```

### Adicionar Lógica de Páginas

Edite arquivos em `js/pages/`:

```javascript
export class MyScreenPage {
    constructor(params = {}) {
        this.params = params;
    }

    async init() {
        // Sua lógica aqui
    }

    render() {
        return `<div>Seu conteúdo</div>`;
    }
}
```

---

## 🐛 Troubleshooting

### "Page Not Found" ao abrir

- Certifique-se de ter definido `is_main_page=True` em pelo menos uma tela
- O router automaticamente carrega a primeira tela com `is_main_page=True`

### Arquivos CSS/JS não carregam (404)

- Certifique-se de que o servidor está rodando no diretorio correta
- Use: `python3 -m http.server 8000` dentro da diretorio da aplicação gerada

### ecrãs não aparecem

- Verifique se o nome da tela não tem caracteres especiais
- Use nomes como: `HomeScreen`, `LoginScreen`, `DetailScreen`

---

## 📚 Exemplos Adicionais

Ver `generate_from_besser_gui.py` para um exemplo completo.


## ✨ Features

- ✅ Gera HTML5 semântico
- ✅ CSS3 responsivo com custom properties
- ✅ Vanilla JavaScript (sem dependências externas)
- ✅ Roteador SPA client-side
- ✅ Templates Jinja2 customizáveis
- ✅ Sem necessidade de build tools


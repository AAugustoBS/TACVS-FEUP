# Web UI Generator com BESSER - Resumo das Alterações

## Arquivos Criados

### 1. `besser_web_ui_generator.py`
Generator principal que:
- Estende `besser.generators.GeneratorInterface` (oficial BESSER)
- Aceita modelo BESSER `GUIModel` como entrada
- Gera HTML, CSS e JavaScript com Jinja2
- Inclui fallback caso BESSER não esteja instalado

**Principais métodos:**
- `generate()`: Orquestra a geração completa
- `_generate_html()`: Cria index.html
- `_generate_css()`: Cria arquivos CSS (styles.css, components.css)
- `_generate_javascript()`: Cria arquivos JS (app.js, router.js, components.js, api.js, pages)
- `_generate_assets()`: Cria README.md e .gitignore

### 2. `generate_from_besser_gui.py`
Script de demonstração que:
- Cria um modelo BESSER GUIModel programaticamente
- Define módulos e telas (BlankScreen, ItemListScreen, LoginScreen, etc.)
- Chama o WebUIGenerator para gerar a aplicação web
- Pode ser executado diretamente: `python generate_from_besser_gui.py`

## Arquivos Modificados

### 1. `requirements.txt`
Atualizado para:
```
jinja2>=3.0.0

# BESSER framework (install from GitHub)
# pip install git+https://github.com/BESSER-PEARL/BESSER.git
```

### 2. `README.md`
Atualizado com:
- Explicação de uso com BESSER oficial
- Dois exemplos: (1) Modelo BESSER GUIModel, (2) Modelo XML/XMI legado
- Instruções de uso do novo script `generate_from_besser_gui.py`

## Arquivos Antigos (Ainda Disponíveis)

- `web_ui_generator.py`: Versão anterior com classes BESSER-inspired locais
- `xml_to_buml.py`: Conversor XML → BESSER B-UML (se precisar usar modelo XMI)
- `generate.py`: Script CLI original para modelos XML/XMI

## Como Usar

### Opção 1: Com Modelo BESSER GUIModel (Recomendado)

```bash
python generate_from_besser_gui.py
```

Isso criará a aplicação web em `./output_besser/`

### Opção 2: Criar Seu Próprio Modelo

```python
from besser.BUML.metamodel.gui import GUIModel, Module, Screen
from besser_web_ui_generator import WebUIGenerator

# Criar modelo
gui = GUIModel(
    name="MeuApp",
    package="com.example.app",
    versionCode="1",
    versionName="1.0",
    modules=set()
)

# Adicionar módulos e telas
modulo = Module(name="Principal", screens=set())
tela = Screen(name="Inicial", x_dpi="xdpi", y_dpi="ydpi", screen_size="Medium", view_elements=set(), is_main_page=True)
modulo.screens.add(tela)
gui.modules.add(modulo)

# Gerar
generator = WebUIGenerator(model=gui, output_dir="./meu_app")
generator.generate()
```

## Instalação de Dependências

```bash
# 1. Instalar Jinja2
pip install jinja2>=3.0.0

# 2. Instalar BESSER framework do GitHub
pip install git+https://github.com/BESSER-PEARL/BESSER.git
```

## Estrutura Gerada

```
output_besser/
├── index.html          # Arquivo HTML principal
├── css/
│   ├── styles.css      # Estilos globais
│   └── components.css  # Estilos de componentes
├── js/
│   ├── app.js          # Aplicação principal
│   ├── router.js       # Roteador
│   ├── components.js   # Componentes reutilizáveis
│   ├── api.js          # Serviço de API
│   └── pages/          # Páginas específicas
├── README.md           # Documentação
└── .gitignore          # Configuração Git
```

## Notas Importantes

1. **BESSER é obrigatório**: O novo generator usa a versão oficial do BESSER framework
2. **Compatibilidade**: Requer Python 3.7+ (para tipos e dataclasses do BESSER)
3. **Templates**: Os templates Jinja2 em `templates/` continuam sendo usados
4. **Modelo GUI BESSER**: Use a classe oficial `GUIModel`, `Module`, `Screen` do BESSER

## Próximos Passos

1. Instalar BESSER: `pip install git+https://github.com/BESSER-PEARL/BESSER.git`
2. Executar: `python generate_from_besser_gui.py`
3. Visualizar: `cd output_besser && python -m http.server 8000`
4. Abrir navegador: `http://localhost:8000`

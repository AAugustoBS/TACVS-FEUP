"""
Generate Web UI from a user-provided .py model file.
The .py must define either:
 - variable: gui (instance of GUIModel), or
 - function: create_model() returning GUIModel
"""

import os
import sys

from besser_web_ui_generator import WebUIGenerator
from gui_model import GUIModel


def _load_module_py2(py_path, module_name):
    # Fallback loader for Python 2
    import imp
    with open(py_path, 'r') as f:
        return imp.load_source(module_name, py_path, f)


def _load_module(py_path):
    # Prefer Python 3 importlib.util when available
    try:
        import importlib.util
        module_name = os.path.splitext(os.path.basename(py_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, py_path)
        module = importlib.util.module_from_spec(spec)
        assert spec and spec.loader
        spec.loader.exec_module(module)
        return module
    except Exception:
        # Fallback to Python 2 loader
        module_name = os.path.splitext(os.path.basename(py_path))[0]
        return _load_module_py2(py_path, module_name)


def load_model(py_path):
    if not os.path.exists(py_path):
        raise IOError("Model file not found: " + py_path)

    module = _load_module(py_path)

    # 1) Direct variable 'gui'
    if hasattr(module, 'gui') and isinstance(module.gui, GUIModel):
        return module.gui
    # 2) Factory 'create_model()'
    if hasattr(module, 'create_model'):
        model = module.create_model()
        if isinstance(model, GUIModel):
            return model
        raise TypeError("create_model() did not return GUIModel")
    # 3) Common sample factory 'create_sample_gui_model()' (do not modify source file)
    if hasattr(module, 'create_sample_gui_model'):
        model = module.create_sample_gui_model()
        if isinstance(model, GUIModel):
            return model
        raise TypeError("create_sample_gui_model() did not return GUIModel")
    # 4) Alternate factory name 'create_gui_model()'
    if hasattr(module, 'create_gui_model'):
        model = module.create_gui_model()
        if isinstance(model, GUIModel):
            return model
        raise TypeError("create_gui_model() did not return GUIModel")

    raise AttributeError("Model file must define 'gui' or one of: 'create_model()', 'create_sample_gui_model()', 'create_gui_model()' returning GUIModel")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 generate_app.py <path_to_model.py> [output_dir]")
        sys.exit(1)

    model_py = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output_besser"

    gui_model = load_model(model_py)

    # Defaults for features if missing
    gui_model.features = {
        'show_mbway': gui_model.features.get('show_mbway', True),
        'show_multibanco': gui_model.features.get('show_multibanco', True),
        'show_logout': gui_model.features.get('show_logout', True),
        'show_profile': gui_model.features.get('show_profile', True)
    }

    generator = WebUIGenerator(model=gui_model, output_dir=output_dir)
    generator.generate()
    print("Website ready at: " + output_dir)


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
BESSER Web UI Generator - CLI Script
Permite gerar aplicações web a partir de qualquer arquivo Python com modelo GUI
"""

import os
import sys
import importlib.util

from besser_web_ui_generator import WebUIGenerator


def print_banner():
    """Imprime banner do gerador"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║           BESSER Web UI Generator                         ║
    ║           Model-to-Text com Jinja2 Templates              ║
    ║                                                           ║
    ║           Gera HTML+CSS+Vanilla JS                        ║
    ║           a partir de Modelos GUI Python                  ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)


def print_usage():
    """Imprime instruções de uso"""
    print("""
    Uso:
        python3 generate_app.py <arquivo_modelo.py> [diretório_saída]
    
    Argumentos:
        arquivo_modelo.py      Caminho para arquivo Python com modelo GUI (obrigatório)
        diretório_saída        Diretório para gerar código (padrão: ./output)
    
    Exemplos:
        python3 generate_app.py meu_app.py
        python3 generate_app.py meu_app.py ./generated_app
        python3 generate_app.py ../models/app.py ./output/my_app
    
    O arquivo Python deve conter:
        - Uma variável 'gui' do tipo GUIModel, OU
        - Uma função 'create_gui_model()' que retorna GUIModel
    
    Exemplo de arquivo_modelo.py:
        
        from gui_model import GUIModel, Module, Screen
        
        gui = GUIModel(
            name="MeuApp",
            package="com.example.app",
            versionCode="1",
            versionName="1.0",
            modules=set()
        )
        
        modulo = Module(name="Principal", screens=set())
        gui.modules.add(modulo)
        
        tela = Screen(name="HomeScreen", is_main_page=True)
        modulo.screens.add(tela)
    """)


def load_gui_model(model_path):
    """Carrega o modelo GUI do arquivo Python"""
    
    if not os.path.exists(model_path):
        print("Erro: Arquivo não encontrado: " + model_path)
        return None
    
    if not model_path.endswith('.py'):
        print("Erro: Arquivo deve ter extensão .py")
        return None
    
    try:
        # Carregar módulo do arquivo
        spec = importlib.util.spec_from_file_location("gui_model_module", model_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Tentar encontrar a variável 'gui'
        if hasattr(module, 'gui'):
            gui = module.gui
            print("✓ Modelo GUI carregado da variável 'gui'")
            return gui
        
        # Tentar encontrar a função 'create_gui_model()'
        if hasattr(module, 'create_gui_model'):
            create_func = module.create_gui_model
            gui = create_func()
            print("✓ Modelo GUI criado pela função 'create_gui_model()'")
            return gui
        
        print("Erro: Arquivo deve conter 'gui' ou 'create_gui_model()'")
        return None
        
    except Exception as e:
        print("Erro ao carregar arquivo: " + str(e))
        import traceback
        traceback.print_exc()
        return None


def main():
    """Função principal"""
    print_banner()
    
    # Validar argumentos
    if len(sys.argv) < 2:
        print("Erro: Arquivo modelo é obrigatório\n")
        print_usage()
        sys.exit(1)
    
    if sys.argv[1] in ['-h', '--help', 'help']:
        print_usage()
        sys.exit(0)
    
    model_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./output"
    
    # Resolver caminhos absolutos
    model_path = os.path.abspath(model_path)
    output_dir = os.path.abspath(output_dir)
    
    # Validar arquivo
    if not os.path.exists(model_path):
        print("Erro: Arquivo modelo não encontrado: " + model_path)
        sys.exit(1)
    
    print("\nCarregando modelo...")
    gui_model = load_gui_model(model_path)
    
    if gui_model is None:
        print("\nErro ao carregar modelo GUI")
        sys.exit(1)
    
    # Validar modelo
    if not hasattr(gui_model, 'name'):
        print("Erro: Modelo deve ter atributo 'name'")
        sys.exit(1)
    
    # Exibir informações
    print("\nInformações da Aplicação:")
    print("   Nome:           " + gui_model.name)
    print("   Versão:         " + gui_model.versionName)
    print("   Diretório saída: " + output_dir)
    
    # Contar telas
    telas_total = 0
    for modulo in gui_model.modules:
        telas_total += len(modulo.screens)
    print("   Telas:          " + str(telas_total))
    print()
    
    # Confirmar geração
    try:
        resposta = input("Iniciar geração? (s/n): ")
    except (EOFError, KeyboardInterrupt):
        print("\nGeração cancelada")
        sys.exit(0)
    
    if resposta.lower() not in ['s', 'sim', 'y', 'yes']:
        print("Geração cancelada")
        sys.exit(0)
    
    print()
    
    try:
        # Criar gerador
        print("Criando gerador...")
        generator = WebUIGenerator(model=gui_model, output_dir=output_dir)
        
        # Gerar
        print("Gerando aplicação web...\n")
        generator.generate()
        
        # Sucesso
        print("\n" + "=" * 60)
        print("Geração concluída com sucesso!")
        print("=" * 60)
        print()
        print("Arquivos gerados em: " + output_dir)
        print()
        print("Próximos passos:")
        print("   1. cd " + output_dir)
        print("   2. python3 -m http.server 8000")
        print("   3. Abra http://localhost:8000 no navegador")
        print()
        
    except Exception as e:
        print()
        print("=" * 60)
        print("Erro na geração!")
        print("=" * 60)
        print()
        print("Erro: " + str(e))
        print()
        
        import traceback
        print("Rastreamento:")
        traceback.print_exc()
        
        sys.exit(1)


if __name__ == "__main__":
    main()

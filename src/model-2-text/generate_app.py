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

import pandas as pd
import os

def carregar_dados(nome_arquivo):
    try:
        # Pega na pasta onde o script está
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_completo = os.path.join(diretorio_atual, nome_arquivo)
        
        print("\n--- INÍCIO DO DIAGNÓSTICO ---")
        print(f"👉 A tentar abrir o arquivo no caminho exato: {caminho_completo}")
        
        # Verifica se o ficheiro realmente existe nesse caminho
        if not os.path.exists(caminho_completo):
            print("❌ ERRO: O arquivo NÃO existe neste caminho!")
        else:
            print("✅ SUCESSO: O arquivo foi encontrado na pasta!")
            
        # Lê o CSV
        df = pd.read_csv(caminho_completo, sep=';', encoding='latin1')
        print("✅ SUCESSO: O Pandas conseguiu ler o arquivo!")
        print("--- FIM DO DIAGNÓSTICO ---\n")
        
        return df
    except Exception as e:
        print(f"❌ Erro ao carregar: O tipo de erro é '{type(e).__name__}' e a mensagem é: {e}")
        print("--- FIM DO DIAGNÓSTICO ---\n")
        return None

def obter_estatisticas_html(df):
    if df is not None:
        # 1. Dicionário com a tradução dos termos do Pandas para Português
        traducao_linhas = {
            'count': 'Contagem',
            'mean': 'Média',
            'std': 'Desvio Padrão',
            'min': 'Valor Mínimo',
            '25%': '1º Quartil (25%)',
            '50%': 'Mediana (50%)',
            '75%': '3º Quartil (75%)',
            'max': 'Valor Máximo'
        }
        
        # 2. Gera as estatísticas, traduz as linhas e arredonda para 2 casas decimais
        estatisticas = df.describe().rename(index=traducao_linhas).round(2)
        
        # 3. Converte para HTML
        return estatisticas.to_html(classes='table table-striped')
    
    return "<p>Erro ao processar dados.</p>"
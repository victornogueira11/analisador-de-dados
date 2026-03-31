# 📊 Analisador de Dados com Flask & Pandas

Este é um projeto de aplicação web Full-Stack que realiza a leitura de dados estruturados em CSV, processa estatísticas descritivas utilizando a biblioteca Pandas e exibe os resultados em uma interface amigável via Flask.

## 🚀 Funcionalidades

* **Leitura de Dados:** Processamento de arquivos CSV com suporte a codificação `latin1` e separadores `;`.
* **Análise Estatística:** Cálculo automático de média, mediana, desvio padrão, valores máximos e mínimos e quartis.
* **Interface Web:** Exibição dos dados através de templates HTML dinâmicos.
* **Diagnóstico de Logs:** Sistema de logs no terminal para verificar a integridade do caminho dos arquivos e sucesso da leitura.

## 🛠️ Tecnologias Utilizadas

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## 📁 Estrutura do Projeto

* `main.py`: O "coração" da aplicação. Gerencia as rotas do Flask e inicia o servidor.
* `analise.py`: Módulo responsável pela lógica de dados. Contém as funções de carregamento do CSV e a lógica de tradução das estatísticas para Português.
* `templates/index.html`: Interface visual que utiliza o motor Jinja2 para renderizar as tabelas de dados.
* `dados.csv`: Base de dados de exemplo contendo informações de nomes, idades e salários.

## 📸 Demonstração

![Screenshot do Projeto](link-da-sua-imagem)
![Screenshot do Projeto](link-da-sua-imagem)

## 🔧 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/victornogueira11/analisador-de-dados.git

2. **Instale as dependências:**
   ```bash
   pip install flask pandas

3. **Inicie o servidor:**
   ```bash
   python main.py

4. **Acesse o navegador:**
   ```bash
   http://127.0.0.1:5000 

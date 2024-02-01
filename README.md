

# AGIO: Gerenciador de Empréstimos 🤑

O Agio é um projeto desenvolvido em Python e Django, idealizado para facilitar a gestão de empréstimos pessoais ou empresariais. Ele automatiza a criação de parcelas, incluindo datas de vencimento, quantidade de parcelas, frequência com que vencem, e cálculo de juros sobre o valor total do empréstimo. Com recursos para filtrar parcelas por datas, o AgioDjango torna mais simples o acompanhamento do fluxo de caixa futuro, mostrando o quanto de dinheiro tem para entrar em determinadas datas.

## Começando 🚀

Siga estas instruções para configurar o Agio em sua máquina local para desenvolvimento e testes.

### Pré-requisitos 📋

Certifique-se de ter instalado em sua máquina:

- Git
- Python

### Instalação 🔧

Clone o repositório

```bash
git clone https://github.com/Andrersm/AgioDjango.git
```

Crie um ambiente virtual (recomendado)

```bash
python -m venv venv
# ou, para sistemas Unix/Mac:
python3 -m venv venv
```

Ative o ambiente virtual

No Windows:

```bash
.\venv\Scripts\activate
```

No Unix ou MacOS:

```bash
source venv/bin/activate
```

Instale as dependências

```bash
pip install -r requirements.txt
```


Execute o servidor de desenvolvimento

```bash
python manage.py runserver
# ou, para sistemas Unix/Mac:
python3 manage.py runserver
```

Acesse o aplicativo em http://127.0.0.1:8000/ no seu navegador.

## Funcionalidades 📌

- **Criação Automática de Parcelas**: Basta informar a quantidade de parcelas, a frequência de vencimento e a taxa de juros.
- **Filtragem de Parcelas por Data**: Facilidade para visualizar o fluxo de caixa futuro, filtrando parcelas que vencem em determinadas datas.

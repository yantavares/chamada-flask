# Chamada - Flask

Este é um simples aplicativo Flask que permite armazenar IDs de estudantes em um arquivo CSV e exportar esse arquivo. Ele inclui uma página inicial protegida por senha para controlar o acesso aos dados.

## Instalação

Certifique-se de ter o Python3 instalado em sua máquina.
Clone este repositório: git clone https://github.com/seu-usuario/flask-armazenamento-ids-estudantes.git
Instale as dependências do projeto: pip install -r requirements.txt

## Execução

Para iniciar o aplicativo Flask, execute o seguinte comando no diretório do projeto:

```py
python app.py
```

O aplicativo será executado em http://localhost:5000/.

## Uso

Para acessar a página inicial, você precisará inserir uma senha. A senha padrão é mysecretkey, mas você pode alterá-la editando a variável app.config['SECRET_KEY'] no arquivo app.py.

Na página inicial, você pode adicionar novos IDs de estudantes usando o formulário e o botão "Adicionar". Os IDs de estudantes são armazenados em um arquivo CSV chamado students.csv.

Para exportar os IDs de estudantes armazenados como um arquivo CSV, clique no botão "Exportar CSV". Isso baixará o arquivo students.csv.

## Créditos

Este projeto foi criado por yantavares no Github.

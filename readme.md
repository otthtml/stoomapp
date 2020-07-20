#stoomapp

Pequeno projeto usando Docker, Testes e Django.

#Como iniciar o projeto?
O jeito mais fácil de rodar a aplicação é rodando o comando "docker-compose up", que realizará todas as instalações necessárias.
Para rodar o comando docker-compose, é necessário estar no diretório "stoomapp", instalar o Docker e o Docker Compose (que já vem com o Docker, caso você esteja usando Windows).

Caso não seja possível instalar o Docker, pode-se seguir os passos:
1. Navegar até o diretório "django" com o comando "cd django";
2. Criar um ambiente com o comando "python -m venv ambiente";
3. Ativar o ambiente com o comando apropriado. No cmd, basta "ambiente\Scripts\activate". No bash, "source ambiente/Scripts/activate";
4. Instalar as dependências com o comando "pip install -r requirements.txt";
5. Navegar até o diretório "projeto" com o comando "cd projeto";
5. Executar o django com "python manage.py runserver"

Após a inicialização da aplicação, basta acessar no navegador de preferência a URL http://127.0.0.1:8000/endereco/

#Como parar?
1. Ctrl+C no terminal para parar a aplicação;
2. "docker-compose down" se estiver usando o Docker Compose

#Executando testes?
Com o ambiente corretamente ativado ou dentro do container Docker, executar, no diretório "stoomapp/django/projeto" o comando "python manage.py test".
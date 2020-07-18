#stoomapp

Pequeno projeto usando Docker, TDD e Django.

#Como iniciar o projeto?
O jeito mais fácil de rodar a aplicação é rodando o comando "docker-compose up", que realizará todas as instalações necessárias.
Para rodar o comando docker-compose, é necessário instalar o Docker e o Docker Compose (que já vem com o Docker, caso você esteja usando Windows).

Caso não seja possível instalar o Docker, pode-se seguir os passos:
1. Navegar até a pasta "django" com o comando "cd django";
2. Criar um ambiente com o comando "python -m venv ambiente";
3. Ativar o ambiente com o comando apropriado. No cmd, basta "ambiente\Scripts\activate". No bash, "source ambiente/Scripts/activate";
4. Instalar as dependências com o comando "pip install -r requirements.txt";
5. Executar o django com "python manage.py runserver"

#Como parar o projeto?
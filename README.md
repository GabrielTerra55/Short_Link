# Short_Link
<p>
Neste repositorio foi feito uma aplicação Monolitica que consegue gerar links encurtadores para url de sites. Foi utilizado no desenvolvimento o framework Django, as bibliotecas requests e validators e alguns modulos nativos do python.
</p>
<p>
 O intuito desse projeto é desenvolver bons fundamentos em algoritimos, boa pratica de programação (metodos e atributos e organização dos folders), reforçar os fundamentos do Django e como o framework funciona.
</p>
<h2>Instalação</h2>
<p>para fazer a instalação da aplicação você deve ter o python 3 instalado na sua maquin, além de ser recomendável a criação de um ambiente virtual de desenvolvimento 'venv'</p>
Passo 1- instale as dependencias necessarias da aplicação.<br>
 SO Windows
	
```
pip install requirements.txt       
```
 SO Linux

```
pip install -r requirements.txt
```
Após essa configurações é necessario fazer as migrações, com os comandos:

```
python manage.py makemigrations
python manage.py migrate
```
Após essa configurações já sera possivel rodar a aplicação utilizando-o

```
python manage.py runserver
```
<h2>Uso</h2>
<p>
  Na pagina inicial sera mostrada um caixa onde você podera colocar o link que deseja. Ao clickar em 'submit', se o link for valido, você sera redirecionado para uma
  nova pagina contendo o link encurtado da requiseção.
</p>
<p>
  Você pode voltar a pagina principal clickando no titulo!
</p>

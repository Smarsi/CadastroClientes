# Teste Técnico Igma

Uma API de cadastro de clientes.

## 🚀 Começando

Siga as instruções de instalação para rodar o projeto em sua máquina local.
Execute os testes automatizados seguindo o passo a passo aqui incluso.
Vale ressaltar que dentro de cada diretório (relevante) do projeto existe um README explicando o que o código faz.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

* <b>Git</b> instalado
* <b>Python 3.x</b> instalado
* <b>Pip</b> na última versão instalado
* Ser capaz de executar comandos por linha de comando (cmd ou power shell por exemplo).


### 🔧 Instalação

Aqui será considerado a instalação e execução do projeto por meio do sistema operacional <span style="color: blue; font-weight: 800">Windows</span>. Caso necessite executar este projeto em outro sistema operacional utilize o passo a passo trocando as variáveis do windows pelas de seu sistema operacional.

---

<b>Passo 1</b>- Primeiramente será necessário baixar ou clonar este repositório em sua máquina local.

Neste repositório do github procure pelo botão verde com o texto "<> code" e logo em seguida clique e copie a URL exibida no drop-down que se abriu.

![Clone_Repo](https://user-images.githubusercontent.com/38111460/219534943-1150ce06-d64c-44fe-8d2d-e4a14ff7c14b.PNG)

Navegue através de sua interface de comandos até a pasta onde deseja clonar o repositório e digite o seguinte comando substituindo < link > pela url copiada aqui no github:

```
git clone < link >
```

Em seguida acesse a página onde clonou o projeto.

```
cd <caminho da sua pasta>
```
---

<b>Passo 2</b>- Agora será preciso instalar os pacotes necessários para rodar nosso projeto, para isso, iremos utilizar um máquina virtual do python e evitar a instalação desses recursos em seu python original.

Já dentro da pasta do projeto digite o seguinte comando:

```
python -m venv venv
```
Isso fará com que o python crie um máquina virtual chamada 'venv'. Repare que logo após a execução uma nova pasta chamada venv foi criada na raiz do projeto.

Agora será necessário ativar nossa venv, para tal, execute os comandos abaixo:

```
cd venv/scripts

activate
```

Uma vez que a venv é ativada repare que ao lado do caminho exibido na interface de comandos temos uma tag (venv)

![venv_ativada](https://user-images.githubusercontent.com/38111460/219537412-c0592852-6452-49ed-92d1-9f2f7fcde49f.PNG)

Agora iremos instalar os pacotes necessários. Para isso, rode o comando abaixo:
(Certifique-se de ter voltado para a raiz do projeto antes de executar o comando)

```
pip install -r requirements.txt
```

---

<b>Passo 3</b>- Crie um banco de dados e configure as credenciais e portas através do arquivo <b>system/settings.py</b>
No projeto atual escolhi utilizar o MySQL como banco de dados, porém, caso prefira poderá alterar por outro (para isso consulte a documentação do DJango).

![image](https://user-images.githubusercontent.com/38111460/220839740-20a2407b-3573-40c7-830e-d5cdf249ce81.png)

Basta alterar os campos 'Name', 'User', 'Password', 'Host' e 'Port' para as informações do seu banco de dados.

---

<b>Passo 4</b>- Feitotudo isso já devemos ser capazes de executar o projeto DJango em sua máquina. Para isso siga os passos a seguir.

<br>

Para iniciarmos o projeto o DJango exige que criemos nossas tabelas do banco de dados. Para isso siga o comando a seguir:

```
python manage.py makemigrations
```

Esse comando fará com que apareçam no diretório de nosso projeto uma pasta chamada migrations (é uma pasta de controle do django).

Agora iremos criar efetivamente as tabelas:

```
python manage.py migrate
```

Você deverá ver uma mensagem como esta:

![image](https://user-images.githubusercontent.com/38111460/220841113-374d12e0-e7d7-45ed-a747-135226614dad.png)

<br>
Agora basta rodar o comando abaixo para iniciar o servidor local do projeto e os endpoints já estarão acessíveis:

```
python manage.py runserver
```

Neste momento já temos o projeto funcional rodando.


---

## ⚙️ Usando o sitema

#### Breve explicação:

<p>A API foi criada seguindo os padrões REST e usa Json como padrão para consulta e cadastro de informações. Todos os módulos criados foram testados e os códigos de testes unitários estão disponíveis dentro do diretório <b>core/tests</b> (olhar commits do projeto para mais detalhes).</p>
<p>O sistema foi criado em cima dos requisitos passados por e-mail, e conta com 3 endpoints que serão explicados abaixo:</p>

<br>

* <b>/new-custumer/</b> 

Este endpoint permite a criação de um novo cliente no sistema. 
O formato padrão usado para o cadastro é JSON.

Abaixo um exempo de formato JSON aceito pelo endpoint:

```
{
    "nome": "Augustinho Carrara",
    "cpf": "771.757.960-05",
    "nascimento": "1986-11-07"
}
``` 

<br>
<br>

* <b>/consult-custumer/</b>  

Este endpoint serve para consultar um cliente em específico que já esteja cadastrado no sistema.
É necessário passar um parâmetro para realizar a pesquisa, os tipos de parâmetros aceitos são Nome, CPF e ID do cliente e todos são passados diretamente na URL.

<br>
<b>Exemplos</b>
<br>

Pesquisando por CPF:

```
http://localhost:8000/consult-custumer?cpf=14128525600
```

Pesquisando por Nome:

```
http://localhost:8000/consult-custumer?nome=Augustinho%Carrara
```
Se o nome pesquisado contiver espaços utilize o '%' (navegadores já fazem isso automaticamente e programas de teste como o postman aceitam espaços sem problemas).

Pesquisando por ID:

```
http://localhost:8000/consult-custumer?id=58
```
<br>
<br>

* <b>/consult-all-custumers/</b>

Este endpoint faz um consulta de todos os clientes cadastrados usando paginação. Por padrão as consultas retornam de 5 em 5 cliente por vez, porém é possível limitar em menos.

Pesquisando com paginação normal:

```
http://localhost:8000/consult-all-custumers
```

<br>

Limitando a busca em 2 clientes por request:

```
http://localhost:8000/consult-all-custumers?limit=2
```

Exemplo de retorno:

```
{
    "count": 21,
    "next": "http://localhost:8000/consult-all-custumers/?limit=5&offset=5",
    "previous": null,
    "results": [
        {
            "id": 41,
            "nome": "Michael Dias",
            "cpf": 29173301809,
            "nascimento": "1999-06-13"
        },
        {
            "id": 42,
            "nome": "Lucas Mendes",
            "cpf": 22303492874,
            "nascimento": "1993-12-01"
        },
        {
            "id": 43,
            "nome": "Silva Rocha",
            "cpf": 30316044822,
            "nascimento": "1954-02-19"
        },
        {
            "id": 44,
            "nome": "Inês Pereira",
            "cpf": 43350784801,
            "nascimento": "1985-07-23"
        },
        {
            "id": 45,
            "nome": "Isabella Moreira",
            "cpf": 68234315803,
            "nascimento": "2006-04-03"
        }
    ]
}
```




### 🔩 Analise os testes de ponta a ponta

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```

### ⌨️ E testes de estilo de codificação

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```

## 📦 Implantação

Adicione notas adicionais sobre como implantar isso em um sistema ativo

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - O framework web usado
* [Maven](https://maven.apache.org/) - Gerente de Dependência
* [ROME](https://rometools.github.io/rome/) - Usada para gerar RSS


---

## 📦 Implantação

Adicione notas adicionais sobre como implantar isso em um sistema ativo

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - O framework web usado
* [Maven](https://maven.apache.org/) - Gerente de Dependência
* [ROME](https://rometools.github.io/rome/) - Usada para gerar RSS

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊
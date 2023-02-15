# CadastroClientes
<b>Um repositório para um teste Técnico da empresa Igma.</b>


---

<h5>Tecnologias usadas neste projeto</h5>

- Python

- Django

- Django Rest Framework


---

<h5>Para iniciar o projeto em sua máquina siga os passos a seguir:</h5>

* 1º: Garanta que tem o python instalado em sua máquina com a última versão do pip (gerenciador de pacotes do python [equivalente ao npm do node])
<br>

* 2º: Clone ou baixe esse diretório em sua máquina local.
<br>

* 3º: Ao adentrar no repositório do projeto usando uma interface de código (CMD / PowerShell), execute o seguinte comando:
<br>

```
python -m venv venv
```
<p>Este comando cria uma máquina virtual do python para evitar de instalarmos os pacotes necessários no python original da sua máquina (boas práticas de desenvolvimento com python).</p>
<br>
<br>

* 4º: Vamos ativar nossa venv usando o seguintes comandos:
<br>
* Navegue até a pasta scripts da venv

    ```
    cd venv/scripts
    ```
<br>

* Agora execute o seguinte comando

    ```
    activate
    ```

* Em seguida basta usar o seguinte comando quantas vezes forem necessárias para voltar para raiz do projeto:

    ```
    cd..
    ```
<br>

* 5º: Agora é necessário instalar os pacotes necessários para usarmos o projeto. Para isso, embarcado no projeto temos um arquivo chamado "requirements.txt" que contém os pacotes e suas respectivas versões usadas durante o desenvolvimento.
Após garantir que está no mesmo nível do arquivo, rode o seguinte comando:

```
pip install -r requirements.txt
```
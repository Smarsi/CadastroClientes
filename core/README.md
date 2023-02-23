# APP Core

Entenda tudo de importante que está acontecendo por aqui!

<br>
<br>
<br>

## verificar_cpf.Py

Esse arquivo contém toda a lógica de cálculo e validação de CPF usada pela API.
Todo o código foi escrito do Zero por mim, apenas seguindo (como sugerido no e-mail) o tutorial do macoratti.net



---

## models.Py

Os models do DJango são usados para criar o banco de dados (eles basicamente definem quais tabelas, campos e formatos o banco de dados deve aceitar).
Neste projeto foi criado apenas um Model chamado Cliente, que é basicamente um retrato de como a tabela Clientes deveria ser.

![image](https://user-images.githubusercontent.com/38111460/220852747-d93a26b5-49df-4804-a3cd-0fc928ce3000.png)


Observe que os campos listados no modelo são os mesmos exibiso na consulta dentro do MySQL Workbench.

---

## views.py

Arquivo do DJango onde são montadas as Views e controllers da nossa API.
<b>Parte da lógica de validação de CPF se encontra aqui.</b>
Use este arquivo para verificar os Códigos HTTP e seus resultados e toda a lógica de funcionamento dos métodos GET e POST.

---

## tests/

Pacote Python criado para conter e organizar todos os testes criados para o projeto atual.

---


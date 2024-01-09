## [Simple Form](https://pypi.org/project/simple-form/)
- Pequena biblioteca para facilitar formulários em CLI.
- Clique [**aqui**](https://github.com/Hoyasumii/SimpleForm) para acessar o repositório.
---
## Instalação
- Você pode baixar pelo pip:
```
pip install simple-form
```
---
## Como usar?
- Em seu projeto, importe a biblioteca e crie um objeto: 
```python
# Importando a biblioteca
from simpleForm import Form

# Criando um objeto
myForm = Form("Título do meu formulário")
```
- Para adicionar elementos ao formulário, use o método `add`:
```python
# Adicionando um campo de texto
myForm.add(name={
    "type": str,
    "description": "Digite seu nome"
})
```
- Para executar o formulário, chame a instância do `objeto`:
```python
myForm()
```
- Para acessar os dados do formulário, use a propriedade `values`:
```python
print(myForm.values)
```
---
## Conhecendo a classe `Form`
- A classe `Form` possui alguns métodos que podem ser úteis e bastante versáteis. E são eles:
### 1. `add`
- Rece
---
## O que cada elemento a ser adicionado pode e precisa ter?
- Cada elemento a ser adicionado precisa ser um dicionário, e precisa ter os seguintes atributos:
### 1. `type`
- É o tipo de dado que o elemento vai receber. Pode ser `str`, `int`, `float`, `bool` ou `list`.
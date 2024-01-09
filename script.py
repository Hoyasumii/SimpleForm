from simpleForm import Form

x = Form("Teste", spacing=1)
x.add(name={
    "type": str,
    "description": "Nome",
    "default": "John Doe",
    "min": 3,
    "max": 10
}, happy={
    "type": bool,
    "description": "Feliz"
}, age={
    "type": int,
    "description": "Idade",
    "min": 1,
    "max": 100,
    "default": 18
}, action={
    "type": list,
    "description": "Escolha a ação",
    "options": [
        "Pular",
        "Correr",
        "Andar"
    ],
}, email={
    "type": str,
    "description": "Email",
    "default": "account@email.com",
    "validate": r"^[a-zA-Z0-9\._]{4,}@\w.{2,}\w{2,}$"
}, option={
    "type": dict,
    "description": "Opção",
    "options": {
        "Pular": "E pulou",
        "Correr": "E correu",
        "Andar": "E andou"
    }
}
)
x()
print(x.values)

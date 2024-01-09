from simpleForm import SimpleForm

x = SimpleForm("Teste", spacing=1)
x.add(name={
    "type": str,
    "description": "Nome",
    "default": "Alan"
})
x()
print(x.values)
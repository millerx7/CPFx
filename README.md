
# Gerador e Validador de CPF em Python 🧾🇧🇷

Este projeto consiste em dois scripts simples desenvolvidos em Python: um **gerador de CPF válido** e um **validador de CPF**. Ele pode ser usado para fins educacionais, testes de sistemas, ou demonstrações em aplicações que lidam com documentos brasileiros.

## 🛠 Funcionalidades

- ✅ Geração de números de CPF válidos com dígitos verificadores corretos
- 🔎 Verificação de validade de um CPF fornecido pelo usuário
- 🧼 Formatação automática no estilo `XXX.XXX.XXX-XX`

---

## 📂 Estrutura do Projeto

```
.
├── generate_cpf.py   # Script para gerar CPFs válidos
├── check_cpf.py      # Script para verificar a validade de um CPF
```

---

## 📌 Como usar

### ▶️ Gerador de CPF

Execute o script `generate_cpf.py`:

```bash
python generate_cpf.py
```

Você será perguntado se deseja gerar um novo CPF. Se responder `sim`, o programa irá:

- Gerar os 9 primeiros dígitos aleatórios
- Calcular corretamente os 2 dígitos verificadores
- Retornar o CPF formatado

**Exemplo de saída:**
```
Deseja gerar um novo CPF? (sim/não): sim
O CPF gerado foi: 123.456.789-09
```

---

### ✅ Validador de CPF

Execute o script `check_cpf.py`:

```bash
python check_cpf.py
```

Você deverá digitar um CPF com 11 dígitos (somente números). O programa então:

- Valida o formato (deve conter exatamente 11 dígitos)
- Calcula os dígitos verificadores esperados
- Compara com os dígitos fornecidos
- Exibe se o CPF é **válido** ou **inválido**

**Exemplo de uso:**
```
Digite o CPF que deseja verificar: 12345678909
O CPF 12345678909 é Válido
```

---

## ⚠️ Observações

- Este projeto tem fins **educacionais**. O uso de CPFs gerados fora de contexto legal pode ser crime.
- Os algoritmos seguem a regra oficial de cálculo de dígitos verificadores do CPF.

---

## 📄 Licença

Este projeto está sob a licença MIT. Sinta-se livre para estudar, modificar e usar em seus próprios projetos!

---

## 👨‍💻 Autor

**Guilherme Miller Nunes Costa**  
Aluno de Telemática - IFPB  
Contato: guilhermemiller.dev@gmail.com

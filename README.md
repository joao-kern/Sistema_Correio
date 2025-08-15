# Sistema_Correio

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

Um sistema de depósito e gerenciamento de correios desenvolvido em Python, aplicando **herança** e **orientação a objetos**.

---

## Visão Geral

O *Sistema_Correio* é um projeto que demonstra a aplicação de herança em Python para modelar um sistema de entrega de encomendas, com diferentes tipos como **Sedex**, **SedexPlus** e **PAC**. Útil como aprendizado e base para sistemas modulares de logística.

## Funcionalidades

- Modelagem orientada a objetos com classes base e classes especializadas.
- Simulação de métodos específicos (peso, tipo de envio, cálculo de prazos ou custos).
- Arquitetura escalável para suportar novos tipos de envio.

## Estrutura do Projeto

```
Sistema_Correio/
│── sistema/           
│    ├── modelos
│    │    ├── heranca_Encomenda.py
│    │    ├── heranca_Encomenda_Sedex.py
│    │    ├── heranca_Encomenda_SedexPlus.py
│    │    └── herenca_Encomenda_PAC.py
|    ├── metodos.py
|    └── sistema.py
│── .gitattributes     
│── .gitignore
│── LICENSE
└── main.py           
```

- **heranca_Encomenda.py** → Classe base do Correio e atributos comuns.
- **heranca_Encomenda_* .py** → Classes especializadas de envio.
- **metodos.py** → Funções auxiliares.
- **sistema.py** → Coordena o fluxo principal.
- **main.py** → Ponto de entrada da aplicação.

## 🛠 Requisitos

- Python **3.x**
- Nenhuma dependência externa.

---

## Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/joao-kern/Sistema_Correio.git
   ```

2. **Acesse o diretório**

  ```bash
  cd Sistema_Correio
  ```

3. **Execute o programa**
  ```bash
  python main.py
  ```

## Autor

Desenvolvido por João Kern – GitHub Profile

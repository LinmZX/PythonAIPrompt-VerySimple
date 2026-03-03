# PythonAIPrompt — Very Simple

---

## 🇧🇷 PT-BR  
Prompt simples de IA com Python

Este código contém imports de subclasses da biblioteca **LangChain** e do **dotenv**.

### Sub-bibliotecas do LangChain utilizadas:

- **ChatOpenAI** (de `langchain_openai`)  
  Utilizado para garantir a conexão com o modelo do ChatGPT.

- **PromptTemplate** (de `langchain_core.prompts`)  
  Utilizado para formatar adequadamente o prompt.

### dotenv:

- **load_dotenv**  
  Utilizado para carregar as variáveis de ambiente a partir do arquivo `.env`.

---

### Como executar:

1. Crie um arquivo `.env` na raiz do projeto.
2. Dentro dele, adicione a variável:

   ```env
   CHATGPT_API_KEY=sua_chave_aqui

------------------------------------------------------------------------

## 🇺🇸 EN-US

### Description

Simple AI prompt with Python.

This code contains imports from **LangChain** sub-libraries and
**dotenv**.

### LangChain sub-libraries used

-   **ChatOpenAI** (`langchain_openai`)  
    Ensures connection with the ChatGPT model.

-   **PromptTemplate** (`langchain_core.prompts`)  
    Used to properly format the prompt.

### dotenv

-   **load_dotenv**  
    Loads environment variables from the `.env` file.

------------------------------------------------------------------------

### ▶ How to execute

1.  Create a `.env` file in the root directory of the project.
2.  Add the variable:

``` env
CHATGPT_API_KEY=your_api_key_here
```

3.  You can:

    -   **Option 1:** Modify the `PromptTemplate` and add an input to
        dynamically write your own prompt.
    -   **Option 2:** Simply change the prompt string and modify the
        variables already used in the code.

4.  Run the Python file:

``` bash
python main.py
```

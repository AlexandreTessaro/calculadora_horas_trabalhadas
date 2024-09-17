# Calculadora de Horas Trabalhadas

Este projeto é uma calculadora de horas trabalhadas desenvolvida em Python. A aplicação permite inserir horários de início, término, e intervalo de almoço, e calcula automaticamente o total de horas trabalhadas no dia. A calculadora suporta formatos de horários com ou sem dois pontos (`HH:mm` ou `Hmm`) e também permite horários invertidos (como cruzar a meia-noite).

## Funcionalidades

-   **Cálculo de horas trabalhadas**: Inserindo o horário de início e término no formato `HH:mm` ou `Hmm`.
-   **Desconto de intervalo de almoço**: Permite inserir um intervalo de almoço que será descontado do total de horas trabalhadas.
-   **Suporte a horários invertidos**: Flexibilidade para inserir horários onde o término é anterior ao início, como casos onde o trabalho cruza a meia-noite.
-   **Inserção de horários sem dois-pontos (`:`)**: A aplicação permite inserir horários tanto no formato `HH:mm` quanto `Hmm`, convertendo automaticamente quando necessário.

## Como executar o projeto

### 1. Clone o repositório



`git clone <url-do-repositorio>
cd calculadora_horas_trabalhadas` 

### 2. Instale as dependências

Este projeto não tem dependências externas além da biblioteca padrão do Python, então não é necessário instalar pacotes adicionais.

### 3. Execute o programa principal

Você pode rodar o programa principal para calcular as horas trabalhadas inserindo os dados manualmente:

`python main.py` 

### 4. Rodar os testes

Os testes unitários estão incluídos para garantir que todas as funcionalidades estão corretas. Para rodar os testes, use o seguinte comando:


`python -m unittest src/testes/test_calculadora.py` 

### Exemplo de Uso

Ao rodar o programa, você pode inserir os horários de início, término, e intervalo de almoço (opcional). Exemplo:

`Bem-vindo à Calculadora de Horas Trabalhadas!`
`Insira o horário de início (HH:mm ou Hmmm): 800`
`Insira o horário de término (HH:mm ou Hmmm): 1700`
`Insira o intervalo de almoço (HH:mm ou Hmmm, ou deixe em branco para nenhum): 100`
`Você trabalhou 8.00 horas.` `

Neste exemplo, o usuário trabalhou das 08:00 às 17:00 com um intervalo de almoço de 1 hora, totalizando 8 horas de trabalho.

## Estrutura do Projeto



`calculadora_horas_trabalhadas/`
`│`
`├── src/`
`│   ├── __init__.py               # Define o diretório como um pacote Python`
`│   ├── calculadora.py            # Funções principais para calcular horas trabalhadas`
`│   ├── formatacao.py             # Funções auxiliares de validação e formatação de horários`
`│   └── testes/`
`│       ├── __init__.py           # Define o diretório como um pacote`
`│       └── test_calculadora.py   # Testes unitários para a aplicação`
`│`
`├── main.py                       # Script principal para executar a aplicação`
`├── README.md                     # Arquivo de documentação (este arquivo)`


## Testes

Os testes foram implementados utilizando a biblioteca `unittest` do Python. Eles cobrem os seguintes cenários:

1.  **Validação de horários**: Testa horários válidos e inválidos no formato `HH:mm`.
2.  **Cálculo de horas trabalhadas**: Testa a precisão do cálculo com horários normais e horários invertidos (fim antes do início).
3.  **Cálculo de horas com intervalo**: Verifica se o cálculo das horas desconta corretamente o intervalo de almoço.
4.  **Formatação de horários sem dois-pontos**: Verifica se a formatação de horários sem dois-pontos (`800` → `08:00`) está correta.
5.  **Testes adicionais**: Casos como horários máximos (23:59), intervalos maiores que o período de trabalho e formatos inválidos também são cobertos.

Para rodar todos os testes:


`python -m unittest src/testes/test_calculadora.py` 

## Melhorias Futuras

-   Implementação de uma interface gráfica simples (GUI) para facilitar o uso da calculadora de horas trabalhadas.
-   Suporte para fusos horários diferentes e jornadas de trabalho internacionais.
-   Adicionar logs de erros e um histórico de cálculos.

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções para este projeto! Para contribuir:

1.  Faça um fork do repositório.
2.  Crie uma nova branch para sua feature (`git checkout -b feature-minha-feature`).
3.  Commit suas alterações (`git commit -m 'Adiciona nova feature'`).
4.  Faça o push da branch (`git push origin feature-minha-feature`).
5.  Abra um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Para mais detalhes, consulte o arquivo LICENSE.
# Copa Passa a Bola - Sistema em Python

Este projeto é um sistema em **Python** para simular o gerenciamento da **Copa Passa a Bola**, permitindo criar times, adicionar jogadoras e salvar os dados em arquivos.

---

## Funcionalidades

- Criar conta de **jogadora** ou **torcedora**
- Criar **times** e inscrever em campeonatos
- Adicionar jogadoras ao time (máx. 10 por time)
- Salvar times e jogadoras em `times.txt`
- Acessar menus exclusivos para jogadoras e torcedoras
- Exibir notícias, jogos do dia e chaveamento

---

## Exemplo de Uso

### Criando um time
⚽ Campeonatos Disponíveis:
Edição 1 - Copa PAB Teste | Disponível: False
Edição 2 - PAB Edição 2 | Disponível: False
Edição 3 - PAB Edição 3 | Disponível: True

Digite a edição do campeonato que deseja ingressar: 3
Digite o nome do seu time: Leonas FC
✅ Time criado e inscrito com sucesso!

### Adicionando jogadora
Deseja adicionar jogadoras ao time Leonas FC? 1 - Sim | 2 - Não: 1
Digite o nome da jogadora: Adriana
Jogadora adicionada com sucesso

### Arquivo `times.txt` gerado
Time: Leonas FC
Jogadoras: 
- Adriana
- Nicole
- Sara
- Gabriela
---

## Como executar

1. Instale o **Python 3.13** (ou superior).
2. Clone este repositório.
3. Execute no terminal:
```bash
python main.py

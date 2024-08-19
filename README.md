
# Coolvert

**Descrição:** Esse é o projeto de um aplicativo que liga músicos a contratantes.

## Configuração do Ambiente

### 1. Criar o ambiente virtual

```bash
python -m venv venv
```
### 2. Acessar o ambiente virtual
```bash
venv\Scripts\Activate
```

### 3. Baixar os requisitos
```bash
pip install -r requirements.txt
```

## Como rodar o projeto
```bash
python run.py
```

## Funcionalidades implementadas
1. Cadastro.
2. Login.
3. Criar demanda. (contratante)
4. Listar demandas. (contratante)
5. Listar demandas. (músico)  
   **OBS:** Essa funcionalidade não implementa os filtros por localidade e estilo, ela apenas mostra todas as demandas disponíveis no banco de dados que não estão no processo de fechar contrato.
6. Candidatar-se a demanda - Match. (músico)
7. Listar candidatos de uma demanda. (contratante)
8. Chat.
9. Fechar contrato. (contratante)  
    **OBS:** Para essa funcionalidade foi implementada apenas um botão para o contratante. Quando ele confirma o fechamento de contrato, o músico também precisa confirmar, mas essa notificação não é enviada. A demanda se torna invisível para os músicos, e não aparece mais o botão de fechar contrato para o contratante.

### Banco de dados
  O banco de dados já foi implementado para todas as classe do projeto, inclusive para as classes que não foram implementadas telas, como avaliação e perfil. 

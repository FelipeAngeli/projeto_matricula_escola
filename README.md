
# Sistema de Matrícula Escolar

Este projeto é um sistema de **back-end** desenvolvido com **Django** e **Django Rest Framework (DRF)**. Ele permite o gerenciamento de matrículas escolares, com funcionalidades para cadastrar alunos e matérias escolares.

---

## 📚 Funcionalidades

- **Cadastro de Alunos**: 
  - Nome, idade, data de nascimento e outras informações relevantes.
  
- **Cadastro de Matérias Escolares**: 
  - Nome da matéria, descrição e código identificador.

- **Listagem de Dados**:
  - Visualização de alunos cadastrados e matérias disponíveis.

- **Detalhes Individuais**:
  - Obtenção de detalhes de um aluno ou matéria específica.

- **Edição e Exclusão**:
  - Atualização ou remoção de alunos e matérias.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Django**: Framework para o desenvolvimento rápido e seguro do back-end.
- **Django Rest Framework (DRF)**: Para criação de APIs RESTful.

---

## 📦 Instalação e Execução

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/FelipeAngeli/projeto_matricula_escola.git
   cd projeto_matricula_escola
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Execute as migrações:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Inicie o servidor local:**

   ```bash
   python manage.py runserver
   ```

6. **Acesse o sistema no navegador:**  
   `http://127.0.0.1:8000/`

---

## 📄 Endpoints da API

### Alunos
- `GET /api/alunos/` - Listar todos os alunos.
- `POST /api/alunos/` - Cadastrar um novo aluno.
- `GET /api/alunos/<id>/` - Obter detalhes de um aluno específico.
- `PUT /api/alunos/<id>/` - Atualizar informações de um aluno.
- `DELETE /api/alunos/<id>/` - Excluir um aluno.

### Matérias
- `GET /api/materias/` - Listar todas as matérias.
- `POST /api/materias/` - Cadastrar uma nova matéria.
- `GET /api/materias/<id>/` - Obter detalhes de uma matéria específica.
- `PUT /api/materias/<id>/` - Atualizar informações de uma matéria.
- `DELETE /api/materias/<id>/` - Excluir uma matéria.

---

## 🚀 Melhorias Futuras

- Implementação de autenticação para controle de acesso.
- Criação de relacionamentos entre alunos e matérias.
- Relatórios de matrículas e desempenho dos alunos.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar *issues* ou abrir *pull requests* para melhorias ou correções.

1. **Faça um fork do projeto.**
2. Crie sua *feature branch*: `git checkout -b minha-nova-feature`
3. Realize as alterações e *commite*: `git commit -m 'Adicionei nova feature'`
4. Envie para o repositório remoto: `git push origin minha-nova-feature`
5. Abra um *pull request*.

---

## 📝 Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

💻 **Desenvolvido por [Felipe Angeli Trebien](https://github.com/FelipeAngeli)**  

🎯 "Simplificando a gestão escolar com tecnologia!"

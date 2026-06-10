# 🏎️ Highway Dodgers

Este é um jogo no estilo *endless runner* (corrida infinita) desenvolvido como projeto acadêmico. A mecânica foi inspirada nos clássicos jogos de carrinho dos antigos celulares de botão, onde o jogador deve desviar de obstáculos e sobreviver pelo maior tempo possível.

## 👤 Autor
* **Dono do projeto:** Antonio Carlos P. Vancini  
* **RA:** 1139402

---

## 💡 Sobre o Projeto
A ideia inicial era desenvolver um jogo simples de navegador controlado pelas setas do teclado (Esquerda / Direita). Durante o processo de concepção, decidi resgatar a nostalgia dos jogos de blocos e carros de celulares antigos, trazendo essa dinâmica para um projeto de faculdade moderno em Python.

Atualmente o projeto cumpre com todos os requisitos acadêmicos básicos exigidos, funcionando como uma base sólida para futuras expansões e melhorias visuais e de jogabilidade.

---

## 🛠️ Tecnologias e Conceitos Utilizados

O jogo foi desenvolvido em **Python** utilizando as seguintes bibliotecas:
* [Pygame](https://pygame.org) - Para renderização de gráficos, controle de tela e eventos.
* [Pyttsx3](https://readthedocs.io) - Para síntese de voz e recursos de áudio falado (conversão de texto em som).

### Conceitos de Programação Aplicados:
* **Estruturas de Repetição:** Loops de jogo (*Game Loop*) para manter a execução contínua.
* **Estruturas Condicionais:** Detecção de colisões, controle de pontuação e fim de jogo (*Game Over*).
* **Funções:** Modularização do código para organização de elementos e interface.
* **Manipulação de Áudio:** Inclusão de trilha sonora de fundo, efeitos sonoros e narração por voz.
* **Sistema de Conquistas:** Lógica implementada para premiar o jogador de acordo com o progresso.

---

## 🚀 Próximos Passos (Melhorias Futuras)
Como o projeto continua em constante evolução, os planos futuros incluem:
- [ ] Implementação de novos cenários e melhorias gráficas (*sprites*).
- [ ] Sistema de pontuação máxima (High Score) salvo localmente.
- [ ] Ajuste gradual de dificuldade conforme o tempo de sobrevivência aumenta.

---

## 💻 Como Executar o Projeto

1. Certifique-se de ter o Python instalado.
2. Instale as bibliotecas necessárias executando:
   ```bash
   pip install pygame pyttsx3
   ```
3. Execute o jogo com:
   ```bash
   python main.py
   ```
*(Ou utilize o executável gerado na pasta `build`).*


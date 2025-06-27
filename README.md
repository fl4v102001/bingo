Sorteio de Números - Painel para Bingo
Um painel web moderno e interativo para exibir números sorteados em um jogo de bingo. A aplicação é totalmente personalizável, responsiva e foi criada para ser exibida para o público durante um evento. Não requer instalação, rodando diretamente no navegador.

Visão Geral
Esta aplicação fornece uma interface visualmente atraente para o gerenciamento de um sorteio de bingo. O locutor pode inserir os números sorteados, e o painel os exibe em destaque, junto com a letra correspondente (B-I-N-G-O). Além disso, oferece recursos avançados como personalização de cores, animações, visualização de cartela e integração via API.

(Sugestão: Adicione aqui um screenshot ou um GIF da aplicação em funcionamento)

✨ Principais Funcionalidades
Exibição em Tempo Real: Mostra instantaneamente os 3 últimos números sorteados em círculos de destaque.
Identificação de Letra (B-I-N-G-O): Identifica e exibe automaticamente a letra correspondente a cada número.
Temas Light & Dark: Alterne entre um tema claro e escuro com um único clique.
Personalização de Cores: Altere as cores da borda e do círculo principal em tempo real usando seletores de cor.
Animação de "Bingo!": Uma animação de fogos de artifício celebra a vitória quando o comando bingo é ativado.
Visualizador de Cartela: Um modal exibe todos os números já sorteados, organizados em colunas (B, I, N, G, O).
Configuração Avançada:
Defina as faixas de número para cada letra.
Crie até 5 mensagens personalizadas para serem exibidas em um letreiro no topo da tela.
Configure uma URL de API para integração.
Design Responsivo: A interface se adapta perfeitamente a telas de desktop, tablets e celulares.
Persistência de Dados: Suas configurações de tema, cores e faixas são salvas localmente no navegador.
🚀 Como Usar
A aplicação é um único arquivo HTML. Não há necessidade de build ou servidor.

Baixe o arquivo index.html.
Abra-o em um navegador de internet moderno (Google Chrome, Mozilla Firefox, Microsoft Edge, etc.).
A aplicação está pronta para ser usada!
Operação Básica
Inserir Números: Digite ou cole os números sorteados na área de texto na parte inferior da tela. Os números devem ser separados por espaços.
Exemplo: 15 32 60 8 71
Comandos Especiais: Digite uma das palavras abaixo como o último item na área de texto para ativar uma ação:
bingo: Aciona a animação de fogos de artifício.
parar: Interrompe a animação de fogos de artifício.
limpar ou resetar: Limpa todos os números da tela e do histórico.
⚙️ Painel de Controle e Configurações
Na parte inferior direita, você encontra os seguintes controles:

🎨 Seletores de Cor: Três círculos coloridos que permitem alterar:
Cor da borda principal.
Cor de fundo do círculo maior.
Cor da fonte do círculo maior.
⚙️ (Engrenagem): Abre o modal de Configuração Avançada.
🌙/☀️ (Lua/Sol): Alterna entre o tema escuro e o claro.
Detalhes da Configuração Avançada
No modal de configuração, você pode ajustar:

Faixas de Números: Defina os valores mínimo e máximo para cada letra (B, I, N, G, O).
Mensagens do Letreiro: Escreva mensagens personalizadas e defina por quanto tempo (em segundos) cada uma será exibida no letreiro superior.
API URL: Informe um endereço web para o qual os dados do sorteio serão enviados (veja a seção de Integração via API).
🔌 Integração via API (Para Desenvolvedores)
A aplicação pode enviar o estado atual do sorteio para um servidor remoto, permitindo a exibição dos dados em uma segunda tela, em uma transmissão ao vivo (overlay) ou em outro sistema.

Endpoint: A aplicação enviará os dados para o endereço que você fornecer no campo "API", com o caminho /input.
Exemplo: Se você configurar a URL http://meuservidor.com, a requisição será feita para http://meuservidor.com/input.
Método: POST
Corpo da Requisição (body): O payload enviado é uma string no formato text/html. Ele contém uma tabela HTML completa com todos os números sorteados e estilos CSS embutidos para uma renderização imediata.
Exemplo do Payload enviado:

HTML

<meta charset="UTF-8"><h1>Sua Mensagem 1</h1><style>...</style><table><thead><tr><th>B</th><th>I</th><th>N</th><th>G</th><th>O</th></tr></thead><tbody><tr><td>8</td><td>21</td><td>32</td><td>46</td><td>71</td></tr><tr><td>15</td><td></td><td></td><td>60</td><td></td></tr>...</tbody></table><a href="https://github.com/fl4v102001/bingo/" target="_blank">fl4v102001/bingo</a>


🛠️ Tecnologias Utilizadas
HTML5: Estrutura semântica e elemento <canvas> para animações.
CSS3: Estilização moderna com Flexbox, Variáveis CSS e Animações (@keyframes).
JavaScript (Vanilla): Toda a lógica é escrita em JavaScript puro e moderno (ES6+), com uma arquitetura orientada a objetos (Classes) para separar responsabilidades (UI, Estado e Lógica).
📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

✍️ Autor
Flávio - fl4v102001
Projeto Original: https://github.com/fl4v102001/bingo/
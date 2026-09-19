================================================================================
QUESTÃO 1 - ITEM A
================================================================================

1. INTERPOLAÇÃO BILINEAR

A interpolação bilinear estima a intensidade do pixel a partir dos seus 4 vizinhos mais próximos (grade 2x2) na imagem original. No mapeamento inverso, as coordenadas inteiras da nova imagem recaem em posições fracionárias; o algoritmo realiza interpolações lineares sucessivas primeiro na direção horizontal e, em seguida, na direção vertical, ponderando as intensidades pela proximidade em relação aos cantos da célula.
- Características: Garante continuidade nos níveis de intensidade (ordem zero), gerando transições suaves de tons de cinza.
- Vantagens: Elimina o aspecto pixelado e o serrilhamento grosseiro do vizinho mais próximo, mantendo baixo custo computacional e rapidez por envolver apenas ponderações lineares simples.
- Desvantagens: Provoca um leve embaçamento (blur), atenuando bordas nítidas e detalhes finos da imagem.

2. INTERPOLAÇÃO BICÚBICA

A interpolação bicúbica utiliza uma vizinhança de 16 pixels (grade 4x4) e polinômios cúbicos por partes baseados no kernel de convolução de Keys. O processo é separável em duas dimensões: realizam-se quatro interpolações cúbicas ao longo das linhas e uma vertical entre os resultados, aplicando pesos que variam suavemente com a distância e contêm coeficientes negativos que realçam os contornos.
- Características: Assegura continuidade de primeira ordem (valores e derivadas contínuas), gerando superfícies sem arestas abruptas.
- Vantagens: Qualidade visual superior, preservando bordas nítidas, transições contínuas e detalhes finos sem a perda de foco da bilinear e sem a pixelização do vizinho mais próximo.
- Desvantagens: Custo computacional elevado, sendo significativamente mais lenta por avaliar 16 vizinhos com cálculos cúbicos, além de poder gerar artefatos de sobreoscilação (efeito halo) em transições de alto contraste, exigindo truncamento dos valores entre 0 e 255.


================================================================================
QUESTÃO 1 - ITEM B
================================================================================

1. QUALIDADE DA IMAGEM

Nas transformações geométricas de escala, rotação e cisalhamento, os três métodos apresentam diferenças visuais nítidas:
- Vizinho Mais Próximo: Por apenas arredondar coordenadas da matriz inversa, gera blocos pixelizados evidentes em ampliações (escala) e forte serrilhamento (efeito escada) em bordas inclinadas na rotação e no cisalhamento, com perda acentuada de detalhes.
- Bilinear: Elimina a pixelização e ameniza o serrilhamento por meio da média ponderada dos 4 vizinhos, produzindo contornos contínuos, porém com leve embaçamento e atenuação de contraste nas texturas finas.
- Bicúbica: Apresenta o melhor acabamento em todas as transformações, mantendo linhas inclinadas suaves e contínuas no cisalhamento e na rotação, além de máxima nitidez e definição de detalhes na ampliação por escala, sem introduzir desfoque.

2. DESEMPENHO COMPUTACIONAL

O tempo de processamento é proporcional ao número de amostras avaliadas por pixel de destino:
- Vizinho Mais Próximo: É o método mais rápido e simples (O(1)), com tempo na faixa de 15 a 43 ms nos testes, exigindo apenas um arredondamento e uma leitura de memória por pixel.
- Bilinear: Apresenta custo intermediário (O(4)), com tempo entre 60 e 208 ms (cerca de 3 a 5 vezes mais lenta que o vizinho mais próximo), decorrente do cálculo de distâncias fracionárias e quatro ponderações lineares.
- Bicúbica: É a mais lenta e custosa (O(16)), com tempos entre 273 e 991 ms (cerca de 15 a 20 vezes mais lenta que o vizinho mais próximo), em razão das 16 leituras de memória e operações polinomiais de terceiro grau por coordenada.

Em síntese, a interpolação bilinear oferece o equilíbrio ideal para aplicações interativas e processamento em tempo real, enquanto a bicúbica é a escolha mandatória quando a fidelidade visual, a nitidez e a qualidade estética são prioridades.
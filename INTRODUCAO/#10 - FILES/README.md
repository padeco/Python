O que é um arquivo?
Antes de começarmos a trabalhar com arquivos em Python, é importante entender o que é exatamente um arquivo e como os sistemas operacionais modernos lidam com alguns de seus aspectos.

Em sua essência, um arquivo é um conjunto contíguo de bytes usado para armazenar dados . Esses dados são organizados em um formato específico e podem ser tão simples como um arquivo de texto ou tão complicados como um executável de programa. No final, esses arquivos de bytes são então traduzidos para o binário 1e 0para um processamento mais fácil pelo computador.

Os arquivos na maioria dos sistemas de arquivos modernos são compostos de três partes principais:

1 Cabeçalho: metadados sobre o conteúdo do arquivo (nome do arquivo, tamanho, tipo e assim por diante)
2 Dados: conteúdo do arquivo conforme escrito pelo criador ou editor
3 Fim do arquivo (EOF): caractere especial que indica o fim do arquivo

Caminhos de arquivo
Quando você acessa um arquivo em um sistema operacional, é necessário um caminho de arquivo. O caminho do arquivo é uma string que representa a localização de um arquivo. Está dividido em três partes principais:

1 Caminho da pasta: o local da pasta de arquivos no sistema de arquivos onde as pastas subsequentes são separadas por uma barra /(Unix) ou barra invertida \(Windows)
2 Nome do arquivo: o nome real do arquivo
3 Extensão: o final do caminho do arquivo pré-pendente com um ponto ( .) usado para indicar o tipo de arquivo
Aqui está um exemplo rápido. Digamos que você tenha um arquivo localizado em uma estrutura de arquivo como esta:

/
│
├── path/
|   │
│   ├── to/
│   │   └── cats.gif
│   │
│   └── dog_breeds.txt
|
└── animals.csv


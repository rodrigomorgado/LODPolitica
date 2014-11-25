# Base de dados em Linked Open Data - Eleições 2014

## Introdução

  No último mês de outubro, ocorreram as últimas eleições para escolher os representantes da população brasileira nos próximos quatro anos. Foram realizadas eleições para presidente, governadores, senadores, deputados federais, estaduais e distritais.
  
  Com o advento da internet e com a grande disponibilidade de informações, a população tem cada vez mais possibilidade de fiscalizar e tomar conhecimento dos acontecimentos dentro do âmbito político nacional. Nesses eleições em específico, as redes sociais e portais de notícia online tiveram grande participação e influência nos debates que ocorreram entre os eleitores. Muitas denúncias e informações foram propagadas e compartilhadas na rede, sendo algumas verídicas, outras não.
  
  Durante as aulas da disciplina, foram apresentados alguns conceitos sobre o Linked Open Data, que se trata basicamente de uma série de base de dados aberta, que disponibiliza seus dados na Web em formato RDF, e esses datasets são ligados uns aos outros.
  
  A partir daí, surgiu a ideia a partir de um e-mail de unir esses dois mundos e gerar uma base de dados sobre o cenário político brasileiro em RDF, e uni-la a outras bases existentes, contribuindo para a nuvem de LOD. Esse relatório tem por objetivo apresentar as ferramentas e etapas realizadas durante o trabalho, além de citar as dificuldade encontradas ao longo do desenvolvimento e sugestões de trabalhos futuros.

## Fonte dos dados utilizados

  Para a realização do trabalho, era necessário encontrar uma base de dados com uma boa documentação das informações nela contidas, além de possuir dados variados e confiáveis sobre o cenário político e eleitoral brasileiro. O portal Transparência Brasil (http://www.transparencia.org.br/) disponibilizou em agosto desse ano uma API (http://dev.transparencia.org.br/api-portal/), para acesso aos seus dados, a fim de estimular a construção de projetos e apps que auxiliassem na divulgação e utilização dessas informações pela população, contribuindo para a democracia brasileira.
  
  A API é aberta, bastando criar um cadastro no site do próprio portal e inserir no cadastro o app que deseja ser criado utilizando a API. Uma vez feito esse processo, é disponibilizado um token para acesso a base de dados. A base de dados confirmou suas características de corretude, com dados confiáveis, e completude, tendo sido encontrados poucos campos nulos ou sem informação.

## Informações disponibilizadas na API

  Na API do portal Transparência Brasil, há uma série de informações disponibilizadas. Essas informações podem ser divididas em 5 categorias principais:
    1. Candidatos - Fornece informações sobre os candidatos a todos os cargos nas eleições de 2014
    2. Partidos - Fornece dados básicos sobre todos os partidos registrados que tiveram candidatos nas eleições de 2014
    3. Estados - Disponibiliza dados básicos sobre os estados que compõe da federação
    4. Cargos - Fornece uma lista de todos os cargos em disputa nas eleições de 2014
    5. Excelências - Fornece informações pessoais e sobre a atuação dos deputados e senadores em atuação no cenário político brasileiro
    
### 1. Candidatos
 
 Para cada candidatos, são fornecidas uma série de informações pessoais, como nome completo, CPF, estado da federação a qual ele pertence, entre outras. Além disso, são fornecidos links sobre possíveis processos aos quais o candidato está sendo julgado.
 
  É possível também recuperar informações sobre os bens declarados do candidato, sobre suas candidaturas em eleições anteriores e estatísticas sobre a sua atuação em cargos públicos ocupados pelo menos ao longo de sua carreira.
  
### 2. Partidos

  A API fornece apenas a sigla de cada um dos partidos que tiveram candidatos na eleição de 2014.

### 3. Estados

  A API fornece o nome e a sigla de cada um dos estados da federação, incluindo o distrito federal e a própria União.

### 4. Cargos

  A API fornece o nome de cada um dos cargos concorridos nas últimas eleições, incluindo suplentes de senadores, vice-presidentes e vice-governadores.

### 5. Excelências

 A API fornece dados pessoais e históricos sobre atuação e candidaturas passadas dos políticos que estão atualemente em exercício na câmara dos deputados e no senado federal. Além disso, a base fornece também dados sobre os bens declarados de cada uma das atuais excelências do cenário político brasileiro.

## Tecnologias usadas

  Para gerar o rdf e fazer as requisições para a API, optou-se por utilizar a linguagem Python. Os códigos fontes para as requisições feitas e para a geração do arquivo RDF encontram-se nesse repositório, na pasta códigos.
  
  Para linkar a base de dados criada com outra base de dados na nuvem de LOD, optou-se por utilizar a ferramenta dataTXT (https://dandelion.eu/products/datatxt/). Essa ferramente foi encontrada e apresentada em uma aula da disciplina pela prória dupla. Essa ferramenta possui uma série de recursos que auxiliam na extração de entidades nomeadas em textos. Ela não só identifica as entidades, como traz uma série de outras informações referentes as mesmas.
  
  Um fator diferencial do dataTXT para outras ferramentas é a capacidade de extração de entidades em diversas línguas, incluindo português, o que foi primordial para o trabalho aqui apresentado. Essa ferramenta mostrou-se muito útil e simplificou o trabalho de linkagem com outra base LOD. No caso, o dataTXT tem a opção de retornar o link para a entidade encontrada na DBPedia.

## Sintaxe 'politica'

## Dificuldades encontradas

  Embora muito eficiente, a ferramenta dataTXT por algumas vezes acaba por fazer um link incorreto do recurso colocado na base de dados criada. Ao realizar testes com diferentes níveis de confiança para a extração de entidades nomeadas no dataTXT verificou-se que, com uma confiança alta, algumas entidades nomeadas não dúbias não eram reconhecidas e outras continuavam sendo classificadas incorretamente. Ao colocar a confiança baixa, o número de entidades encontradas era consideravelmente maior e o número de erros era semelhante, proporcionalmente. Optou-se, então, por colocar um nível de confiança baixo na extração das entidades nomeadas para encontrar o link da DBPedia associado ao recurso inserido.
  
  O fato de o número de erros continuar semelhante independentemente do nível de confiança colocado se deve ao fato de algumas das consultas serem dúbias, ou seja, de haver mais de uma entidade com a mesma representação. Dois exemplos deixam claro essa questão.
  
  A API da Transparência Brasil fornece apenas a sigla de cada um dos partidos. Portanto, ao fazer a consulta no dataTXT para o partido, colocou-se para consulta a sua sigla. Um dos partidos existentes no cenário nacional é o PR, Partido da República. Ao fazer a consulta com a sigla PR no dataTXT, essa ferramenta retornava com grande confiança que essa sigla se referia ao estado do Paraná, cuja sigla também é PR. O mesmo ocorre quando é colocado o nome de um político que possua um homônimo famoso.

## Trabalhos futuros

===========

Este trabalho foi realizado como trabalho final da disciplina Tópicos Espceiais em Sistemas Inteligentes, em 2014.2, na Universidade Federal do Rio de Janeiro - UFRJ.

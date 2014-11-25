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

## Sintaxe 'politica'

## Dificuldades encontradas

## Trabalhos futuros

===========

Este trabalhos foi realizado como trabalho final da disciplina TESI - 2014.2

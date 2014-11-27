# Base de dados em Linked Open Data - Eleições 2014

## Introdução

  No último mês de outubro, ocorreram as últimas eleições para escolher os representantes da população brasileira nos próximos quatro anos. Foram realizadas eleições para presidente, governadores, senadores, deputados federais, estaduais e distritais.
  
  Com o advento da internet e com a grande disponibilidade de informações, a população tem cada vez mais possibilidade de fiscalizar e tomar conhecimento dos acontecimentos dentro do âmbito político nacional. Nesses eleições em específico, as redes sociais e portais de notícia online tiveram grande participação e influência nos debates que ocorreram entre os eleitores. Muitas denúncias e informações foram propagadas e compartilhadas na rede, sendo algumas verídicas, outras não.
  
  Durante as aulas da disciplina, foram apresentados alguns conceitos sobre o Linked Open Data, que se trata basicamente de uma série de base de dados aberta, que disponibiliza seus dados na Web em formato RDF, e esses datasets são ligados uns aos outros.
  
  A partir daí, surgiu a ideia, a partir de um e-mail enviado no grupo de discussão da disciplina, de unir esses dois mundos e gerar uma base de dados sobre o cenário político brasileiro em RDF, e uni-la a outras bases existentes, contribuindo para a nuvem de LOD. Esse relatório tem por objetivo apresentar as ferramentas e etapas realizadas durante o trabalho, além de citar as dificuldade encontradas ao longo do desenvolvimento e sugestões de trabalhos futuros.

## Fonte dos dados utilizados

  Para a realização do trabalho, era necessário encontrar uma base de dados com uma boa documentação das informações nela contidas, além de possuir dados variados e confiáveis sobre o cenário político e eleitoral brasileiro. O portal Transparência Brasil (http://www.transparencia.org.br/) disponibilizou em agosto desse ano uma API (http://dev.transparencia.org.br/api-portal/), para acesso aos seus dados, a fim de estimular a construção de projetos e apps que auxiliassem na divulgação e utilização dessas informações pela população, contribuindo para a democracia brasileira.
  
  A API é aberta, bastando criar um cadastro no site do próprio portal e inserir no cadastro o app que deseja ser criado utilizando a API. Uma vez feito esse processo, é disponibilizado um token para acesso a base de dados. A base de dados confirmou suas características de corretude, com dados confiáveis, e completude, tendo sido encontrados poucos campos nulos ou sem informação.
  
  Outras bases semelhantes foram procuradas, mas somente uma foi encontrada. Tratava-se de um arquivo .csv contendo informações sobre os candidatos a eleição no ano de 2014. Porém, esse tabela não possuía nenhum metadado, o que dificultaria bastante a sua utilização. Portanto, para esse trabalho, apenas os dados da API da Transparência Brasil foram utilizados como fonte de dados da polítca brasileira

## Informações disponibilizadas na API da Transparência Brasil

  Na API do portal Transparência Brasil, há uma série de informações disponibilizadas. Essas informações podem ser divididas em 5 categorias principais:
  
    1. Candidatos - Fornece informações sobre os candidatos a todos os cargos nas eleições de 2014
    
    2. Partidos - Fornece dados básicos sobre todos os partidos registrados que tiveram candidatos na eleições de 2014
    
    3. Estados - Disponibiliza dados básicos sobre os estados que compõe da federação
    
    4. Cargos - Fornece uma lista de todos os cargos em disputa nas eleições de 2014
    
    5. Excelências - Fornece informações pessoais e sobre a atuação dos deputados e senadores em atividade no cenário político brasileiro
    
### 1. Candidatos
 
 Para cada candidato, são fornecidas uma série de informações pessoais, como nome completo, CPF, estado da federação a qual ele pertence, entre outras. Além disso, são fornecidos links sobre possíveis processos aos quais o candidato está sendo julgado.
 
  É possível também recuperar informações sobre os bens declarados do candidato, sobre suas candidaturas em eleições anteriores e estatísticas sobre a sua atuação em cargos públicos ocupados pelo mesmo ao longo de sua carreira.
  
### 2. Partidos

  A API fornece apenas a sigla de cada um dos partidos que tiveram candidatos na eleição de 2014.

### 3. Estados

  A API fornece o nome e a sigla de cada um dos estados da federação, incluindo o distrito federal e a própria União.

### 4. Cargos

  A API fornece o nome de cada um dos cargos concorridos nas últimas eleições, incluindo suplentes de senadores, vice-presidentes e vice-governadores.

### 5. Excelências

 A API fornece dados pessoais e históricos sobre atuação e as candidaturas passadas dos políticos que estão atualmente em exercício na câmara dos deputados e no senado federal. Além disso, a base fornece também dados sobre os bens declarados de cada uma das atuais excelências do cenário político brasileiro.

## Tecnologias usadas

  Para gerar o RDF e fazer as requisições para a API, optou-se por utilizar a linguagem Python. Os códigos fontes para as requisições feitas e para a geração do arquivo RDF encontram-se nesse repositório, na pasta códigos.
  
  Para linkar a base de dados criada com outra base de dados na nuvem de LOD, optou-se por utilizar a ferramenta dataTXT (https://dandelion.eu/products/datatxt/). Essa ferramenta foi encontrada e apresentada em uma aula da disciplina pela prória dupla. Ela possui uma série de recursos que auxiliam na extração de entidades nomeadas em textos. Ela não só identifica as entidades, como traz uma série de outras informações referentes as mesmas.
  
  Um fator diferencial do dataTXT para outras ferramentas é a sua capacidade de extração de entidades em diversas línguas, incluindo português, o que foi primordial para o trabalho aqui apresentado. Essa ferramenta mostrou-se muito útil e simplificou o trabalho de linkagem com outra base LOD. No caso, o dataTXT tem a opção de retornar o link para a entidade encontrada na DBPedia.

## Sintaxe 'politica'

 Por estar trabalhando com uma base de dados com características próprias e, optou-se por criar uma nova sintaxe a ser referenciada no arquivo rdf. Essa novo sintaxe recebeu o nome de 'política'. 
 
 Para criar a sintaxe, primeiro é necessário dizer que foram utilizados os prefixos de xsd, rdf e rdfs para trabalhar melhor com nossos dados e fazer a descrição das propriedades criadas.
 
 A maior parte das propriedades que compõe a descrição da sintaxe segue o mesmo padrão. Elas são definidas como rdf:Property e seus rdfs:range e são instâncias também de rdf:Property. Elas possuem labels que discernem sua utilidade, como "municipiosPassados", "apelido" e "partido". Esse labels foram escolhidos a partir de cada uma das chaves dos JSON's que eram retornados com os dados solicitados da API da TRansparÊncia Brasil. Por fim, cada um possui um rdfs:comment que explicite sua função.
 
 Certas propriedades, no entanto, são puramente numéricas, como "estadoId", "CPF" e "titulo". Assim, elas foram consideradas como instâncias de números inteiros não-negativos, e o rdfs:range foi colocado como xsd:nonNegativeInteger. A sintaxe gerada encontra-se disponível nesse repositório

## Etapas do projeto realizadas

  Para gerar o arquivo RDF, optou-se por colher os dados da API e trabalhar diretamente com as strings que comporiam o arquivo. Para gerar a base de dados do trabalho, é gerado um arquivo com extensão .rdf e, a cada requisição feita e informação extraída, a string formadora do conteúdo a ser inserido no arquivo é complementada com a novo informação. Ao final, a string final gerada é inserida no arquivo e o mesmo é salvo.
  
  A cada iteração, é feita uma consulta à API da Transparência BRasil, referente a algum dado que ela possui. Uma vez recuperado os dados, os mesmos são extraídos e, para cada entidade requisitada na API, é gerado um recurso no RDF para a mesma. Cada um dos dados referentes a entidade recuperada é considerado como uma propriedade do recurso recém inserido.
  
  Além disso, para cada entidade requisitada na base de dados do portal da Transparência, é feita uma requisição para a API do dataTXT, a fim de encontrar um link daquela entidade com o DBPedia. Caso alguma entidade seja encontrada, esse é linkada ao recurso gerado através do 'rdf:about' na descrição do recurso. Caso não seja encontrada nenhuma referência na DBPedia, esse recurso é tratado como um recurso anônimo no RDF.
  
  Para cada uma das propriedade dos recursos gerados, é utilizada a sintaxe 'politica' criada nesse trabalho, a fim de descrever o significado de cada uma das propriedades inseridos nos recursos da base.

## Dificuldades encontradas

  Embora muito eficiente, a ferramenta dataTXT por algumas vezes acaba por fazer um link incorreto do recurso colocado na base de dados criada. Ao realizar testes com diferentes níveis de confiança para a extração de entidades nomeadas no dataTXT verificou-se que, com uma confiança alta, algumas entidades nomeadas não dúbias não eram reconhecidas e outras continuavam sendo classificadas incorretamente. Ao colocar a confiança baixa, o número de entidades encontradas era consideravelmente maior e o número de erros era semelhante, proporcionalmente. Optou-se, então, por colocar um nível de confiança baixo na extração das entidades nomeadas para encontrar o link da DBPedia associado ao recurso inserido. Esse valor é de fácil modificação, caso o entendimento para essa questão seja diferente do adotado atualmente.
  
  O fato de o número proporcional de erros continuar semelhante independentemente do nível de confiança colocado se deve ao fato de algumas das consultas serem dúbias, ou seja, de haver mais de uma entidade com a mesma representação. O exemplo a seguir deixa claro essa questão.
  
  A API da Transparência Brasil fornece apenas a sigla de cada um dos partidos. Portanto, ao fazer a consulta no dataTXT para o partido, colocou-se para consulta a sua sigla. Um dos partidos existentes no cenário nacional é o PR, Partido da República. Ao fazer a consulta com a sigla PR no dataTXT, essa ferramenta retornava com grande confiança que essa sigla se referia ao estado do Paraná, cuja sigla também é PR. O mesmo ocorre quando é colocado o nome de um político que possua um homônimo famoso, por exemplo.
  
  Outra questão encontrada durante o desenvolvimento foi a falta de atualização dos dados da API da Transparência Brasil no que se refere às empresas doadoras dos candidatos no ano de 2014. A API fornece a opção de retornar as empresas que fizeram doações para cada um dos candidatos e o montante doado. Porém, até o momento da execução desse trabalho, a API não disponibilizava esses dados sobre as eleições do ano de 2014, apenas para dados de anos anteriores, como em 2010.

## Trabalhos futuros

  O trabalho feito até o momento oferece uma base rica de dados, com a grande parte deles já linkado com a base da DBPedia. Porém, outras tarefas relevantes ainda podem ser realizadas para aperfeiçoar e complementar o projeto. A primeira delas é a análise apurada da porcentagem de acerto dos links com a DBPedia realizados através do dataTXT. Alguns deles estão incorretos, como citado no tópico anterior.
  
  Uma segunda tarefa é linkar essa base de dados com outras bases de LOD, além de linkar os recursos que atualmente não tem nenhum link, que são os recursos anônimos da base criada.
  
  Uma terceira possibilidade de trabalho é aguradar a atualização da API da Transparência Brasil, para que sejam informados os doadores dos candidatos das eleições em 2014. Assim, a atual base de dados poderá receber mais informações relevantes sobre o cenário político brasileiro. Uma sugestão dada em aula é a de colocar as empresas doadoras numa região separada do RDF, ao invés de ser um recurso 'interno' de cada candidato. Essa separação dos doadores numa região própria poderia facilitar uma consulta futura para saber o montante doado por uma certa empresa, e quais candidatos foram financiados pela mesma.
  
  Por fim, uma vez que a base esteja completa e que tenha tido a sua qualidade aferida, ainda é necessário preparar a base para disponibilizá-la para consultas na Web, de tal forma que ela fique integrada a atual nuvem de LOD.

===========

Este trabalho foi realizado como trabalho final da disciplina Tópicos Especiais em Sistemas Inteligentes, em 2014.2, na Universidade Federal do Rio de Janeiro - UFRJ.

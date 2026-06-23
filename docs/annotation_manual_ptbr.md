# Manual de Anotação Axiológica v2.0
## IA e Educação em Posts do Bluesky

## 1. Finalidade do manual

Este manual orienta a anotação axiológica de posts do Bluesky sobre inteligência artificial e educação. O objetivo da anotação é identificar quando um post apresenta algum enquadramento valorativo sobre IA na educação e, quando esse enquadramento existe, posicioná-lo em uma matriz formada por dois eixos: **aceitação** e **intensidade**.

A tarefa não consiste em classificar todo post que mencione “IA”, “ChatGPT”, “professor”, “aluno” ou “educação”. A presença lexical desses termos é apenas um ponto de partida para a coleta. A anotação propriamente dita exige uma decisão interpretativa: verificar se o post oferece evidência textual suficiente para ser colocado em uma matriz axiológica.

A anotação deve responder, nessa ordem:

1. O post é aplicável à matriz axiológica?
2. Se for aplicável, qual é sua orientação de aceitação em relação à IA na educação?
3. Se for aplicável, qual é sua intensidade avaliativa?

A estrutura final esperada para um post aplicável é:

```json
{
  "item_id": 1,
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

A estrutura final esperada para um post não aplicável é:

```json
{
  "item_id": 1,
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

## 2. Unidade de anotação

A unidade de anotação é o **post coletado**.

O anotador deve usar apenas as informações textuais disponíveis no registro coletado. Isso inclui o texto do post e, se estiver presente no próprio registro, trechos visíveis de chamada, manchete, citação, repost ou prévia textual de link. O anotador não deve abrir links externos, pesquisar o perfil do usuário, investigar a intenção do autor fora do post ou buscar contexto adicional na internet.

Quando o post estiver truncado, incompleto ou dependente de contexto ausente, o anotador deve decidir se ainda há evidência textual suficiente para anotação. Se não houver, o post deve ser marcado como não aplicável.

## 3. Visão geral da tarefa

A anotação é hierárquica.

Primeiro, decide-se a **aplicabilidade**. Essa etapa define se o post entra ou não na matriz. Depois, apenas para posts aplicáveis, anotam-se os dois eixos da matriz:

| Etapa | Campo | Valores | Função |
|---|---|---:|---|
| 1 | `applicability_score` | 0 ou 1 | Decide se o post entra na matriz |
| 2 | `acceptance_5` | -2, -1, 0, 1, 2 | Mede a orientação diante da IA na educação |
| 3 | `intensity_5` | 1, 2, 3, 4, 5 | Mede a força avaliativa, retórica ou afetiva do post |

A aplicabilidade **não é um eixo da matriz**. Ela é um critério decisório. A matriz é formada apenas pelos eixos de aceitação e intensidade.

## 4. Árvore de decisão da anotação

Antes de atribuir qualquer rótulo, siga esta sequência.

### Passo 1: o post trata de IA e educação?

Pergunte:

> O post fala, direta ou indiretamente, de inteligência artificial, IA generativa, ChatGPT, LLMs ou ferramentas semelhantes em contexto educacional?

Se a resposta for **não**, marque:

```json
"applicability_score": 0
```

Se a resposta for **sim**, siga para o passo 2.

### Passo 2: há enquadramento valorativo?

Pergunte:

> O post apresenta crítica, defesa, preocupação, entusiasmo, promessa, ameaça, ironia, juízo, risco, benefício, transformação, solução, denúncia, medo, alerta ou outro tipo de valoração sobre IA na educação?

Se a resposta for **não**, marque:

```json
"applicability_score": 0
```

Se a resposta for **sim**, siga para o passo 3.

### Passo 3: a orientação é negativa, neutra/ambivalente ou positiva?

Pergunte:

> O post tende a rejeitar, aceitar ou suspender uma posição clara sobre IA na educação?

A resposta define `acceptance_5`.

### Passo 4: a força textual é baixa, média ou alta?

Pergunte:

> A valoração aparece de forma fraca, moderada, forte ou extrema no texto?

A resposta define `intensity_5`.

## 5. Critério decisório de aplicabilidade

### 5.1 Regra central

Um post só é aplicável quando oferece evidência textual suficiente para ser posicionado na matriz axiológica.

A presença simultânea de termos de IA e educação **não basta**.

A pergunta decisiva é:

> Há algum modo de valoração da IA na educação neste post?

Essa valoração pode ser explícita ou atribuída a outra fonte. Pode aparecer em uma opinião direta, em uma crítica, em uma defesa, em uma promessa, em uma ameaça, em uma chamada jornalística, em uma ironia, em uma metáfora ou em um vocabulário avaliativo.

### 5.2 Quando marcar `applicability_score = 1`

Marque `applicability_score = 1` quando o post trata de IA e educação e permite uma leitura axiológica minimamente justificada.

Isso inclui posts que:

1. criticam o uso de IA por alunos, professores, escolas, universidades ou instituições;
2. defendem ou celebram o uso de IA em ensino, aprendizagem, avaliação, planejamento ou formação;
3. apontam riscos, ameaças, prejuízos, fraudes, plágio, dependência, desigualdade ou precarização;
4. apontam benefícios, inovação, apoio pedagógico, personalização, produtividade ou melhoria da aprendizagem;
5. atribuem a alguém uma posição valorativa sobre IA na educação;
6. usam manchetes, chamadas ou termos jornalísticos com forte enquadramento avaliativo;
7. apresentam ironia ou sarcasmo sobre o uso de IA em contexto educacional;
8. discutem transformações no papel do professor, do aluno, da escola ou da avaliação por causa da IA;
9. são neutros ou ambivalentes, mas ainda tratam de uma questão axiologicamente relevante.

### 5.3 Quando marcar `applicability_score = 0`

Marque `applicability_score = 0` quando o post não oferece evidência suficiente para entrar na matriz.

Isso inclui posts que:

1. não tratam de IA e educação;
2. entram na coleta apenas por coincidência lexical;
3. são links soltos, spam, propaganda automática ou ruído;
4. apenas anunciam cursos, eventos, livros, notícias ou materiais sem valoração suficiente;
5. apenas listam informações;
6. apenas compartilham uma chamada vaga;
7. estão em idioma incompatível com o recorte da pesquisa e não fazem parte do debate analisado;
8. estão truncados ou dependem de contexto externo que não está no registro;
9. mencionam IA e educação sem orientar, avaliar, problematizar ou enquadrar o tema.

### 5.4 Diferença entre não aplicável e neutro aplicável

Esta é uma das regras mais importantes do manual.

`applicability_score = 0` significa:

> O post não entra na matriz.

`acceptance_5 = 0` significa:

> O post entra na matriz, mas não apresenta aceitação nem rejeição claras.

Portanto:

```text
não aplicável ≠ neutro
```

O rótulo `acceptance_5 = 0` não deve ser usado como depósito para qualquer post informativo. Ele só deve ser usado quando o post é aplicável à matriz, mas sua orientação é neutra, ambivalente, equilibrada ou descritiva dentro de um enquadramento axiologicamente relevante.

### 5.5 Exemplos de aplicabilidade

#### Exemplo 1: anúncio simples, tendência à exclusão

```text
Curso online sobre inteligência artificial para professores abre inscrições nesta semana.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justificativa: o post menciona IA e professores, mas funciona apenas como anúncio. Não há evidência suficiente de avaliação sobre IA na educação.

#### Exemplo 2: anúncio com enquadramento valorativo, tendência à inclusão

```text
Curso promete preparar professores para a revolução da inteligência artificial na sala de aula.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 3
}
```

Justificativa: o termo “revolução” e a ideia de preparação para mudança na sala de aula constroem enquadramento valorativo. A orientação tende a ser positiva ou prudente, com intensidade moderada.

#### Exemplo 3: chamada vaga, tendência à exclusão

```text
Como preparar a geração da inteligência artificial? Saiba o que muda na educação.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justificativa: se o registro contém apenas essa chamada, sem outro trecho avaliativo, o post pode ser tematicamente pertinente, mas axiologicamente insuficiente.

#### Exemplo 4: chamada jornalística com enquadramento valorativo, tendência à inclusão

```text
Revolução da inteligência artificial segundo Bill Gates: o futuro do ensino.

Bill Gates aposta que a inteligência artificial está prestes a transformar nossas vidas. Segundo ele, ferramentas de IA alcançarão níveis equivalentes aos dos professores.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

Justificativa: há enquadramento valorativo forte em “revolução”, “futuro do ensino”, “transformar nossas vidas” e “equivalentes aos dos professores”. Mesmo sendo uma chamada jornalística, o post constrói uma valoração positiva e intensa da IA na educação.

#### Exemplo 5: crítica a aluno usando IA

```text
Aluno entrega trabalho feito no ChatGPT e ainda acha que o professor não vai perceber.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

Justificativa: há crítica ao uso de IA em atividade escolar ou acadêmica. A orientação é negativa ou tecnocrítica. A intensidade é média, pois há julgamento claro, mas sem explosão retórica.

#### Exemplo 6: ironia crítica

```text
Vai, professor, manda os alunos usarem ChatGPT pra tudo. Vai dar super certo.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 4
}
```

Justificativa: a formulação literal parece incentivo, mas a orientação pragmática é irônica e crítica. A intensidade é alta pela ironia marcada.

#### Exemplo 7: informação neutra, mas aplicável

```text
Debate reúne professores e estudantes para discutir limites, riscos e possibilidades da inteligência artificial na educação.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 2
}
```

Justificativa: há pertinência axiológica porque o post explicita limites, riscos e possibilidades. Não há polaridade clara. A intensidade é baixa, pois o texto é descritivo e pouco enfático.

#### Exemplo 8: crítica não dirigida à IA

```text
O problema da educação brasileira é falta de investimento, não tecnologia.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justificativa: o post critica a educação brasileira, mas não há evidência suficiente de avaliação sobre IA na educação. Se o contexto coletado não menciona IA, não deve entrar na matriz.

## 6. Eixo de aceitação

A aceitação mede a orientação do post diante da IA na educação.

Ela responde à pergunta:

> O post rejeita, problematiza, aceita, defende ou suspende posição sobre IA na educação?

A aceitação deve ser atribuída em relação à IA na educação, não em relação a qualquer outro objeto. Um post pode criticar alunos, professores, empresas, governo, escola ou universidade. O anotador deve verificar se essa crítica é dirigida ao papel da IA na educação ou se a IA aparece apenas como elemento lateral.

### 6.1 `acceptance_5 = -2`: rejeição forte

Use `-2` quando o post enquadra a IA na educação como claramente nociva, destrutiva, inaceitável, ameaçadora ou algo a ser recusado.

Sinais comuns:

- linguagem catastrófica;
- pânico moral;
- denúncia forte;
- recusa explícita;
- ideia de destruição da educação;
- substituição de professores como ameaça;
- IA como fraude generalizada;
- IA como decadência intelectual;
- ataque direto ao uso educacional da IA.

Exemplos:

```text
ChatGPT na escola é o fim da educação. Estão ensinando os alunos a não pensar.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 5
}
```

```text
Se deixarem IA corrigir prova e orientar aluno, pode fechar a escola.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 4
}
```

### 6.2 `acceptance_5 = -1`: rejeição crítica ou tecnocrítica

Use `-1` quando o post expressa crítica, alerta, preocupação, resistência ou desconfiança em relação à IA na educação, mas sem rejeição extrema.

Sinais comuns:

- preocupação com uso inadequado;
- crítica a plágio ou fraude;
- alerta sobre aprendizagem;
- receio de dependência;
- crítica à adoção sem preparo;
- preocupação ética;
- crítica a políticas educacionais com IA;
- crítica ao uso por alunos ou professores em contexto específico.

Exemplos:

```text
O problema não é o ChatGPT existir. É aluno usar como atalho e a escola fingir que nada mudou.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

```text
Professor vai precisar repensar avaliação. Trabalho feito em casa com IA ficou complicado.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 2
}
```

### 6.3 `acceptance_5 = 0`: neutro, ambivalente ou equilibrado

Use `0` quando o post é aplicável, mas não apresenta predominância clara de aceitação ou rejeição.

Esse rótulo pode indicar:

- descrição de debate relevante;
- pergunta aberta;
- coexistência equilibrada de riscos e possibilidades;
- notícia com enquadramento axiológico, mas sem polaridade clara;
- ambivalência real;
- apresentação de posições diferentes sem adesão explícita.

Exemplos:

```text
Professores discutem como a inteligência artificial pode mudar avaliações, planejamento de aulas e aprendizagem dos alunos.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 2
}
```

```text
IA na educação: ferramenta de apoio ou risco para a aprendizagem?
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 3
}
```

Atenção: se o post apenas diz “evento sobre IA na educação hoje”, sem indicar debate, risco, possibilidade, transformação ou outro enquadramento, ele deve ser não aplicável, não neutro.

### 6.4 `acceptance_5 = 1`: aceitação prudente ou condicional

Use `1` quando o post reconhece valor, utilidade ou potencial da IA na educação, mas com alguma cautela, condição, mediação, limite ou preocupação.

Sinais comuns:

- IA como ferramenta de apoio;
- uso responsável;
- uso mediado por professor;
- necessidade de formação;
- defesa com ressalvas;
- potencial pedagógico sem entusiasmo extremo;
- aceitação condicionada a ética, regulação ou planejamento.

Exemplos:

```text
IA pode ajudar muito no planejamento das aulas, desde que o professor continue decidindo o caminho pedagógico.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 2
}
```

```text
ChatGPT pode ser bom para estudar, mas precisa de orientação. Sem professor, vira só resposta pronta.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 3
}
```

### 6.5 `acceptance_5 = 2`: aceitação forte ou tecnofílica

Use `2` quando o post enquadra a IA na educação como claramente benéfica, transformadora, desejável, inevitável ou superior.

Sinais comuns:

- entusiasmo forte;
- promessa de revolução educacional;
- IA como solução;
- IA como futuro inevitável e positivo;
- melhoria forte da aprendizagem;
- substituição ou equivalência apresentada como avanço;
- celebração explícita da tecnologia.

Exemplos:

```text
A inteligência artificial vai revolucionar a educação e finalmente personalizar o ensino para cada aluno.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

```text
Todo estudante deveria ter um tutor de IA. Isso muda completamente o jogo da aprendizagem.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

## 7. Eixo de intensidade

A intensidade mede a força avaliativa, retórica, afetiva ou enfática do post.

Ela responde à pergunta:

> Com que força textual a avaliação aparece?

A intensidade não mede se o post é positivo ou negativo. Ela mede o quão forte a valoração é construída.

### 7.1 O que conta como força textual

Considere como sinais de intensidade:

- adjetivos fortes;
- verbos de impacto;
- hipérboles;
- metáforas;
- ironia;
- sarcasmo;
- pontuação enfática;
- caixa alta;
- insultos;
- marcas de indignação;
- entusiasmo forte;
- medo;
- alarme;
- promessa de transformação;
- ameaça;
- generalizações radicais;
- oposição dramática;
- formulações performáticas.

### 7.2 O que não deve aumentar a intensidade sozinho

Não aumente a intensidade apenas porque:

- o tema é socialmente importante;
- o assunto é polêmico;
- você concorda ou discorda do post;
- o post fala de plágio, escola, professor ou aluno;
- o post menciona “revolução” de modo meramente convencional;
- o post é uma notícia sobre tema grave, mas escrita sem força textual.

A intensidade deve estar no texto, não na opinião do anotador sobre o tema.

### 7.3 `intensity_5 = 1`: intensidade muito baixa

Use `1` quando o post é predominantemente descritivo, informativo ou fracamente avaliativo.

Sinais comuns:

- linguagem neutra;
- ausência de emoção;
- ausência de ênfase;
- chamada simples;
- pergunta aberta sem carga forte;
- baixa presença de julgamento;
- vocabulário pouco marcado.

Exemplos:

```text
Pesquisadores discutem o uso de inteligência artificial em atividades educacionais.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 1
}
```

```text
Escola realiza conversa sobre inteligência artificial e aprendizagem.
```

Se houver apenas essa informação, a tendência pode ser exclusão. Se o post estiver dentro de um debate axiologicamente relevante, pode ser:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 1
}
```

### 7.4 `intensity_5 = 2`: intensidade baixa

Use `2` quando há avaliação perceptível, mas com pouca força.

Sinais comuns:

- leve crítica;
- leve apoio;
- preocupação discreta;
- defesa moderada;
- sugestão sem ênfase;
- vocabulário avaliativo fraco;
- ausência de marcas expressivas fortes.

Exemplos:

```text
Acho que IA pode ajudar professores, mas ainda precisa de muito cuidado.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 2
}
```

```text
Usar ChatGPT para estudar pode ser útil, mas não substitui leitura.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 2
}
```

### 7.5 `intensity_5 = 3`: intensidade média

Use `3` quando há avaliação clara e força argumentativa moderada.

Sinais comuns:

- crítica ou defesa clara;
- tese reconhecível;
- julgamento perceptível;
- preocupação ou entusiasmo moderados;
- enquadramento de risco ou benefício;
- formulação que ultrapassa a mera descrição.

Exemplos:

```text
O uso de IA na escola vai obrigar professores a repensarem avaliação. Fingir que nada mudou é erro.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

```text
A IA pode melhorar a aprendizagem, mas só se a escola formar professores para usar bem essas ferramentas.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 3
}
```

### 7.6 `intensity_5 = 4`: intensidade alta

Use `4` quando o post apresenta forte ênfase, ironia clara, julgamento marcado, indignação, entusiasmo forte ou carga afetiva evidente.

Sinais comuns:

- pontuação enfática;
- ironia marcada;
- vocabulário forte;
- metáforas de impacto;
- crítica incisiva;
- alarme;
- entusiasmo marcado;
- oposição forte;
- caixa alta pontual;
- formulação retoricamente carregada.

Exemplos:

```text
É assustador ver escola tratando ChatGPT como solução mágica para problema pedagógico.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 4
}
```

```text
A IA na educação não é detalhe técnico, é uma mudança profunda no jeito de ensinar e aprender.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 4
}
```

### 7.7 `intensity_5 = 5`: intensidade muito alta

Use `5` quando o post é extremo, ofensivo, catastrófico, alarmista, altamente emocional, celebratório em grau máximo ou retoricamente explosivo.

Sinais comuns:

- insulto;
- catastrofismo;
- pânico moral;
- ataque direto;
- exaltação extrema;
- generalização radical;
- ameaça extrema;
- promessa extrema;
- ironia muito agressiva;
- uso forte de caixa alta;
- múltiplas exclamações;
- formulação performática.

Exemplos:

```text
ChatGPT na escola é a morte do pensamento crítico. Estão destruindo a educação!!!
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 5
}
```

```text
IA vai salvar a educação brasileira!!! Todo aluno precisa disso agora!
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 5
}
```

## 8. Regras para casos difíceis

### 8.1 Posts jornalísticos, notícias e manchetes

Posts jornalísticos podem ser aplicáveis ou não.

Marque como não aplicável quando o post apenas informa, sem enquadramento valorativo suficiente.

Exemplo:

```text
Pesquisa sobre inteligência artificial na educação será apresentada nesta sexta.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Marque como aplicável quando a notícia ou manchete apresenta enquadramento avaliativo.

Exemplo:

```text
Inteligência artificial ameaça mudar o papel dos professores nas escolas.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

Exemplo:

```text
IA promete revolucionar a aprendizagem personalizada nas escolas.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

### 8.2 Links, cursos, eventos e divulgação

Posts de divulgação não são automaticamente aplicáveis.

Exemplo não aplicável:

```text
Inscrições abertas para palestra sobre IA e educação.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Exemplo aplicável:

```text
Palestra discute como a IA pode substituir práticas tradicionais de avaliação nas escolas.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 3
}
```

Justificativa: há enquadramento relevante sobre substituição de práticas avaliativas, embora a polaridade possa ficar aberta.

### 8.3 Ironia e sarcasmo

A ironia deve ser anotada pragmaticamente.

O anotador deve perguntar:

> O post quer dizer literalmente o que afirma ou está usando a formulação para criticar, ridicularizar ou inverter o sentido?

Exemplo:

```text
Claro, deixa o ChatGPT fazer o trabalho, a prova, a redação e já entrega o diploma também.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 4
}
```

Justificativa: a orientação pragmática é de rejeição forte ao uso indiscriminado de IA em atividades educacionais.

### 8.4 Alvo misto

Um post pode avaliar diferentes usos da IA de modo diferente.

Exemplo:

```text
IA para ajudar professor a planejar aula é ótimo. IA para aluno entregar trabalho pronto é outro problema.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 3
}
```

Justificativa: há aceitação de um uso e rejeição de outro. Se não houver predominância clara, use `acceptance_5 = 0`.

Quando houver alvo dominante, anote a orientação dominante.

Exemplo:

```text
Até pode ajudar no planejamento, mas na prática o ChatGPT virou máquina de plágio escolar.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 4
}
```

Justificativa: apesar da concessão inicial, a orientação dominante é negativa.

### 8.5 Crítica ao aluno, professor ou instituição

Nem toda crítica ao aluno, professor, escola ou governo é crítica à IA na educação.

Exemplo:

```text
Aluno não lê nada e depois reclama da prova.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Exemplo aplicável:

```text
Aluno não lê nada, joga tudo no ChatGPT e chama isso de estudar.
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

Justificativa: a crítica se dirige ao uso de IA em prática educacional.

### 8.6 Português de Portugal e outros idiomas

Posts em português europeu não devem ser excluídos automaticamente. Se o post é compreensível, trata de IA e educação, e apresenta enquadramento avaliativo, ele pode ser anotado.

Posts em outro idioma devem ser excluídos quando não fizerem parte do recorte linguístico da pesquisa ou quando entrarem por coincidência lexical.

Exemplo:

```text
Professor explains how AI tools can help students write essays.
```

Anotação provável:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justificativa: está em inglês e fora do recorte linguístico principal, salvo decisão metodológica em contrário.

### 8.7 Duplicatas

Quando o mesmo texto aparece duplicado na mesma fonte, ele deve ser deduplicado antes da análise final.

Quando textos iguais aparecem em fontes diferentes ou em contextos diferentes, eles podem ser mantidos, mas devem receber anotação consistente, salvo se o contexto textual disponível no registro alterar claramente a interpretação.

Se duplicatas tiverem anotações divergentes, devem ser revisadas na adjudicação.

### 8.8 Texto truncado ou incompleto

Se o texto estiver truncado, mas ainda houver evidência suficiente para anotação, anote normalmente.

Exemplo:

```text
A IA vai transformar completamente a sala de aula, mas professores...
```

Anotação provável:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 4
}
```

Justificativa: apesar do truncamento, há enquadramento valorativo claro.

Se o texto truncado não permitir inferência segura, marque como não aplicável.

## 9. Quadro rápido de decisão

| Situação | Aplicabilidade | Aceitação | Intensidade |
|---|---:|---:|---:|
| Link solto sobre IA e educação | 0 | null | null |
| Curso ou evento sem avaliação | 0 | null | null |
| Curso que promete “revolução” na educação | 1 | 1 ou 2 | 3 ou 4 |
| Notícia neutra sem enquadramento | 0 | null | null |
| Notícia com “ameaça”, “risco”, “substituição” | 1 | -1 ou -2 | 3 a 5 |
| Debate sobre riscos e possibilidades | 1 | 0 | 2 ou 3 |
| Ironia contra ChatGPT em trabalhos escolares | 1 | -1 ou -2 | 4 ou 5 |
| Defesa de IA com ressalvas pedagógicas | 1 | 1 | 2 ou 3 |
| Celebração forte de IA como futuro da educação | 1 | 2 | 4 ou 5 |
| Crítica à escola sem relação com IA | 0 | null | null |
| Crítica ao uso de IA por alunos | 1 | -1 ou -2 | 2 a 5 |

## 10. Mapeamento para 3 classes

A anotação principal é feita em 5 níveis. A versão em 3 classes é derivada automaticamente.

### 10.1 Aceitação em 3 classes

| `acceptance_5` | `acceptance_3` | Rótulo |
|---:|---:|---|
| -2 | -1 | negativo |
| -1 | -1 | negativo |
| 0 | 0 | neutro |
| 1 | 1 | positivo |
| 2 | 1 | positivo |

### 10.2 Intensidade em 3 classes

O mapeamento operacional atual é:

| `intensity_5` | `intensity_3` | Rótulo |
|---:|---:|---|
| 1 | 0 | baixa |
| 2 | 1 | média |
| 3 | 1 | média |
| 4 | 2 | alta |
| 5 | 2 | alta |

Justificativa operacional: o nível 1 representa descrição ou força muito baixa; os níveis 2 e 3 concentram avaliação perceptível, mas ainda não fortemente marcada; os níveis 4 e 5 concentram formulações com força retórica, afetiva ou enfática alta.

Observação metodológica: esse mapeamento deve ser auditado empiricamente por distribuição de classes e acordo entre anotadores. Caso outro mapeamento apresente maior estabilidade sem prejudicar a interpretação linguística, ele pode ser adotado em versão posterior.

## 11. Protocolo de adjudicação

A adjudicação deve ser feita depois da anotação independente.

A ordem recomendada de revisão é:

1. conflitos de aplicabilidade;
2. conflitos entre não aplicável e neutro aplicável;
3. conflitos de aceitação em 3 classes;
4. conflitos de intensidade em 3 classes;
5. diferenças finas grandes, por exemplo delta maior ou igual a 2;
6. duplicatas inconsistentes;
7. casos de ironia, sarcasmo ou manchete com enquadramento forte.

A adjudicação não deve buscar “quem acertou” de forma abstrata. Ela deve perguntar:

> Qual regra do manual decide este caso?

O registro adjudicado deve indicar a decisão final e, quando possível, a regra usada.

Exemplo:

```json
{
  "item_id": 1,
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3,
  "acceptance_3": -1,
  "intensity_3": 1,
  "adjudication_status": "adjudicated",
  "adjudication_rule": "R4_IRONY_PRAGMATIC_ORIENTATION"
}
```

## 12. Protocolo cego para validação manual de corpus externo

Quando o manual for usado para validar uma amostra de corpus externo, como posts de 2024, a anotação deve ser cega.

O anotador deve receber apenas:

```text
item_id
text
manual_applicability
manual_acceptance_5
manual_intensity_5
manual_notes
```

O anotador não deve ver predições dos modelos supervisionados ou do LLM durante a anotação. As predições devem ser comparadas apenas depois da anotação manual.

Essa regra evita que a validação vire revisão assistida pelo modelo.

## 13. Checklist final para o anotador

Antes de finalizar cada item, verifique:

1. O post realmente trata de IA e educação?
2. Há evidência textual de valoração?
3. Se não houver, marque como não aplicável.
4. Se houver, a orientação é negativa, neutra/ambivalente ou positiva?
5. A crítica ou defesa é realmente sobre IA na educação?
6. A intensidade está baseada em marcas do texto, não na gravidade do tema?
7. Há ironia?
8. O post depende de link externo ou contexto não disponível?
9. O rótulo `0` foi usado como neutro aplicável, e não como depósito de post informativo?
10. Se a anotação parece forçada, provavelmente o post deve ser não aplicável.

## 14. Formulação curta para a metodologia do artigo

A seguinte formulação resume o protocolo:

> Definimos a aplicabilidade como um critério decisório de entrada na matriz, não como um eixo de classificação. Um post é incluído apenas quando apresenta evidência textual suficiente de enquadramento avaliativo sobre IA na educação. Menções puramente temáticas, links soltos, anúncios neutros e chamadas sem valoração suficiente são excluídos. Quando um post é aplicável, mas não apresenta polaridade clara, ele recebe aceitação neutra. A intensidade é anotada separadamente e representa a força avaliativa, retórica ou afetiva observável no texto.

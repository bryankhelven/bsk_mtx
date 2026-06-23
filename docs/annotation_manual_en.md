# Axiological Annotation Manual v2.0
## AI and Education in Bluesky Posts

## 1. Purpose of the manual

This manual guides the axiological annotation of Bluesky posts about artificial intelligence and education. The goal of the annotation is to identify when a post presents an evaluative framing of AI in education and, when such framing exists, to position the post in a matrix formed by two axes: **acceptance** and **intensity**.

The task is not to classify every post that mentions “AI”, “ChatGPT”, “teacher”, “student”, or “education”. The lexical presence of these terms is only a starting point for data collection. The annotation itself requires an interpretive decision: checking whether the post provides enough textual evidence to be placed in an axiological matrix.

The annotation must answer, in this order:

1. Is the post applicable to the axiological matrix?
2. If it is applicable, what is its acceptance orientation toward AI in education?
3. If it is applicable, what is its evaluative intensity?

The expected final structure for an applicable post is:

```json
{
  "item_id": 1,
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

The expected final structure for a non-applicable post is:

```json
{
  "item_id": 1,
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

## 2. Annotation unit

The annotation unit is the **collected post**.

The annotator must use only the textual information available in the collected record. This includes the post text and, when present in the record itself, visible snippets of a headline, quote, repost, or textual link preview. The annotator must not open external links, inspect the user profile, investigate the author’s intention outside the post, or search for additional context on the internet.

When the post is truncated, incomplete, or dependent on missing context, the annotator must decide whether there is still enough textual evidence for annotation. If there is not, the post must be marked as non-applicable.

## 3. Overview of the task

The annotation is hierarchical.

First, the annotator decides **applicability**. This step determines whether the post enters the matrix. Then, only for applicable posts, the two matrix axes are annotated:

| Step | Field | Values | Function |
|---|---|---:|---|
| 1 | `applicability_score` | 0 or 1 | Decides whether the post enters the matrix |
| 2 | `acceptance_5` | -2, -1, 0, 1, 2 | Measures the orientation toward AI in education |
| 3 | `intensity_5` | 1, 2, 3, 4, 5 | Measures the evaluative, rhetorical, or affective force of the post |

Applicability is **not an axis of the matrix**. It is a decision criterion. The matrix is formed only by the acceptance and intensity axes.

## 4. Annotation decision tree

Before assigning any label, follow this sequence.

### Step 1: does the post address AI and education?

Ask:

> Does the post refer, directly or indirectly, to artificial intelligence, generative AI, ChatGPT, LLMs, or similar tools in an educational context?

If the answer is **no**, assign:

```json
"applicability_score": 0
```

If the answer is **yes**, go to step 2.

### Step 2: is there evaluative framing?

Ask:

> Does the post present criticism, defense, concern, enthusiasm, promise, threat, irony, judgment, risk, benefit, transformation, solution, denunciation, fear, warning, or another form of valuation about AI in education?

If the answer is **no**, assign:

```json
"applicability_score": 0
```

If the answer is **yes**, go to step 3.

### Step 3: is the orientation negative, neutral/ambivalent, or positive?

Ask:

> Does the post tend to reject, accept, or suspend a clear position about AI in education?

The answer defines `acceptance_5`.

### Step 4: is the textual force low, medium, or high?

Ask:

> Does the valuation appear weakly, moderately, strongly, or extremely in the text?

The answer defines `intensity_5`.

## 5. Applicability decision criterion

### 5.1 Central rule

A post is applicable only when it provides enough textual evidence to be positioned in the axiological matrix.

The simultaneous presence of AI and education terms **is not enough**.

The decisive question is:

> Is there any form of valuation of AI in education in this post?

This valuation may be explicit or attributed to another source. It may appear through a direct opinion, a criticism, a defense, a promise, a threat, a journalistic framing, irony, metaphor, or evaluative vocabulary.

### 5.2 When to assign `applicability_score = 1`

Assign `applicability_score = 1` when the post addresses AI and education and allows a minimally justified axiological reading.

This includes posts that:

1. criticize the use of AI by students, teachers, schools, universities, or institutions;
2. defend or celebrate the use of AI in teaching, learning, assessment, planning, or training;
3. point to risks, threats, harms, fraud, plagiarism, dependency, inequality, or precarization;
4. point to benefits, innovation, pedagogical support, personalization, productivity, or learning improvement;
5. attribute an evaluative position about AI in education to someone;
6. use headlines, calls, or journalistic terms with clear evaluative framing;
7. present irony or sarcasm about the use of AI in educational contexts;
8. discuss transformations in the role of the teacher, the student, the school, or assessment because of AI;
9. are neutral or ambivalent, but still address an axiologically relevant issue.

### 5.3 When to assign `applicability_score = 0`

Assign `applicability_score = 0` when the post does not provide enough evidence to enter the matrix.

This includes posts that:

1. do not actually address AI and education;
2. enter the collection only through lexical coincidence;
3. are isolated links, spam, automated advertising, or noise;
4. only announce courses, events, books, news, or materials without sufficient valuation;
5. only list information;
6. only share a vague call or headline;
7. are in a language incompatible with the research scope and do not belong to the analyzed debate;
8. are truncated or depend on external context that is not available in the record;
9. mention AI and education without orienting, evaluating, problematizing, or framing the topic.

### 5.4 Difference between non-applicable and neutral applicable

This is one of the most important rules in the manual.

`applicability_score = 0` means:

> The post does not enter the matrix.

`acceptance_5 = 0` means:

> The post enters the matrix, but does not present clear acceptance or rejection.

Therefore:

```text
non-applicable ≠ neutral
```

The label `acceptance_5 = 0` must not be used as a storage label for any informative post. It should only be used when the post is applicable to the matrix, but its orientation is neutral, ambivalent, balanced, or descriptive within an axiologically relevant framing.

### 5.5 Applicability examples

#### Example 1: simple announcement, likely exclusion

```text
Online course on artificial intelligence for teachers opens registration this week.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justification: the post mentions AI and teachers, but functions only as an announcement. There is not enough evidence of evaluation about AI in education.

#### Example 2: announcement with evaluative framing, likely inclusion

```text
Course promises to prepare teachers for the artificial intelligence revolution in the classroom.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 3
}
```

Justification: the term “revolution” and the idea of preparation for classroom change construct evaluative framing. The orientation tends to be positive or prudent, with moderate intensity.

#### Example 3: vague call, likely exclusion

```text
How should we prepare the generation of artificial intelligence? Learn what changes in education.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justification: if the record contains only this call, without another evaluative excerpt, the post may be thematically relevant, but axiologically insufficient.

#### Example 4: journalistic call with evaluative framing, likely inclusion

```text
The artificial intelligence revolution according to Bill Gates: the future of teaching.

Bill Gates believes that artificial intelligence is about to transform our lives. According to him, AI tools will reach levels equivalent to those of teachers.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

Justification: there is strong evaluative framing in “revolution”, “future of teaching”, “transform our lives”, and “equivalent to teachers”. Even though it is a journalistic call, the post constructs a positive and intense valuation of AI in education.

#### Example 5: criticism of a student using AI

```text
A student submits an assignment made with ChatGPT and still thinks the teacher will not notice.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

Justification: there is criticism of AI use in a school or academic activity. The orientation is negative or technocritical. The intensity is medium, since there is clear judgment, but no rhetorical explosion.

#### Example 6: critical irony

```text
Sure, teacher, tell students to use ChatGPT for everything. It will work out great.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 4
}
```

Justification: the literal formulation sounds like encouragement, but the pragmatic orientation is ironic and critical. The intensity is high because of the marked irony.

#### Example 7: neutral information, but applicable

```text
Debate brings together teachers and students to discuss limits, risks, and possibilities of artificial intelligence in education.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 2
}
```

Justification: there is axiological relevance because the post explicitly mentions limits, risks, and possibilities. There is no clear polarity. The intensity is low because the text is descriptive and not strongly emphatic.

#### Example 8: criticism not directed at AI

```text
The problem of Brazilian education is lack of investment, not technology.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justification: the post criticizes Brazilian education, but there is not enough evidence of evaluation about AI in education. If the collected context does not mention AI, it should not enter the matrix.

## 6. Acceptance axis

Acceptance measures the orientation of the post toward AI in education.

It answers the question:

> Does the post reject, problematize, accept, defend, or suspend a position about AI in education?

Acceptance must be assigned in relation to AI in education, not in relation to any other object. A post may criticize students, teachers, companies, government, schools, or universities. The annotator must check whether this criticism is directed at the role of AI in education or whether AI only appears as a side element.

### 6.1 `acceptance_5 = -2`: strong rejection

Use `-2` when the post frames AI in education as clearly harmful, destructive, unacceptable, threatening, or something to be refused.

Common signs:

- catastrophic language;
- moral panic;
- strong denunciation;
- explicit refusal;
- idea of destruction of education;
- replacement of teachers as threat;
- AI as generalized fraud;
- AI as intellectual decay;
- direct attack on educational use of AI.

Examples:

```text
ChatGPT in school is the end of education. They are teaching students not to think.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 5
}
```

```text
If they let AI grade exams and guide students, we might as well close the school.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 4
}
```

### 6.2 `acceptance_5 = -1`: critical or technocritical rejection

Use `-1` when the post expresses criticism, warning, concern, resistance, or distrust toward AI in education, but without extreme rejection.

Common signs:

- concern about inappropriate use;
- criticism of plagiarism or fraud;
- warning about learning;
- fear of dependency;
- criticism of adoption without preparation;
- ethical concern;
- criticism of educational policies involving AI;
- criticism of use by students or teachers in a specific context.

Examples:

```text
The problem is not that ChatGPT exists. It is students using it as a shortcut and schools pretending nothing has changed.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

```text
Teachers will need to rethink assessment. Homework done with AI has become complicated.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 2
}
```

### 6.3 `acceptance_5 = 0`: neutral, ambivalent, or balanced

Use `0` when the post is applicable, but does not show a clear predominance of acceptance or rejection.

This label may indicate:

- description of a relevant debate;
- open question;
- balanced coexistence of risks and possibilities;
- news with axiological framing, but no clear polarity;
- real ambivalence;
- presentation of different positions without explicit adherence.

Examples:

```text
Teachers discuss how artificial intelligence may change assessment, lesson planning, and student learning.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 2
}
```

```text
AI in education: support tool or risk to learning?
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 3
}
```

Attention: if the post only says “event on AI in education today”, without indicating debate, risk, possibility, transformation, or another framing, it should be non-applicable, not neutral.

### 6.4 `acceptance_5 = 1`: prudent or conditional acceptance

Use `1` when the post recognizes value, usefulness, or potential in AI in education, but with some caution, condition, mediation, limit, or concern.

Common signs:

- AI as a support tool;
- responsible use;
- use mediated by teachers;
- need for training;
- defense with reservations;
- pedagogical potential without extreme enthusiasm;
- acceptance conditioned on ethics, regulation, or planning.

Examples:

```text
AI can help a lot with lesson planning, as long as the teacher continues to decide the pedagogical path.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 2
}
```

```text
ChatGPT can be useful for studying, but it needs guidance. Without a teacher, it becomes just ready-made answers.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 3
}
```

### 6.5 `acceptance_5 = 2`: strong or technophilic acceptance

Use `2` when the post frames AI in education as clearly beneficial, transformative, desirable, inevitable, or superior.

Common signs:

- strong enthusiasm;
- promise of educational revolution;
- AI as solution;
- AI as inevitable and positive future;
- strong improvement of learning;
- replacement or equivalence presented as progress;
- explicit celebration of technology.

Examples:

```text
Artificial intelligence will revolutionize education and finally personalize teaching for every student.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

```text
Every student should have an AI tutor. This completely changes the game of learning.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

## 7. Intensity axis

Intensity measures the evaluative, rhetorical, affective, or emphatic force of the post.

It answers the question:

> With what textual force does the evaluation appear?

Intensity does not measure whether the post is positive or negative. It measures how strongly the valuation is constructed.

### 7.1 What counts as textual force

Consider the following as signs of intensity:

- strong adjectives;
- impact verbs;
- hyperbole;
- metaphors;
- irony;
- sarcasm;
- emphatic punctuation;
- uppercase;
- insults;
- signs of indignation;
- strong enthusiasm;
- fear;
- alarm;
- promise of transformation;
- threat;
- radical generalizations;
- dramatic opposition;
- performative formulations.

### 7.2 What should not increase intensity by itself

Do not increase intensity only because:

- the topic is socially important;
- the topic is controversial;
- you agree or disagree with the post;
- the post mentions plagiarism, school, teacher, or student;
- the post mentions “revolution” in a merely conventional way;
- the post is news about a serious topic, but written without textual force.

Intensity must be in the text, not in the annotator’s opinion about the topic.

### 7.3 `intensity_5 = 1`: very low intensity

Use `1` when the post is predominantly descriptive, informative, or weakly evaluative.

Common signs:

- neutral language;
- absence of emotion;
- absence of emphasis;
- simple call or headline;
- open question without strong load;
- low presence of judgment;
- weakly marked vocabulary.

Examples:

```text
Researchers discuss the use of artificial intelligence in educational activities.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 1
}
```

```text
School holds a conversation about artificial intelligence and learning.
```

If there is only this information, the likely tendency may be exclusion. If the post is within an axiologically relevant debate, it may be:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 1
}
```

### 7.4 `intensity_5 = 2`: low intensity

Use `2` when there is perceptible evaluation, but with little force.

Common signs:

- mild criticism;
- mild support;
- discreet concern;
- moderate defense;
- suggestion without emphasis;
- weak evaluative vocabulary;
- absence of strong expressive marks.

Examples:

```text
I think AI can help teachers, but it still requires a lot of care.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 2
}
```

```text
Using ChatGPT to study can be useful, but it does not replace reading.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 2
}
```

### 7.5 `intensity_5 = 3`: medium intensity

Use `3` when there is clear evaluation and moderate argumentative force.

Common signs:

- clear criticism or defense;
- recognizable thesis;
- perceptible judgment;
- moderate concern or enthusiasm;
- framing of risk or benefit;
- formulation that goes beyond mere description.

Examples:

```text
The use of AI in school will force teachers to rethink assessment. Pretending nothing has changed is a mistake.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

```text
AI can improve learning, but only if schools train teachers to use these tools well.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 3
}
```

### 7.6 `intensity_5 = 4`: high intensity

Use `4` when the post presents strong emphasis, clear irony, marked judgment, indignation, strong enthusiasm, or evident affective load.

Common signs:

- emphatic punctuation;
- marked irony;
- strong vocabulary;
- impactful metaphors;
- incisive criticism;
- alarm;
- marked enthusiasm;
- strong opposition;
- occasional uppercase;
- rhetorically loaded formulation.

Examples:

```text
It is frightening to see schools treating ChatGPT as a magical solution to a pedagogical problem.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 4
}
```

```text
AI in education is not a technical detail, it is a profound change in the way we teach and learn.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 4
}
```

### 7.7 `intensity_5 = 5`: very high intensity

Use `5` when the post is extreme, offensive, catastrophic, alarmist, highly emotional, maximally celebratory, or rhetorically explosive.

Common signs:

- insult;
- catastrophism;
- moral panic;
- direct attack;
- extreme exaltation;
- radical generalization;
- extreme threat;
- extreme promise;
- very aggressive irony;
- strong use of uppercase;
- multiple exclamation marks;
- performative formulation.

Examples:

```text
ChatGPT in school is the death of critical thinking. They are destroying education!!!
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 5
}
```

```text
AI will save Brazilian education!!! Every student needs this now!
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 5
}
```

## 8. Rules for difficult cases

### 8.1 Journalistic posts, news, and headlines

Journalistic posts may be applicable or non-applicable.

Mark as non-applicable when the post only informs, without sufficient evaluative framing.

Example:

```text
Research on artificial intelligence in education will be presented this Friday.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Mark as applicable when the news or headline presents evaluative framing.

Example:

```text
Artificial intelligence threatens to change the role of teachers in schools.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

Example:

```text
AI promises to revolutionize personalized learning in schools.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 2,
  "intensity_5": 4
}
```

### 8.2 Links, courses, events, and promotional posts

Promotional posts are not automatically applicable.

Non-applicable example:

```text
Registration open for lecture on AI and education.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Applicable example:

```text
Lecture discusses how AI may replace traditional assessment practices in schools.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 3
}
```

Justification: there is relevant framing around the replacement of assessment practices, although polarity may remain open.

### 8.3 Irony and sarcasm

Irony must be annotated pragmatically.

The annotator must ask:

> Does the post literally mean what it says, or is it using the formulation to criticize, ridicule, or invert the meaning?

Example:

```text
Of course, let ChatGPT do the assignment, the exam, the essay, and just hand over the diploma too.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -2,
  "intensity_5": 4
}
```

Justification: the pragmatic orientation is strong rejection of indiscriminate AI use in educational activities.

### 8.4 Mixed target

A post may evaluate different uses of AI in different ways.

Example:

```text
AI to help teachers plan lessons is great. AI for students to submit ready-made assignments is another problem.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 0,
  "intensity_5": 3
}
```

Justification: there is acceptance of one use and rejection of another. If there is no clear predominance, use `acceptance_5 = 0`.

When there is a dominant target, annotate the dominant orientation.

Example:

```text
It may help with planning, but in practice ChatGPT has become a school plagiarism machine.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 4
}
```

Justification: despite the initial concession, the dominant orientation is negative.

### 8.5 Criticism of the student, teacher, or institution

Not every criticism of students, teachers, schools, or government is criticism of AI in education.

Example:

```text
The student does not read anything and then complains about the exam.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Applicable example:

```text
The student does not read anything, throws everything into ChatGPT, and calls that studying.
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": -1,
  "intensity_5": 3
}
```

Justification: the criticism targets AI use in an educational practice.

### 8.6 European Portuguese and other languages

Posts in European Portuguese should not be automatically excluded. If the post is understandable, addresses AI and education, and presents evaluative framing, it may be annotated.

Posts in another language must be excluded when they do not belong to the linguistic scope of the research or when they enter through lexical coincidence.

Example:

```text
Professor explains how AI tools can help students write essays.
```

Likely annotation:

```json
{
  "applicability_score": 0,
  "acceptance_5": null,
  "intensity_5": null
}
```

Justification: it is in English and outside the main linguistic scope, unless the methodology explicitly decides otherwise.

### 8.7 Duplicates

When the same text appears duplicated from the same source, it must be deduplicated before final analysis.

When identical texts appear from different sources or in different contexts, they may be kept, but should receive consistent annotation unless the textual context available in the record clearly changes the interpretation.

If duplicates have divergent annotations, they must be reviewed during adjudication.

### 8.8 Truncated or incomplete text

If the text is truncated, but there is still enough evidence for annotation, annotate normally.

Example:

```text
AI will completely transform the classroom, but teachers...
```

Likely annotation:

```json
{
  "applicability_score": 1,
  "acceptance_5": 1,
  "intensity_5": 4
}
```

Justification: despite truncation, there is clear evaluative framing.

If the truncated text does not allow a safe inference, mark it as non-applicable.

## 9. Quick decision table

| Situation | Applicability | Acceptance | Intensity |
|---|---:|---:|---:|
| Isolated link about AI and education | 0 | null | null |
| Course or event without evaluation | 0 | null | null |
| Course that promises a “revolution” in education | 1 | 1 or 2 | 3 or 4 |
| Neutral news without framing | 0 | null | null |
| News with “threat”, “risk”, “replacement” | 1 | -1 or -2 | 3 to 5 |
| Debate on risks and possibilities | 1 | 0 | 2 or 3 |
| Irony against ChatGPT in schoolwork | 1 | -1 or -2 | 4 or 5 |
| Defense of AI with pedagogical reservations | 1 | 1 | 2 or 3 |
| Strong celebration of AI as the future of education | 1 | 2 | 4 or 5 |
| Criticism of school unrelated to AI | 0 | null | null |
| Criticism of students’ use of AI | 1 | -1 or -2 | 2 to 5 |

## 10. Mapping to 3 classes

The main annotation is done in 5 levels. The 3-class version is derived automatically.

### 10.1 Acceptance in 3 classes

| `acceptance_5` | `acceptance_3` | Label |
|---:|---:|---|
| -2 | -1 | negative |
| -1 | -1 | negative |
| 0 | 0 | neutral |
| 1 | 1 | positive |
| 2 | 1 | positive |

### 10.2 Intensity in 3 classes

The current operational mapping is:

| `intensity_5` | `intensity_3` | Label |
|---:|---:|---|
| 1 | 0 | low |
| 2 | 1 | medium |
| 3 | 1 | medium |
| 4 | 2 | high |
| 5 | 2 | high |

Operational justification: level 1 represents description or very low force; levels 2 and 3 concentrate perceptible evaluation, but not yet strongly marked evaluation; levels 4 and 5 concentrate formulations with high rhetorical, affective, or emphatic force.

Methodological note: this mapping must be empirically audited through class distribution and inter-annotator agreement. If another mapping shows greater stability without harming the linguistic interpretation, it may be adopted in a later version.

## 11. Adjudication protocol

Adjudication must be done after independent annotation.

The recommended review order is:

1. applicability conflicts;
2. conflicts between non-applicable and neutral applicable;
3. acceptance conflicts in 3 classes;
4. intensity conflicts in 3 classes;
5. large fine-grained differences, for example delta greater than or equal to 2;
6. inconsistent duplicates;
7. cases of irony, sarcasm, or headlines with strong framing.

Adjudication should not seek to decide “who is right” in an abstract sense. It should ask:

> Which rule of the manual decides this case?

The adjudicated record must indicate the final decision and, when possible, the rule used.

Example:

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

## 12. Blind protocol for manual validation of an external corpus

When the manual is used to validate a sample from an external corpus, such as 2024 posts, the annotation must be blind.

The annotator should receive only:

```text
item_id
text
manual_applicability
manual_acceptance_5
manual_intensity_5
manual_notes
```

The annotator must not see predictions from supervised models or the LLM during annotation. Predictions must be compared only after manual annotation.

This rule prevents validation from becoming model-assisted review.

## 13. Final checklist for the annotator

Before finalizing each item, check:

1. Does the post actually address AI and education?
2. Is there textual evidence of valuation?
3. If there is no such evidence, mark it as non-applicable.
4. If there is evidence, is the orientation negative, neutral/ambivalent, or positive?
5. Is the criticism or defense really about AI in education?
6. Is intensity based on textual marks, not on the seriousness of the topic?
7. Is there irony?
8. Does the post depend on an external link or unavailable context?
9. Was the label `0` used as neutral applicable, not as a storage label for informative posts?
10. If the annotation feels forced, the post probably should be non-applicable.

## 14. Short formulation for the paper methodology

The following formulation summarizes the protocol:

> We define applicability as a decision criterion for entry into the matrix, not as a classification axis. A post is included only when it presents enough textual evidence of evaluative framing about AI in education. Purely topical mentions, isolated links, neutral announcements, and calls without sufficient valuation are excluded. When a post is applicable but does not present clear polarity, it receives neutral acceptance. Intensity is annotated separately and represents the evaluative, rhetorical, or affective force observable in the text.

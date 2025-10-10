---
layout: post
title: "Building Agents"
tags: [wip]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

### 28sep2025
 - Built a mini personal finance APP the plan is to build a agent system around it.
 - Personal Finance APP
 - Agents around it

### 29sep2025
  - Create GPT 
    - Prompt engineering
    - How I created a  prompt for finanicial expert with the help of chat gpt
  - Multi agent system
    - Evolution
    - What I've done
    - Pros & Cons

### 01oct2025
  It is regular wednessday morning, I brought air fried chicken thighs to the table, it is still hot and fumes out of it. My son stared it and started eating by saying that seasoning has to be spread evenly. I said let me know the taste. After tasting the edge he said that It is good. I repeated you want the seasoning to spread, he noded. "I've noted it" I replied.

  Immediately I was wondering how my brian stores that information,
    - home cooking
      - which is healthy
      - Felt relieved (without cooking my son was surviving with his friends support.)
      - better economy choice
    - gratified to prepare breakfast my son

  I said that I'm storing this message with all these context like a vector DB, then Iniyan replied that vector DB might got inspiration from how human memory works.


### 02oct2025

  As I'm building parallel App for personal finance, going through a shift of mindset from traditional way of app building vs hybrid approach on app build.



| Traditional APP building                 | Agent + LLM supported APP building                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------ |
| 100% Business logic managed by developer | Hybrid approach both developer and agent                                       |
| logic in functions                       | logic in functions : but while calling function, parameters are decided by LLM |
| logic in config files                    | which config to choose can be decided from LLM                                 |
| logic in database                        | very good possibility that , logic in database could be updated from LLM       |



### 03oct2025
  - What is plugin ?
  - What is semantic plugin ?
  - What is SK ?
    - SK is the orchestrator of API tool calls, aka plugins
    - SK      `Functional Module` --> `Skills`
    - Open Ai `Skills` --> `Plugins`
    - SK is useful too for managing multiple plugins (actions for agents)
    - Why do you need SK ? how SK is diff from promptflow ?
  - What is `semantic function`
    - `semantic function` encapsulate a prompt/profile and execute through interaction with an LLM

  - > WHOLE AI : sounds me like searching structure from un structure or randomness
  - > Is there a need for Tableau , how can it be replaced by an Agent ?

### 04oct2025
- Today played around a playground to run ABTs which leverages py_tree .
- Concepts to explore further
  - How to apply Behaviour Tree ? What is Agentic Behaviour Tree ?
  - How to leverage  Playground to test ABT ?

### 05oct2025
- Various other concepts similar to Behaviour Tree

### 06oct2025
- How do you reduce token usage ?
  - By split a document and use only the relevant parts .
- I was talking to you a student, who is trying to learn agentic AI, following is the conversation
  - student : have you seen the github repo of semantic kernel referred in "AI agents in action"
  - myself:   do you mean the repo created by the author ?
  - student : No microsoft's official repo `context`
  - myself  : Oh yeah, whats in it ?
  - student : It has some c programs ?
  - myself  : probably why do you ask ? is it causes you stuck ?
  - student : out of curiosity ? `context`
- Got good idea on RAG and RAGR
  - RAGR - Retrive Augment Generate & Remember
    - Retrive
      - from knowledge (vector db)  - semantic search
      - from memory (postgresql )   - plugins

### 07oct2025
- why do you need PCA ?
- How do you reduce dimension ?
- Splitting documents
  - 100 char chunks (split into semantically meaningful chunks)
  - Tokenization (split each word)
- Got good idea on memory
  - RAG vs RAGR
  - embedding 
    - TF-IDF
    - Language model based embedding
  - Storage
    - vector store 
    - vector DB (In memory vs dedicated )
    - vector DB extension
  - spliting
    - Langchain based splitting, chunk size and overlap ( used not to loose meaning)
  - Memory structure
    - Sensory
      - Iconic
      - Auditory
      - haptic
    - Short term or context : conversational
    - Long term memory
      - conscious (explicit/declarative)
        - episodic ( eg : events)
        - semantic ( facts )
      - unconscious ( implicit / procedural )
        - skills
### 08oct2025
- Agent profile
  - This includes following things about an agent
    - persona
    - memory,knowledge
    - functions & plugins
    - planning
    - Evaluation & Feed back
- why do you need promptflow ?
    - To run and archestrate agents
- What is a promptflow
  - input --> prompt (in jinja2 ) --> evaluate (.py) --> output
### 09oct
- Axes 
  - Y - Thinking ( allow time to think)
  - X - Reasoning 
- Reasoning process 
  - Solutions
    - Q & A prompting
    - one shot prompting
    - zero shot prompting
  - Reasoning
    - COT (Chain of Thought prompting)
    - PC (Prompt Chaining )
  - Evaluation
    - Self-consistency prompting 
    - TOT (Tree of Thought prompting)
- Why there are 3 reasoning process
  - It is hierachy for simple problems you get solution in direction solutioning, few go for reasoning other complex ones go until Evaluation
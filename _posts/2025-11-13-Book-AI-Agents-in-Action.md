---
layout: post
title: "Book review : AI Agents Action"
tags: [wip]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

As the era of Agents has started, wanted master AI Agents by building a customer facing APP ( started using by myself and my family), after skim through few books landed on this book <b>AI Agents in Action<b/>  by <b>Micheal Lanham.</b> After reading this book for 2 iteration and working on examples, I came to a conclusion this is best book to learn AI Agents and build it for practical purpose.

#### Overview of the book

- He starts with amazing introduction of AI Agent, defining an agent in a rational way, with this I start looking an agent as a person like. It (let me use the pronuoun "It" as of 2025) has a personanlity or persona. It can remember facts and mastery(is it a tool).It has tools to use . it can reason and eveluate. It can plan and take feedback. #TODO Include a picture by mapping Figure 1.3 mapped with tools. Author gives motivation how an agent era would look like  #Exand it
- As LLM is backbone nope, a genie knows almost everything what human kind gathered , if you talk to him in his language (Prompting), you would get right answer 90% of the time . Author gives famous LLMs , how to interact with it through API . How to run local LLMs. A nice structure on Prompting how to write good prompt (2025s skill like coding over 2000s). Types of LLM and how to choose one for your need. You would choose a LLM model based these criteria : Model Performance , Model Parameters, Training Input Training Method, Context Token Size , Model Speed, Model Cost # TODO include a picture here with examples.
- GPT Assistants : Gives a general intro to the world of Agent. As we are going to build autonomous much reliable agents. GPT assistants would prepare us ( model builders) for a hands on approach to tame  LLMs  . Also talks about extending an assistant's knowledge using file uploads. #TODO elobrate usecases for knowledge assistant : search, compare , contrast , ordering , classification and generation
- multi agent system. more than an agent with different persona, they interact either in group chat or in a hierarchical chat to solve a problem. How to use autogen ( a opens ource library to deal with multi agent). introduces CrewAI a parallel to autogen. how to use agentOps
- From an Agent perspective, Actions is an important component especially to implement RAG. ChatGPT plugin is basic implementation of Agent Action., Author Micheal depicts interaction between LLM and a plugin.
  - first_function : Gives a taste of how LLM can choose to call a function , and call with which params, uses `openai` package.
  - parallel_functions : how to use `OpenAI.chat.completions.create` which returns `tool_calls` which has info which function to call and how to call.
  - Semantic Kernel 
    - sk_connecting : How a semantic function can be created .how to use sk.kernel.add_service
    - sk_context_variable : How to write a prompt for LLM with _variable, which gets value during the call_.
    - Synergizing semantic and native functions
      - sk_first_skill : # TODO check one more time
        - Create a plugin under plug in directory 
        - You pass a list to plugin, kernel uses this list and LLM to get a merged output
      - sk_native_functions : how to call a native function when required , decision is made by LLM.
      - sk_semantic_native_functions: embedding native functions within semantic functions
    - SK as an interactive service agent : Gives nice taste on how to implement an interactive service with Semantic Kernel.
- Building Autonomous : I personally felt a very exciting chapter, as software engineer, we come from a concrete world of hand written , fixed business rules for an application. Autonomy on business rule during runtime is hard to face reality, also thrilling.
  - `behavior tree`, Micheal introduces behavior tree, I played around my own behavior trees with a robot example, from which understood the power of behavior tree. You may end up writing lot of if thens if you dont use behavior tree. At first it is hard to get into behavior tree in , understanding,  motivation and apprecitaion for behavior tree. `robot_behavior_tree.py` this example helped me.
  - Also he gives an execellent comparision chart of various AI control systems and which can be leveraged for AI Agents.
    - `Finite state Machine`, `Decision tree`, `utility-based-system`,`Rule-based-system`,`Planning system`,`Behavior cloning`,`Hierarchical Task Network`,`Blackboard system` and `Genetic algorithm`.
  - GPT Assistants playground : It needs efforts to understand but worth mastering, especially when you are moving towards autonomous agents.
  - Behavior Tree for Coding challenge and X post from youtube : I'm not quite convinced using behavior tree for coding challenge and autonomous X post. In my opinion, behavior tree is good where you need run multiple if thens with time tick. tick size can vary from millisecond to hours or even days.
  - Behavior Tree for conversational multi agent : BT would be effective agent conversation, as it involves feedback, reasoning and emergent behaviors.
  - Agentic Behavior Tree with back chaining : Its an interesting concept for top down approach for problems. 
  <div class="mermaid">
  flowchart LR
  igb[Identify goal behaviour] --> drq[Determine required actions ] --> ic[Identify the conditions] --> dmc[Determine the mode of communication] --> ct[Construct the tree]
- Nexus : worth master nexus code
- Agent memory and knowledge : What a beautiful depicted chapter. One of the best structure given for RAG (which is core of an Agent). In this chapter Micheal introduces RAG in a right way , what is vector , what is the importance of conventional SQL in agentic system (as against the trend talks predominantly about vector). basic RAG. Best explanation on document embeddings. starting from TF-IDF and advanced embedding techniques. Nice depiction of visual examining of vector db.

  
  </div>

- He structured the book
    - Introduction
    - LLM : happenings 
    - Multi-Agent
    - Agent Actions
    - Autonomous 
      - Behaviour Tree, FSM
      - He has built a playground
    - Assembling
    - Agent Memory
    - Platform to implement Agent : Prompt Flow | Auto gen
    - Agent Reasoning and evaluation
    - Agent Planning and Feedback

#### nucleous : It is best book 
  - this book explains,  what is an Agent, composition of an Agent, how to build the pieces ,how to test the pieces.
  - He took an example , grows it with various techniques.
  - He wrote this book by building agents and using it for this book
  - He explains RAG with an working sample
  - He explains memory in practical way (instead of use vector DB approach), beautifully splits difference between , vector DB and SQL and where to use what. Using detailed examples helps us to understand what is vector DB ? how the internals works

#### How to prove
  - evidence
    - Structure of the book : Definition and Agent, hands on examples to see that how various components works
    - expand points from nucleus 
  - proving events : I'm building an APP with agents that I need
  - Rejections 
    - When discussed about agents, my friends who are dealing with agents 
      - shared same approach : build MCP server   
      - Enterprise Architects talks in scaring language : Agent would open up security threat ( I'm not refusing but , until building agent to solve an inital problem of a company this is too early to talk  )


#### criticism
- A human drawn picture on definition of Agent
- LLM how to run locally using llama 
#### conclusion
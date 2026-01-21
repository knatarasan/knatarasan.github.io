---
layout: post
title: "My experienve with the book: AI Agents in Action by Michael Lanham"
tags: [wip]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

![image info]({{ site.image_base }}/2025-11-13/ai-agents-action.jpg)


As in the era of Agents, I wanted to build a customer-facing app (which is already being used by myself and my family). After skimming through a few books, I landed on **AI Agents in Action** by **Michael Lanham**.  
After reading this book for two iterations and working through the examples, I came to a clear conclusion: **this is the best book to learn AI Agents and build them for practical purposes.**

---

## Overview of the Book

The author starts with an amazing introduction to AI Agents, defining an agent in a very rational and grounded way.  
After this chapter, I started looking at an agent almost like a person.  
Let me use the pronoun “It” (as of 2025).

An agent:

- has a personality / persona  
- can remember facts  
- has mastery (tools)  
- can reason and evaluate  
- can plan and take feedback  

This mental model completely changed how I think about agents.  
The author also motivates what the agent era would look like—a world where software is no longer just deterministic rules, but adaptive, reasoning systems that work alongside humans.

LLMs are the backbone, but they are not magic.  
Think of an LLM as a genie that knows almost everything humankind has gathered, and if you talk to it in its language (prompting), you will get the right answer 90% of the time.

The author explains:

- popular LLMs  
- how to interact with them through APIs  
- how to run local LLMs  
- a nice structured approach to prompting, which honestly feels like a 2025 skill, similar to how coding was a 2000s skill  

He also explains types of LLMs and how to choose one based on:

- Model performance  
- Model parameters  
- Training input and training method  
- Context token size  
- Model speed  
- Model cost  

This section gives clarity instead of hype.

---

## GPT Assistants

This chapter gives a practical introduction to the world of agents.  
Since we are moving toward building autonomous and reliable agents, GPT Assistants prepare us (model builders) with a hands-on way to tame LLMs.

The author also explains how to extend assistant knowledge using file uploads.  
This is extremely powerful for building knowledge assistants, such as:

- search  
- compare  
- contrast  
- ordering  
- classification  
- content generation  

---

## Multi-Agent Systems

This chapter introduces systems where more than one agent, each with a different persona, collaborates to solve a problem.

Agents can interact:

- in group chat  
- in hierarchical conversations  

The author introduces:

- AutoGen (an open-source library for multi-agent systems)  
- CrewAI as a parallel approach  
- AgentOps for observing and managing agents  

---

## Agent Actions

From an agent’s perspective, actions are critical, especially for implementing RAG.  
ChatGPT plugins are explained as a basic implementation of agent actions.

Michael clearly depicts how an LLM interacts with a plugin, and then walks through practical examples:

##### first_function
Shows how an LLM decides when to call a function and with which parameters, using the openai package.

##### parallel_functions
Explains how OpenAI.chat.completions.create returns `tool_calls`, which tell us:

- which function to call  
- how to call it  

---

### Semantic Kernel

This is one of the strongest sections of the book.

##### sk_connecting
Shows how to create a semantic function and connect it using `sk.kernel.add_service`.

##### sk_context_variable
Explains how to write prompts with variables that get resolved at runtime.

##### Synergizing semantic and native functions

##### sk_first_skill
- Create a plugin under the plugin directory  
- Pass a list to the plugin  
- The kernel and LLM collaborate to generate a merged output  

##### sk_native_functions
Shows how an LLM can decide when to call native functions.

##### sk_semantic_native_functions
Embedding native functions inside semantic functions.

---

### Semantic Kernel as an Interactive Service Agent

This section gives a very practical taste of building real interactive services or so called conversational AI using SK.

---

## Building Autonomous Agents

Personally, this was one of the most exciting chapters.

As a software engineer, we came from a world of building concrete systems using concrete logic and deliver it with concrete testing. 
But it is both scary and thrilling to build a system with a probably concrete element ( LLM ) and pushing it towards autonomy.  I believe the traditional pattern of 70% effort to build a system and 30% effort to test would change in agentic building as 30% effort to build and 70% effort to test . Here I didn't mean software testing , but more functional testing with all functional edge cases.


### Behavior Trees

Michael introduces behavior trees, and I experimented with my own robot examples.  
That’s when I truly understood their power.

Without behavior trees, you end up writing endless if-else chains.  
At first, behavior trees are hard to appreciate, but this example [robot_behavior_tree.py]({{ site.image_base }}/2025-11-13/robot_behavior_tree.py) makes it clear.

The author provides an excellent comparison chart of AI control systems:

- Finite State Machine  
- Decision Tree  
- Utility-based System  
- Rule-based System  
- Planning System  
- Behavior Cloning  
- Hierarchical Task Network  
- Blackboard System  
- Genetic Algorithm  

---

## GPT Assistants Playground

Takes effort to understand, but it’s worth mastering—especially for autonomous agents.

---

## Behavior Tree for Coding Challenges and X Posts

I’m not fully convinced here.  
In my opinion, behavior trees shine where time-based ticks matter—milliseconds, minutes, hours, or even days.

---

## Behavior Tree for Conversational Multi-Agent Systems

This makes more sense, as conversation naturally involves feedback, reasoning, and emergent behavior.

---

## Agentic Behavior Tree with Back-Chaining

A very interesting top-down problem-solving approach.

---

## Nexus

You may focus on Nexus if you want to build agentic App by your self without frameworks.
The code is dense but powerful, and it ties together many concepts from earlier chapters.

---

## Agent Memory and Knowledge

This is one of the most beautifully written chapters in the book.

The author introduces RAG the right way:

- what vectors are  
- why SQL still matters in agentic systems  
- when vector DBs make sense and when they don’t  

### RAGR – Retrieval Augmented Generation & Remember

The “Remember” part is critical—the system stores what it generates.

### Semantic Search
Motivation of embedding vs TF-IDF is depicted very well.

- TF-IDF: word-frequency based  
- Embeddings: meaning-based, stored close in vector space  

I played around more examples to get visual idea of how values stored in vector databases, author lead us with right points.

- ChromaDB as an in-memory vector DB  
- LangChain  
- CharacterTextSplitter  
- OpenAIEmbeddings  

---

## Agent Memory Types

- Sensory (touch, visual, auditory)  
- Short-term (context, conversation, RAG)  
- Long-term  
  - Explicit (facts, life events)  
  - Implicit (procedural memory)  

Memory compression and practical trade-offs are explained very clearly.

---

## Prompting, Reasoning, Planning, and Evaluation

This section ties everything together:

- Prompt engineering  
- Prompt flow  
- Agent profiles (why they matter)  
- Reasoning and planning  
- Chain-of-thought  
- Evaluation techniques  
- Feedback loops  

It feels like engineering discipline finally applied to AI.

---

## How the Book Is Structured

- Introduction  
- LLM Fundamentals  
- Multi-Agent Systems  
- Agent Actions  
- Autonomous Systems  
- Assembling Agents  
- Agent Memory  
- Platforms (Prompt Flow, AutoGen)  
- Reasoning & Evaluation  
- Planning & Feedback  

---

## Nucleus: Why This Is the Best Book

- It explains what an agent is, what it’s made of, and how to build each part  
- A single example grows throughout the book  
- The author clearly built agents while writing this book  
- RAG is explained with working samples  
- Memory is explained practically, not just “use a vector DB”  

### Proof

- The book structure itself is evidence  
- I’m actively building an app with agents using these concepts  
- Conversations with others working on agents confirm the same approach  

Some enterprise architects talk in a scary language about security risks.  
I’m not denying them—but until we build agents that solve real problems, that discussion feels premature.



---

## Conclusion

**AI Agents in Action** is not just a book—it’s a playbook.  
If you want to understand agents deeply, build them practically, and reason about them correctly, this book is hard to beat.


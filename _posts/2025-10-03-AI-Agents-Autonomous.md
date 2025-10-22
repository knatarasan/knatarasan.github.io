---
layout: post
title: "AI-Agents-Autonomy"
tags: [wip]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

### Autonomous
##### what is autonomy ?
A machine or application's ability to solve a problem or handle a scenario, even when instructions to solve isn't given, the meaning of word auto is "self" or "by itself".

##### chronological history of autonomous ?
boat - wind driven -  wheel - animal  pulled carts - engines (steam to diesel) - machines ( make decision , gears and timing wheels ) - electronics - computer - LLM model

##### why am I worrying about it now ?
LLMs makes decision now , probabilistically. When asked in human language, with right context  (  with opt memory ( memory and knowledge) , all relevant tools accessible and registered through semantic layer), it is being proven that the probability exceeds human decisions.

##### Advantage of autonomy ?
###### To overcome a user's limitation 
Poor user had been stuck with rigid system and UI, he can only consume the information provided by the application . So he can only provide info within this limitation . He can't ask a specific question.

###### To overcome an engineer's limitation
So far the tool in my mastery, a computer language (eg : python ) can do things what had been instructed to do , and can handle exceptions in the way it is instructed. An application built in this way can make decisions, based on pre written instructions (through if then else ).An Engineer's scope of building App is based on the tools he had.

###### To overcome system's limitation
With conventional UI and backend, there is no way an app can provide additional info to user, when it found

##### Dis-advantage of autonomy ?
  - The engineer or builder feels out of control, since the system would eventually create its own code/logic and going to serve the user
  - Testing : So far engineer wrote the code for scenarios and all those scenarios were tested., now the scenarios are in future , how to test them.
  - Responsibility : So far product manager owns the business logic and engineer owns the code , now who is responsible
  
#### In a robot , autonomy ?
Imagine a robot with following tasks,
  - found enemy 
    - FIGHT
  - low battery
    - CHARGE
  - PATROL field

What is time required for charging ?
How to interrupt , when enemy found while charging ? (how to decide should I charge more or fight )
How to set FIGHT strategy when having least charge

##### Autonomous powered by an AI agent ?
Yes, it can do what it wasn't instructed to do . 
  - It can use behavior tree 
    - what is behavior tree ? and eg 
    - Behavior Tree vs Vanilla "if else"
    - how can you solve a behavior tree problem with if then else ?
  - It can create tools to solve a problem ( a python code) and execute it to solve. ( this code is based on the scenario given)

- Autonomy in AI breaks this barrier in the following ways,
  - AI can create its own tools ( eg : python ), to solve a problem that the builder (engineer) is not aware of.
  - Using un conventional decision making logics
    - Behavior Tree
    - FSM 
    - Decision Tree
    - Utility-based system
    - Rule-based system
    - Planning system
    - Behavioral cloning
    - Hierarchical Task Network (HTN)
    - Blackboard system
    - Genetic algorithm


#### How to apply to my app ?
In my Personal finance App, I can use it in following points,
  - User uploads a transactions file , the parser failed to process it ( due to format mismatch)
  - Users asks an analytical question , where there isn't a logic written in app to answer or show visual.
  - Agent come up with an analysis, insight or suggested action neither asked by the user nor triggered from the business logic.



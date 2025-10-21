---
layout: post
title: "AI-Agents-Autonomous"
tags: [wip]
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

### Autonomous
##### what is autonomous ?
A machine or application's ability to solve a problem or handle a scenario, even when instructions to solve isn't given, the meaning of word auto is "self" or "by itself".

##### chronological history of autonomous ?
boat - wind driven -  wheel - animal  pulled carts - engines (steam to diesel) - machines ( make decision , gears and timing wheels ) - electronics - computer - LLM model

##### why am I worrying about it now ?
LLMs makes decision now , probabilistically. When asked in human language, with right context  (  with opt memory ( memory and knowledge) , all relevant tools accessible and registered through semantic layer), it is being proven that the probability exceeds human decisions.

##### An engineer's limitations ?
So far the tool in my mastery had been a language ( eg : python) can do things what had been instructued to do , and can handle exceptions again the way I instructed. 
  - his app can make decision only based on pre written if then else .
  - Engineer's scope of building App is based on the tools he had

##### What happens without autonomy in an app ?
- The user is so limited to access info from the rigid interface. 
- He can't ask a question 
- The App can't provide an interesting info that it found , like to be shared with user

#### In a robot , autonomacity ?
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

#### How to apply to my app ?
In my Personal finance App, I can use it in following points,
  - User uploads a transactions file , the parser failed to process it ( due to format mismatch)
  - Users asks an analytical question , where there isn't a logic written in app to answer or show visual.
  - Agent come up with an analysis, insight or suggested action neither asked by the user nor triggered from the business logic.



---
layout: post
title: "Agent Building: Semantic Kernel vs Promptflow"
tags: [wip]
permalink: /2025/10/01/agent-building-sk-promptflow.html
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

### Semantic Kernel vs Prompt Flow

- As Semantic Kernel and PromptFlow are important libraries to build agents 
- As we (myself and my buddy ) are building [A personal finance app with Agents In-Built]({% link _posts/2025-10-02-how-to-design-an-app-with-agents.md %})
-  Here I'm sharing what am I ponder where to use Semantic Kernel and where to use PromptFlow

<img src="/assets/images/2025-10-01/sk.png" alt="Semantic Kernel" height="230" loading="lazy" decoding="async" style="vertical-align:middle;" />
 vs 
<img src="/assets/images/2025-10-01/pf.svg" alt="PromptFlow" height="250" loading="lazy" decoding="async" style="vertical-align:middle;" />

<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Semantic Kernel <br/><code>agent brain  / orchestration engine</code></th>
      <th>Prompt Flow <br/><code>flow engine + evolution & deployment</code></th>
      <th>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>A Request that may require <b>Branching / Dynamic</b>  decision making</b>
      </td>
      <td>Yes (multiple plugins could be registered to SK, at runtime SK can decide which plugin to use)</td>
      <td>No (static has limited control logic)</td>
      <td>You can embed SK logic inside a PromptFlow node to get dynamic behavior within a flow</td>
    
    </tr>
    <tr>
    <td colspan=4>
    <div class="mermaid">
    flowchart LR
    cu[Anser my calculus question ?]:::cu --> sk((Semantic Kernel))
    sk --> ca[Calculus Plugin]:::cu
    mu[Recommend movie]:::mu --> sk
    sk --> mo[Movie Plugin]:::mu

    classDef cu stroke:#0f0
    classDef mu stroke:#f90
    </div>
    </td>
    </tr>
    
    <tr>
      <td><b>Evaluation</b>, testing, metrics, deploying generative App</td>
      <td>No (Less focused on built-in evaluation)</td>
      <td>Yes (Built-in evaluation, batch runs, metric tracking)</td>
      <td>Prompt Flow can be used to evaluate &amp; benchmark your SK planners/plugins</td>
    </tr>
    <tr>
    <td colspan=4>
    <img src="/assets/images/2025-10-01/pf_flow.png" alt="Semantic Kernel" height="230" loading="lazy" decoding="async" style="vertical-align:middle;" />
    </td>
    </tr>
    <tr>
      <td><b>Visual flow</b> (eg: DAG), modular nodes &amp; team visibility</td>
      <td>No (more code)</td>
      <td>Yes (flows declared in YAML, visualized, nodes can be debugged individually)</td>
      <td>PromptFlow can be used to structure and visualize your Sk-based logic</td>
    </tr>
    
    <tr>
      <td>You want to integrate with <b>existing code</b>,libraries, APIs , business logic</td>
      <td>Yes (you can call native code, integrate with your systems)</td>
      <td>No (native code has to be in nodes)</td>
      <td>Use SK for heavy lifting but wrap or invoke parts via PromptFlow when you want orchestration at flow level</td>
    </tr>

    <tr>
      <td colspan=4>
        <div class="mermaid">
        flowchart LR

        pl[Show me significant expenses in Aug transactions]:::pl --> sk((Semantic Kernel))
        subgraph plugin
          sk -- "call existing code" --> td[TransactionsData]:::pl
          end
        classDef pl stroke:#00f

        </div>
      </td>
    </tr>
    <tr>
      <td><b>Simpler</b> and <b>Linear</b> prompt pipeline (eg: prompt-&gt; model -&gt; output -&gt; post process)</td>
      <td>No (overkill)</td>
      <td>Yes (good fit for simpler workflows)</td>
      <td>You may use SK funcitons/skills but flow is main driver</td>
    </tr>
    <tr>
    <td colspan=4>    
    <img src="/assets/images/2025-10-01/pf_simple_flow.png" alt="Semantic Kernel" height="230" loading="lazy" decoding="async" style="vertical-align:middle;" />
    </td>
    </tr>
    <tr>
      <td>You anticipate the <b>logic evolving</b>, branching , growing more complex</td>
      <td>Yes</td>
      <td>No - Constrained for highly dynamic logic</td>
      <td>Mix them : flows + planner nodes</td>
    </tr>
  </tbody>
</table>


### Suggested prcatice
- Start with prompt flow for simple prompt pipelines; if behabior becomes more dynamic/complex, introduce SK for planning/skill orcgestration inside the flow
- Use Prompt Flow's evaluation/batch testing on SK planners&plugins to get metcis and guard quality
- Keep logic-heavy decisions down into SK and flow logic in prompt flow.
- Keep visualization and modular node capabilities in prompt flow to manage complexity, esp across team
  
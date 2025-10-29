---
layout: post
title: "Agent Building: Semantic Kernel vs Promptflow"
tags: [tech]
permalink: /2025/10/01/agent-building-sk-promptflow.html
---

{% if page.tags contains "wip" %}

<div style="background:#ffeeba; border-left:4px solid #f0ad4e; padding:1em; margin-bottom:2em;">
  🚧 This post is a Work In Progress — feel free to share feedback.
</div>
{% endif %}

### Semantic Kernel vs Prompt Flow

Semantic Kernel and PromptFlow are important libraries to build agents. Semantic Kernel, in my understanding, is a platform to build agents which helps to bridge a query in human language translated into a concrete function call to an internal API, and the resulting values from the API call is converted back to human language. PromptFLow is simply an agent that could be built in the form of a flow with jinja templates for the prompts and python code for evaluation.
While building [A personal finance app with Agents In-Built]({% link _posts/2025-10-02-how-to-design-an-app-with-agents.md %}), me and my buddy came across this scenario. Here are some of the thoughts I pondered while building.</p>

<img src="/assets/images/2025-10-01/sk.png" alt="Semantic Kernel" height="200" loading="lazy" decoding="async" style="vertical-align:middle;" />
 vs 
<img src="/assets/images/2025-10-01/pf.svg" alt="PromptFlow" height="220" loading="lazy" decoding="async" style="vertical-align:middle;" />

<table>
  <thead>
    <tr style="vertical-align:top">
      <th>Scenario</th>
      <th>Semantic Kernel <br/><code>agent brain  </code></th>
      <th>Prompt Flow <br/><code>flow engine </code></th>
      <th>Hybrid approach</th>
    </tr>
  </thead>
  <tbody>
  <tr><td colspan=4>. </td></tr>
    <tr style="vertical-align:top">
      <td>A Request that may require <b>Branching / Dynamic</b>  decision making</b>
      </td>
      <td><b>Semantic Kernel : Yes</b> <br/>(multiple plugins could be registered to SK, at runtime SK can decide which plugin to use)</td>
      <td><b>PromptFlow : No</b> <br/> (static has limited control logic)</td>
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
    
    <tr><td colspan=4>. </td></tr>
    <tr style="vertical-align:top">
      <td><b>Evaluation</b>, testing, metrics, deploying generative App</td>
      <td><b>Semantic Kernel : No</b> <br/> (Less focused on built-in evaluation)</td>
      <td><b>PromptFlow : Yes</b> <br/> (Built-in evaluation, batch runs, metric tracking)</td>
      <td>Prompt Flow can be used to evaluate &amp; benchmark your SK planners/plugins</td>
    </tr>
    <tr>
    <td colspan=4>
    <img src="/assets/images/2025-10-01/pf_flow.png" alt="Semantic Kernel" height="230" loading="lazy" decoding="async" style="vertical-align:middle;" />
    </td>
    </tr>


    <tr><td colspan=4>. </td></tr>
    <tr style="vertical-align:top">
      <td><b>Visual flow</b> (eg: DAG), modular nodes &amp; team visibility</td>
      <td><b>Semantic Kernel : No</b> <br/> (more code)</td>
      <td><b>PromptFlow : Yes</b> <br/> (flows declared in YAML, visualized, nodes can be debugged individually)</td>
      <td>PromptFlow can be used to structure and visualize your Sk-based logic</td>
    </tr>
    
<tr><td colspan=4>. </td></tr>
    <tr style="vertical-align:top">
      <td>You want to integrate with <b>existing code</b>,libraries, APIs , business logic</td>
      <td><b>Semantic Kernel : Yes</b> <br/> (you can call native code, integrate with your systems)</td>
      <td><b>PromptFlow : No</b> <br/> (native code has to be in nodes)</td>
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
    <tr><td colspan=4>. </td></tr>
    <tr style="vertical-align:top">
      <td><b>Simpler</b> and <b>Linear</b> prompt pipeline (eg: prompt-&gt; model -&gt; output -&gt; post process)</td>
      <td><b>Semantic Kernel : No</b> <br/> (overkill)</td>
      <td><b>PromptFlow : Yes</b> <br/> (good fit for simpler workflows)</td>
      <td>You may use SK funcitons/skills but flow is main driver</td>
    </tr>
    <tr>
    <td colspan=4>    
    <img src="/assets/images/2025-10-01/pf_simple_flow.png" alt="Semantic Kernel" height="230" loading="lazy" decoding="async" style="vertical-align:middle;" />
    </td>
    </tr>
    <tr><td colspan=4>. </td></tr>
    <tr style="vertical-align:top">
      <td>You anticipate the <b>logic evolving</b>, branching , growing more complex</td>
      <td><b>Semantic Kernel : Yes</b> <br/></td>
      <td><b>PromptFlow : No</b> <br/> - Constrained for highly dynamic logic</td>
      <td>Mix them : flows + planner nodes</td>
    </tr>
  </tbody>
</table>


### Suggested prcatice
- Start with prompt flow for simple prompt pipelines; if behabior becomes more dynamic/complex, introduce SK for planning/skill orcgestration inside the flow
- Use Prompt Flow's evaluation/batch testing on SK planners&plugins to get metcis and guard quality
- Keep logic-heavy decisions down into SK and flow logic in prompt flow.
- Keep visualization and modular node capabilities in prompt flow to manage complexity, esp across team
  
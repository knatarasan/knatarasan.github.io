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
- I' pondering to understand where to use Semantic Kernel and where to use PromptFlow

<img src="/assets/images/2025-10-01/sk.png" alt="Semantic Kernel" height="230" loading="lazy" decoding="async" style="vertical-align:middle;" />
 vs 
<img src="/assets/images/2025-10-01/pf.svg" alt="PromptFlow" height="250" loading="lazy" decoding="async" style="vertical-align:middle;" />

| Scenario                                                                          | Semantic Kernel                                                                                 | Prompt Flow                                                                     | Notes                                                                                                      |
| --------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| A Request that may require branching/dynamic decision making                      | Yes  (multiple plugins could be registered to SK, at runtime SK can decide which plugin to use) | No (static has limited control logic)                                           | You can embed SK logic inside a PromptFlow node to get dynamic behavior within a flow                      |
| Evaluation, testing, metrics, deploying generative App                            | No (Less focused on built-in evaluation)                                                        | Yes (Built-in evaluation, batch runs, metric tracking)                          | Prompt Flow can be used to  evaluate & benchmark your SK planners/plugins                                  |
| Visual flow/ DAG, modular nodes & team visibility                                 | No (more code)                                                                                  | Yes   (flows declared in YAML , visualized, nodes can be debugged individually) | PromptFlow can be used to structure and visualize your Sk-based logic                                      |
| You want to integrate with existing code,libraries, APIs , business logic         | Yes   ( you can call native code,integrate with your systems)                                   | No  ( native code has to be in nodes)                                           | Use SK for heavy lifting but wrap or invoke parts via PromptFlow when you want orchestration at flow level |
| Simpler and linear prompt pipeline (eg: prompt-> model -> output -> post process) | No (overkill)                                                                                   | Yes  (good fit for simpler workflows)                                           | You may use SK funcitons/skills but flow is main driver                                                    |
| You anticipate the logic evolving, branching , growing more complex               | Yes                                                                                             | No - Constrained for highly dynamic logic                                       | Mix them : flows + planner nodes                                                                           |
| how to treat                                                                      | `agent brain`/orchestration engine                                                              | `flow engine` + evaluation/deployment polish                                    |

### Suggested prcatice
- Start with prompt flow for simple prompt pipelines; if behabior becomes more dynamic/complex, introduce SK for planning/skill orcgestration inside the flow
- Use Prompt Flow's evaluation/batch testing on SK planners&plugins to get metcis and guard quality
- Keep logic-heavy decisions down into SK and flow logic in prompt flow.
- Keep visualization and modular node capabilities in prompt flow to manage complexity, esp across team
  
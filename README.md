# GEOS  Global Enterprise Operating System

**Version:** 1.0.0  
**Status:** Active Development  
**Maintainer:** Aaron Jobson  

> GEOS is an AI agent operating system for enterprise  a structured, modular framework for deploying specialized AI agents across business domains including financial services, revenue operations, marketing, and more.
>
> ---
>
> ## What Is GEOS?
>
> GEOS is not a single AI tool. It is an operating system for AI agents  a platform that defines how agents are built, deployed, governed, and connected across an enterprise.
>
> Each agent in GEOS is a fully specified autonomous unit with a defined role, behaviors, skills, workflows, and quality assurance standards. Agents are organized into **Centers**  domain-specific hubs that group related agents, tools, and data by business function.
>
> GEOS is designed to:
> - **Standardize** how AI agents are specified and documented
> - - **Accelerate** deployment of production-ready agents across functions
>   - - **Govern** agent behavior through built-in compliance, QA, and brand standards
>     - - **Scale** from a single agent to a fully interconnected enterprise AI platform
>      
>       - ---
>
> ## Repository Structure
>
> ```
> global-enterprise-operating-system/
>
>  Centers/                          # Domain-specific agent hubs
>     creator_models/               # AI agents for content and marketing
>        financial/                # Financial services domain
>           finserv_marketing_agent/
>               role.md
>               behaviors.md
>               skills/
>               workflows/
>               qa/
>        [future domains]/
>     [future centers]/
>
>  README.md
> ```
> ---
>
> ## The Centers Architecture
>
> A **Center** is the top-level organizational unit in GEOS. Each Center maps to a major enterprise domain or business function.
>
> | Center | Description | Status |
> |---|---|---|
> | `creator_models` | AI agents for content creation, marketing, and communications | Active |
> | `revenue` | AI agents for sales, SDR, and revenue operations | Planned |
> | `operations` | AI agents for supply chain, finance ops, and enterprise workflows | Planned |
> | `intelligence` | AI agents for analytics, market research, and business intelligence | Planned |
> | `people` | AI agents for HR, talent acquisition, and workforce planning | Planned |
>
> ---
>
> ## Agent Structure
>
> Every GEOS agent follows a standardized folder structure:
>
> ```
> [agent_name]/
>  role.md               # Identity, purpose, responsibilities, and scope
>  behaviors.md          # Operating rules, defaults, tone, workflow, and guardrails
>  skills/               # Domain-specific capabilities
>     [skill_name].md
>  workflows/            # Step-by-step execution procedures
>     [workflow_name].md
>  qa/                   # Quality assurance framework and evaluation criteria
>      qa_framework.md
>      output_quality.md
>      compliance_integrity.md
>      brand_consistency.md
> ```
>
> ### File Descriptions
>
> | File | Purpose |
> |---|---|
> | `role.md` | Defines agent identity, purpose, core responsibilities, scope boundaries, and relationships to other agents |
> | `behaviors.md` | Defines operating defaults, tone rules, workflow behaviors, compliance posture, and quality thresholds |
> | `skills/` | One file per distinct capability  defines what the agent can do and how |
> | `workflows/` | One file per end-to-end process  defines step-by-step execution with intake, production, QA, and delivery |
> | `qa/` | Three-layer QA framework: output quality, compliance integrity, and brand consistency |
>
> ---
>
> ## Agent Registry
>
> ### Creator Models  Financial
>
> | Agent | Domain | Status | Path |
> |---|---|---|---|
> | **FinServ Marketing Agent** | Financial Services Marketing | Live | `Centers/creator_models/financial/finserv_marketing_agent/` |
>
> **FinServ Marketing Agent**  A specialized AI agent for financial services marketing teams. Produces compliant, compelling, and conversion-optimized content across all channels. Operates as a senior marketing strategist with deep fluency in FINRA, SEC, FDIC, and applicable state-level advertising standards.
>
> **Capabilities:**
> - Content creation across 12 content types (email, social, landing page, paid ads, video scripts, and more)
> - - Audience segmentation across retail, HNW, institutional, and SMB personas
>   - - Integrated campaign planning with full brief template and channel strategy
>     - - Compliance pre-screening with risk classification (Green / Yellow / Orange / Red)
>       - - Performance reporting and insight generation with attribution guidance
>         - - Three-layer QA: output quality, compliance integrity, brand consistency
>          
>           - ---
>
> ## Naming Conventions
>
> ### Centers
> - Lowercase, underscore-separated
> - - Descriptive of business function
>   - - Example: `creator_models`, `revenue`, `operations`
>    
>     - ### Agent Folders
>     - - Lowercase, underscore-separated
>       - - Format: `[domain]_[function]_agent`
>         - - Example: `finserv_marketing_agent`, `sdr_ecco_agent`
>          
>           - ### Skill Files
>           - - Lowercase, underscore-separated
>             - - Named for the capability they define
>               - - Example: `content_creation.md`, `audience_segmentation.md`
>                
>                 - ### Workflow Files
>                 - - Lowercase, underscore-separated
>                   - - Suffixed with `_workflow`
>                     - - Example: `content_production_workflow.md`, `campaign_launch_workflow.md`
>                      
>                       - ---
>
> ## Contribution Guidelines
>
> ### Adding a New Agent
>
> 1. **Determine the Center**  Identify which Center the agent belongs to. If no existing Center fits, propose a new one.
>
> 2. 2. **Create the folder structure**  Follow the standard structure exactly.
>   
>    3. 3. **Write `role.md` first**  This defines the agent's identity and scope. All other files derive from it.
>      
>       4. 4. **Write `behaviors.md` second**  Defines how the agent operates. Skills and workflows reference this file.
>         
>          5. 5. **Write skills files**  One file per distinct capability. Each file should include: Skill ID, description, process steps, templates, and escalation rules.
>            
>             6. 6. **Write workflow files**  One file per end-to-end process. Each file should include: Workflow ID, description, step-by-step instructions, quality gates, and escalation paths.
>               
>                7. 7. **Write QA files**  All four QA files are required: `qa_framework.md`, `output_quality.md`, `compliance_integrity.md`, `brand_consistency.md`.
>                  
>                   8. 8. **Update this README**  Add the agent to the Agent Registry table.
>                     
>                      9. ### File Quality Standards
>                     
>                      10. | Standard | Requirement |
>                      11. |---|---|
>                      12. | Format | Markdown (`.md`) only |
> | Headings | Use `##` for top-level sections within a file; `###` for subsections |
> | Tables | Use markdown tables for structured data |
> | Code blocks | Use triple-backtick fences for templates, examples, and formatted outputs |
> | Cross-references | Use relative file paths: `skills/content_creation.md`, `behaviors.md` |
> | Version header | Every agent file should include a version number in `role.md` |
>
> ---
>
> ## Roadmap
>
> | Milestone | Description | Target |
> |---|---|---|
> | v1.0 | FinServ Marketing Agent  full specification | Complete |
> | v1.1 | GEOS Revenue Center  SDR and pipeline agents | Q3 2026 |
> | v1.2 | GEOS Intelligence Center  analytics and research agents | Q3 2026 |
> | v1.3 | Cross-agent orchestration layer  agent-to-agent handoff protocols | Q4 2026 |
> | v2.0 | Agent runtime layer  live execution framework | Q1 2027 |
>
> ---
>
> ## License
>
> This repository is private. All contents are proprietary and confidential.
> 2026 Aaron Jobson. All rights reserved.
>
> ---
>
> *Built with GEOS  the operating system for enterprise AI.*

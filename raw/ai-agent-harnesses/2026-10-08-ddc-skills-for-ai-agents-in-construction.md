# DDC Skills Collection for AI Coding Assistants

> Source: https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction/tree/main
> Collected: 2026-10-08
> Published: Unknown

## AI Tools for Construction Company Automation

The DDC Skills Collection is a collection of 238 skills for automating construction company processes with AI coding assistants. It works with Claude Code, Google Antigravity, OpenCode, ClawdBot, and similar assistants.

## What Is a Skill?

A skill is a `SKILL.md` file containing structured instructions that an AI coding assistant can read and execute. Each skill describes a specific task, the problem it solves, the code to generate, and the tools it needs. The user opens a skill folder in an AI assistant, which helps implement the described functionality.

## Collection Structure

Skills are organized by source and complexity level:

| Category | What's inside | Skills | Start here if... |
|----------|---------------|--------|------------------|
| **1_DDC_Toolkit** | Production-ready tools: CWICR database, CAD converters, analytics | 85 | You need a working tool now |
| **2_DDC_Book** | Skills mapped to book chapters: data evolution, types, estimation, ML | 67 | You want a structured learning path |
| **3_DDC_Insights** | Practical workflows: n8n automation, AI agents, field tools | 20 | You need workflow automation |
| **4_DDC_Curated** | Document generation for PDF, Excel, DOCX, and PPTX, plus quality checks | 20 | You need document or report templates |
| **5_DDC_Innovative** | Computer vision, IoT, digital twins, risk assessment, AI agents, ESG, EU AI Act, circular construction, and generative design | 34 | You are ready for AI/ML experimentation |
| **6_OpenConstructionERP** | Cost bases, BOQ and estimating, BIM takeoff, 4D/5D, cost browser, MCP, field operations, tendering, validation, geo/coordination, and property development | 12 | You build on the open-source construction ERP |

The collection describes CWICR database coverage, CAD converters from Revit/IFC/DWG to Excel, analytics, book chapters on data evolution and estimation, n8n workflows, field automation, document generation, advanced BIM and AI/ML, IoT, digital twins, ESG, generative design, and OpenConstructionERP integrations.

## Where to Start

Construction managers should begin with `GETTING_STARTED.md`, read the Data-Driven Construction book, and then choose a skill matching the largest operational pain point. Developers and IT leads should install prerequisites, select a skill folder, read its `SKILL.md`, adapt the generated code to local data, and deploy it.

## Automation Examples

The repository maps construction problems to skills. Examples include semantic search across work-item rates with `semantic-search-cwicr`, estimate generation with `estimate-builder`, BIM quantity and property extraction with `ifc-to-excel` and `rvt-to-excel`, automated reports with `n8n-daily-report`, site-photo classification with `n8n-photo-report`, data-silo discovery with `data-silo-detection`, KPI dashboards with `kpi-dashboard`, budget comparison with `budget-tracker`, PDF specification extraction with `specification-extractor`, and schedule variance analysis with `schedule-delay-analyzer`.

The README calls these examples a selection and elsewhere says the full collection contains 221 skills covering estimation, reporting, BIM, document processing, and analytics, despite its title and category table stating 238 skills.

## How to Use a Skill

```text
1. Clone this repository.
2. Open a skill folder in the AI assistant.
3. Let the assistant read SKILL.md and generate the code.
4. Review, adapt to local data, and run it.
```

The README's ETL example reads Excel files with pandas, concatenates them, calculates totals from quantity and unit price, groups totals by category, and writes a summary workbook.

## Implementation Path

The proposed automation path has five stages:

1. **Audit:** list company data sources such as Excel files, databases, BIM models, PDFs, and email. Suggested skills include `data-silo-detection` and `data-source-audit`.
2. **Classify:** identify structured, semi-structured, and unstructured data. Suggested skills include `data-type-classifier` and `data-profiler`.
3. **Connect:** build ETL pipelines to extract and normalize data. Suggested skills include `etl-pipeline`, `ifc-to-excel`, and `specification-extractor`.
4. **Automate:** create recurring reports, alerts, and dashboards. Suggested skills include `n8n-daily-report`, `kpi-dashboard`, and `budget-tracker`.
5. **Analyze:** apply analytics and machine learning to find patterns and predict outcomes. Suggested skills include `cost-prediction`, `schedule-forecaster`, and `risk-assessment`.

Each stage builds on the previous one, but the user can enter at any stage depending on the current state.

## Construction Data Types

The README groups construction data into three types:

| Data type | Examples | Processing skills |
|-----------|----------|-------------------|
| **Structured** | Excel, CSV, SQL databases | `etl-pipeline`, `estimate-builder`, `budget-tracker` |
| **Semi-structured** | IFC/BIM models, JSON, XML | `ifc-to-excel`, `rvt-to-excel`, `dwg-to-excel` |
| **Unstructured** | PDF documents, photos, scans | `specification-extractor`, `n8n-photo-report`, `document-ocr` |

The intended flow is to extract or parse these inputs into a central database and then use automation and analytics. Structured data uses direct queries and transformations, semi-structured data uses specialized parsers, and unstructured data uses AI or OCR extraction.

## Prerequisites

The stated requirements are Python 3.9+, an AI coding assistant, basic Python knowledge, and project data such as Excel files, PDFs, or BIM models. Optional requirements for advanced skills include Docker, PostgreSQL or SQLite, and an OpenAI API key.

The example installation command is:

```bash
pip install pandas openpyxl ifcopenshell pdfplumber
```

## Repository Layout

The top-level layout contains `1_DDC_Toolkit/`, `2_DDC_Book/`, `3_DDC_Insights/`, `4_DDC_Curated/`, `5_DDC_Innovative/`, `6_OpenConstructionERP/`, `Books/`, `GETTING_STARTED.md`, and `README.md`.

The toolkit contains CWICR and CAD-converter tools. The book section covers data evolution, data silos, estimation, and ETL. Insights covers n8n, AI agents, field automation, and open-data transparency. Curated contains document generation and quality assurance. Innovative contains defect detection, digital twins, IoT, advanced BIM, agent orchestration, embodied carbon, ESG, EU AI Act, material passports, and generative design.

## Documentation and Results

`GETTING_STARTED.md` is aimed at executives and beginners, `OPTIMIZER_GUIDE.md` explains how developers can work effectively with AI assistants, and `IMPROVEMENT_ROADMAP.md` describes collection development.

The README presents potential improvements as examples rather than guarantees: database queries instead of manual price-book searches, aggregated daily reports instead of manual collection, script-based IFC extraction instead of manual measurement, scheduled budget comparisons instead of weekly spreadsheet updates, and metadata classification instead of manual document sorting. It states that results depend on data preparation, company size, and workflow complexity.

Most skills are based on the Data-Driven Construction book, which describes data maturity, bottlenecks, data classification, and automation priorities. The book is offered in 31 languages.

## Resources, Licensing, and Contribution

Resources include the Data-Driven Construction website and books, the OpenConstructionEstimate demo, the DDC GitHub organization, the OpenConstructionEstimate-DDC-CWICR repository, and the CAD2Data Revit/IFC/DWG/DGN pipeline.

The README lists CC BY-NC 4.0 for the CWICR database, separate DDC commercial licensing for that database, and MIT licensing for DDC tools and skills. Contributions can report issues, suggest skills, or submit pull requests. Each skill should include a clear `SKILL.md` with instructions and working code examples.

The README notes that product names and file-format references are used for identification and interoperability, not endorsement.

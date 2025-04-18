#!/usr/bin/env python3
import json

# Mapping from original categories to consolidated categories
category_mapping = {
    # 1. Data Versioning & Lineage
    "Data & Model Versioning": "Data Versioning & Lineage",
    "Data Lake Management": "Data Versioning & Lineage",
    "Data Versioning": "Data Versioning & Lineage",
    "Data Lineage & Pipelines": "Data Versioning & Lineage",
    "Data Lineage": "Data Versioning & Lineage",

    # 2. Data Management & Catalog
    "Data Management": "Data Management & Catalog",
    "Data Catalog": "Data Management & Catalog",

    # 3. Data Preparation & Validation
    "Data Validation": "Data Preparation & Validation",
    "Data Processing": "Data Preparation & Validation",
    "Data Enrichment": "Data Preparation & Validation",
    "Data Exploration": "Data Preparation & Validation",

    # 4. Data Labeling & Annotation
    "Data Labeling": "Data Labeling & Annotation",
    "Data Labeling / Weak Supervision": "Data Labeling & Annotation",

    # 5. Feature Engineering & Store
    "Feature Store": "Feature Engineering & Store",
    "Feature Store / Platform": "Feature Engineering & Store",

    # 6. Workflow Orchestration & Pipelines
    "Workflow Orchestration": "Workflow Orchestration & Pipelines",
    "ML Pipeline Platform": "Workflow Orchestration & Pipelines",
    "ML Pipeline Framework": "Workflow Orchestration & Pipelines",
    "Pipeline Framework": "Workflow Orchestration & Pipelines",
    "Workflow Automation": "Workflow Orchestration & Pipelines",

    # 7. Experiment Tracking
    "Experiment Tracking": "Experiment Tracking",

    # 8. Model Building & Hyperparameter Tuning
    "Hyperparameter Tuning": "Model Building & Hyperparameter Tuning",
    "Distributed ML Framework": "Model Building & Hyperparameter Tuning",
    "AutoML": "Model Building & Hyperparameter Tuning",
    "AutoML/Hyperparameter Tuning": "Model Building & Hyperparameter Tuning",
    "AutoML/ML Platform": "Model Building & Hyperparameter Tuning",
    "AutoML/Low-code ML": "Model Building & Hyperparameter Tuning",
    "AutoML/Database ML": "Model Building & Hyperparameter Tuning",
    "AutoML Platform": "Model Building & Hyperparameter Tuning",

    # 9. Model Serving & Deployment
    "Model Serving": "Model Serving & Deployment",
    "Model Deployment": "Model Serving & Deployment",
    "Model UI & Serving": "Model Serving & Deployment",
    "Model UI & Apps": "Model Serving & Deployment",
    "Model Sharing/Deployment": "Model Serving & Deployment",

    # 10. Model Monitoring & Validation
    "Model Monitoring": "Model Monitoring & Validation",
    "Data Logging & Monitoring": "Model Monitoring & Validation",
    "Model Testing & Validation": "Model Monitoring & Validation",
    "Model Lifecycle": "Model Monitoring & Validation",

    # 11. Model Debugging & Visualization
    "Model Debugging": "Model Debugging & Visualization",
    "Model Visualization": "Model Debugging & Visualization",
    "Experiment Visualization": "Model Debugging & Visualization",
    "LLM Evaluation & Debugging": "Model Debugging & Visualization",

    # 12. Interpretability & Fairness
    "Model Interpretability": "Interpretability & Fairness",
    "Fairness & Bias": "Interpretability & Fairness",
    "Model Fairness & Privacy": "Interpretability & Fairness",

    # 13. Optimization & Scaling
    "Optimization & Scaling": "Optimization & Scaling",

    # 14. Platforms & DevOps
    "ML Platform": "Platforms & DevOps",
    "Cloud ML Platform": "Platforms & DevOps",
    "Training Framework/ML Platform": "Platforms & DevOps",
    "Training Platform": "Platforms & DevOps",
    "CI/CD for ML": "Platforms & DevOps",
    "Simplification & Automation": "Platforms & DevOps",
    "Knowledge Sharing": "Platforms & DevOps",
    "Dataset & Experiment Sharing": "Platforms & DevOps",
    "Cron Job Monitoring": "Platforms & DevOps",
}

def refactor_categories(input_file='tools.json', output_file='tools_refactored.json'):
    with open(input_file, 'r') as f:
        tools = json.load(f)

    for tool in tools:
        orig_cat = tool.get('category')
        if orig_cat in category_mapping:
            tool['category'] = category_mapping[orig_cat]
        else:
            # Leave unchanged if no mapping exists
            print(f"Warning: no mapping for category '{orig_cat}'")

    with open(output_file, 'w') as f:
        json.dump(tools, f, indent=2)

    print(f"Refactored categories written to {output_file}")

if __name__ == '__main__':
    refactor_categories()
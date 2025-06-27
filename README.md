# System Analysis & Design Workshops

## Workshop 1. Kaggle Systems Engineering Analysis
The selected case study for this workshop involved a Kaggle competition centered on Grupo Bimbo Inventory Demand. Using systems engineering methodology, we first conceptualized the competition framework as an interconnected system before analyzing its emergent properties, particularly focusing on system sensitivity metrics and chaos theory applications in the AI training environment.
- [Workshop 1](./Workshop_1/Workshop_1.pdf)

## Workshop 2. Kaggle Competition System Design

This repository contains the comprehensive system design developed as part of Workshop #2 for the Systems Analysis & Design course (2025-I), instructed by Eng. Carlos Andrés Sierra, MSc, at Universidad Distrital Francisco José de Caldas. The focus of this workshop was the "Grupo Bimbo Inventory Demand" Kaggle competition, aimed at creating accurate weekly demand forecasts to optimize the supply chain of Mexico's largest baked goods distributor.

### Development Process

The development of this system design involved the following structured steps:

1. Analysis of Competition and Requirements

- Reviewed and analyzed the competition description, datasets, and winning solutions on Kaggle.
- Identified key challenges including large data volumes, noisy data, and the requirement for precise forecasting.

2. System Requirements Specification

- Defined comprehensive functional and non-functional requirements to handle data ingestion, preprocessing, feature engineering, model training, and validation.
- Addressed critical aspects like reproducibility, scalability, modularity, and sensitivity to data variations.

3. System Architecture

- Designed a modular and scalable system architecture.
- Each component was described in detail, focusing on their roles, responsibilities, and the flow of data between modules.

4. Technical Stack and Implementation

- Selected Python exclusively to ensure consistency, ease of use, and robust support from the data science community.
- Identified key libraries including Pandas, NumPy, XGBoost, SciPy, and scikit-learn for feature engineering and modeling.

5. Sensitivity and Chaos Management

- Addressed high-sensitivity factors such as lagged predictions, sparse data, outliers, and sequential drift.
- Implemented controlled feature engineering, sequential validation, noise mitigation, regularization, and comprehensive monitoring and logging.

Final Documentation

The complete and detailed system design report can be accessed below:
- [Workshop 2](./Workshop_2/Workshop_2.pdf)

# Workshop 3 - Grupo Bimbo Inventory Demand Simulation

This repository contains the computational simulation for the [Grupo Bimbo Inventory Demand](https://www.kaggle.com/competitions/grupo-bimbo-inventory-demand) competition, validating the system design from Workshop #2 through data-driven experiments. Key components:

- **Data pipeline** cleaning and feature engineering
- **XGBoost model** for demand forecasting
- **Chaos testing** with noise injection
- **Performance analysis** (RMSE, robustness)
## ⚠ Usage Note

The dataset `train.csv` must be downloaded manually from [Kaggle](https://www.kaggle.com/competitions/grupo-bimbo-inventory-demand/data?select=train.csv.zip) and placed in the simulation folder (excluded from Git due to size).

---
The simulation report and code can be accessed below:
- [Simulation Report PDF](./Workshop_3_Simulation/Workshop3Report.pdf)
- [Notebook Code and Requirements](./Workshop_3_Simulation)

# AI Dashboard — Architecture

## 1. Architecture Overview

AI Dashboard follows a layered and modular architecture designed
to separate user interface, application coordination, business
services, and data sources.

## 2. High-Level Flow

User
↓
Dashboard UI
↓
Application Layer
↓
Application Services
↓
Data Sources
↓
Application Services
↓
Dashboard UI

## 3. Main Components

### Entry Point

`main.py`

Responsible for starting the application and initializing the
application environment.

### Application Layer

Coordinates the major application components and controls the
application lifecycle.

### Dashboard UI

Built using PySide6.

Responsible for displaying information and receiving user actions.

### Application Services

Services handle specific responsibilities:

- System Service
- Time Service
- Learning Service

### Data Sources

Initial data sources include:

- Windows/system information through `psutil`
- Python system time
- Local JSON learning data

## 4. Architecture Principle

Each component should have a clear responsibility.

The UI should not directly implement system monitoring,
data storage, or other business logic.

Communication should occur through appropriate application
services.

## 5. Initial Data Flow

User
→ Dashboard UI
→ Application Layer
→ Appropriate Service
→ Data Source
→ Service
→ Dashboard UI
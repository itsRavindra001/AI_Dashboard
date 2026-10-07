# AI Dashboard — Requirements

## 1. Project Overview

AI Dashboard is a Windows desktop application that provides a balanced
workspace for system monitoring, productivity, and AI/ML learning.

The application will be developed incrementally using a professional
software development approach.

---

## 2. Main Goals

The application should:

- Monitor important system information.
- Provide useful productivity features.
- Track AI/ML learning progress.
- Present information through a clean desktop interface.
- Be modular and easy to extend.
- Serve as a practical AI/ML engineering portfolio project.

---

## 3. MVP — Version 0.1

### 3.1 System Monitoring

The dashboard should display:

- CPU usage
- RAM usage
- Storage usage

### 3.2 Time

The dashboard should display:

- Current time
- Current date

The time should update automatically.

### 3.3 Learning Progress

The dashboard should display:

- Current learning goal
- Learning progress percentage

### 3.4 Settings

The application should provide basic settings for dashboard preferences.

---

## 4. Future Features

The following features are planned for later versions:

- Weather information
- Focus timer
- GPU monitoring
- Advanced learning tracker
- AI assistant
- Live wallpaper / desktop integration

These features are outside the MVP.

---

## 5. High-Level Architecture Principle

The application should follow separation of concerns.

The user interface should not directly handle all data collection.

Example:

UI → Service → Data Source → Service → UI

---

## 6. Target Platform

Primary platform:

- Windows Desktop

---

## 7. Development Approach

The project will follow:

Problem
→ Requirements
→ Architecture
→ Implementation
→ Testing
→ Deployment

Git and GitHub will be used throughout development.

Important development milestones should be committed to Git.

---

## 8. Technology Requirements

### Programming Language

- Python 3.12

### Desktop UI

- PySide6 (Qt for Python)

### System Monitoring

- psutil

### Local Data Storage

- JSON for the initial version

### Version Control

- Git

### Remote Repository

- GitHub

### Target Platform

- Windows
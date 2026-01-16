# HY-Chat (한양챗)

## Overview

HY-Chat is a Streamlit-based web application designed for Hanyang University. The application appears to be a chat or information interface with a professional Korean university branding, featuring interactive data visualizations and a tabbed interface design. The project uses Hanyang University's signature blue color (#0E4A84) throughout its styling.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Framework
- **Streamlit**: Chosen as the primary web framework for rapid prototyping and data-driven applications
  - Provides built-in widgets, layouts, and state management
  - Wide layout configuration for better content display
  - Expandable sidebar for navigation/settings

### Visualization Layer
- **Plotly (Graph Objects & Express)**: Used for interactive data visualizations
  - Supports complex, interactive charts
  - Works seamlessly with Streamlit's rendering

### Styling Approach
- Custom CSS injected via `st.markdown()` for university branding
- Gradient-based card designs for scholarship information
- Tab-based navigation with custom styling overrides

### Application Structure
- Single-file architecture (`app.py`) containing all application logic
- `main.py` exists as a placeholder/entry point but is not the primary application

## External Dependencies

### Python Packages
- **streamlit**: Web application framework
- **plotly**: Interactive charting library (graph_objects and express modules)

### Standard Library Usage
- `random`: For generating random data/content
- `time`: For timing operations
- `datetime`: For date/time handling

### No External Services Currently Integrated
- No database connections detected
- No external API integrations
- No authentication system implemented
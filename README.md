# Data Lineage Tracking System

This project implements a comprehensive data lineage tracking system using Neo4j for graph data storage, Flask for the backend API, and React for the frontend user interface.

## Features

- Data source ingestion and tracking
- ETL process monitoring
- Machine learning model versioning and performance tracking
- Output tracking and data lineage visualization
- User authentication and authorization
- Interactive data lineage graph exploration

## Project Structure

```
project_root/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes/
│   │   ├── models/
│   │   └── utils/
│   ├── config.py
│   └── run.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.js
│   │   └── index.js
│   └── package.json
├── tests/
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.8+
- Node.js 14+
- Neo4j 4.0+

### Backend Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/data-lineage-tracking.git
   cd data-lineage-tracking
   ```

2. Set up a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables (see `config.py` for required variables)

5. Run the Flask development server:
   ```
   cd backend
   python run.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install Node.js dependencies:
   ```
   npm install
   ```

3. Install additional required packages:
   ```
   npm install axios react-router-dom @material-ui/core d3
   ```

4. Start the React development server:
   ```
   npm start
   ```

## Usage

After setting up both the backend and frontend, you can access the application by opening a web browser and navigating to `http://localhost:3000`.

## Development

To continue development:

1. Backend: Add new routes in the `backend/app/routes/` directory and update `backend/app/__init__.py` to register new blueprints.

2. Frontend: Add new components in the `frontend/src/components/` directory and update routing in `frontend/src/App.js`.

## Testing

Run backend tests:
```
python -m pytest tests/
```

Run frontend tests:
```
cd frontend
npm test
```

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
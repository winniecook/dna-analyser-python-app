# DNA Sequence Analyzer

A comprehensive DNA sequence analysis tool that provides various analytical features through both a web interface and command-line workflow. This project combines a Flask web application with Nextflow workflows for scalable DNA sequence analysis.

## Features

- Interactive web interface for DNA analysis
- Command-line workflow support using Nextflow
- Containerized application using Docker
- Analysis capabilities:
  - Nucleotide frequency analysis
  - GC content calculation
  - Complementary sequence generation
  - Open Reading Frame (ORF) identification
  - Restriction enzyme cut site detection

## Technology Stack

- Python 3.9+
- Flask (Web Framework)
- Nextflow (Workflow Management)
- Docker (Containerization)
- JavaScript/Chart.js (Frontend Visualization)

## Quick Start

### Using Docker

```bash
# Build the Docker image
docker build -t dna-analyzer .

# Run the web application
docker run -p 5000:5000 dna-analyzer
```

### Using Nextflow Pipeline

```bash
# Install Nextflow
curl -s https://get.nextflow.io | bash

# Run the workflow
nextflow run main.nf --input "path/to/sequences.fasta" --outdir "results"
```

## Project Structure

```
dna-analyzer/
├── app/
│   ├── static/
│   │   ├── styles.css
│   │   └── script.js
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   └── dna_analyzer.py
├── nextflow/
│   ├── main.nf
│   └── nextflow.config
├── docker/
│   └── Dockerfile
├── tests/
│   └── test_dna_analyzer.py
├── .gitignore
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/dna-analyzer.git
   cd dna-analyzer
   ```

2. Choose your preferred method:

   ### Local Development
   ```bash
   python -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   python app/app.py
   ```

   ### Docker Deployment
   ```bash
   docker-compose up --build
   ```

   ### Nextflow Workflow
   ```bash
   nextflow run main.nf --help
   ```

## Workflow Usage

The Nextflow workflow supports both single and batch sequence analysis:

```bash
# Analyze a single sequence
nextflow run main.nf --input "sequence.fasta"

# Analyze multiple sequences
nextflow run main.nf --input "sequences/*.fasta"

# Specify output directory
nextflow run main.nf --input "sequence.fasta" --outdir "my_results"
```

## Configuration

### Docker Configuration
Environment variables can be set in `docker-compose.yml` or passed at runtime:
```bash
docker run -p 5000:5000 -e DEBUG=1 dna-analyzer
```

### Nextflow Configuration
Workflow settings can be modified in `nextflow.config` or passed as parameters:
```bash
nextflow run main.nf --input "sequence.fasta" --threads 4
```

## Testing

```bash
# Run unit tests
python -m pytest tests/

# Run tests in Docker
docker-compose run app python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
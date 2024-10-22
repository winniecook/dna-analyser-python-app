// Default parameters
params {
    input = false
    outdir = "results"
}

// Process configuration
process {
    container = 'dna-analyzer'
}

// Docker configuration
docker {
    enabled = true
    runOptions = '-u $(id -u):$(id -g)'
}

// Execution reports
report {
    enabled = true
    file = "${params.outdir}/reports/execution_report.html"
}

timeline {
    enabled = true
    file = "${params.outdir}/reports/timeline.html"
}

dag {
    enabled = true
    file = "${params.outdir}/reports/dag.html"
}

// Manifest
manifest {
    name = 'DNA Analyzer Pipeline'
    author = 'Your Name'
    description = 'Pipeline for DNA sequence analysis'
    version = '1.0.0'
    nextflowVersion = '>=21.04.0'
}
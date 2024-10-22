#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

// Parameters
params.input = false
params.outdir = "results"

// Input validation
if (!params.input) {
    error "Please provide an input file with --input"
}

// Process definition
process analyzeDNA {
    publishDir "${params.outdir}/analysis", mode: 'copy'
    
    input:
    path sequence

    output:
    path "*_analysis.json"
    path "*_report.html"
    
    script:
    """
    #!/usr/bin/env python3
    
    from Bio import SeqIO
    import json
    from pathlib import Path
    
    def analyze_sequence(seq):
        # Basic sequence analysis
        analysis = {
            'length': len(seq),
            'gc_content': (seq.count('G') + seq.count('C')) / len(seq) * 100,
            'nucleotides': {
                'A': seq.count('A'),
                'T': seq.count('T'),
                'G': seq.count('G'),
                'C': seq.count('C')
            }
        }
        return analysis

    # Read sequence file - using the actual input variable
    sequences = []
    for record in SeqIO.parse("$sequence", "fasta"):
        seq = str(record.seq)
        analysis = analyze_sequence(seq)
        sequences.append({
            'id': record.id,
            'analysis': analysis
        })
    
    # Write JSON output - using the sequence basename
    with open("${sequence.baseName}_analysis.json", 'w') as f:
        json.dump(sequences, f, indent=4)
    
    # Create HTML report
    html_content = "<html><body>"
    html_content += "<h1>DNA Analysis Report</h1>"
    for seq in sequences:
        html_content += f"<h2>Sequence: {seq['id']}</h2>"
        html_content += f"<pre>{json.dumps(seq['analysis'], indent=4)}</pre>"
    html_content += "</body></html>"
    
    with open("${sequence.baseName}_report.html", 'w') as f:
        f.write(html_content)
    """
}

// Workflow definition
workflow {
    // Create input channel
    sequences_ch = Channel.fromPath(params.input)
    
    // Execute analysis
    analyzeDNA(sequences_ch)
}
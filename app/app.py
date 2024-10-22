from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
import re

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

logging.basicConfig(level=logging.DEBUG)

def is_valid_dna(sequence):
    return set(sequence.upper()).issubset({'A', 'T', 'C', 'G'})

def analyze_dna(sequence):
    sequence = sequence.upper()
    
    # Calculate nucleotide frequency
    nucleotide_count = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'C': sequence.count('C'),
        'G': sequence.count('G')
    }
    
    # Calculate GC content
    gc_content = (nucleotide_count['G'] + nucleotide_count['C']) / len(sequence) * 100
    
    # Find complementary sequence
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complementary_sequence = ''.join(complement[base] for base in sequence)
    
    # Find open reading frames (ORFs)
    orfs = find_orfs(sequence)
    
    # Identify restriction enzyme cut sites
    restriction_sites = find_restriction_sites(sequence)
    
    return {
        'nucleotide_count': nucleotide_count,
        'gc_content': round(gc_content, 2),
        'complementary_sequence': complementary_sequence,
        'orfs': orfs,
        'restriction_sites': restriction_sites
    }

def find_orfs(sequence):
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    orfs = []

    for frame in range(3):
        for match in re.finditer(f'(?={start_codon})', sequence[frame:]):
            start = match.start() + frame
            for i in range(start + 3, len(sequence), 3):
                codon = sequence[i:i+3]
                if codon in stop_codons:
                    orfs.append({
                        'start': start,
                        'end': i + 2,
                        'length': i + 3 - start,
                        'sequence': sequence[start:i+3]
                    })
                    break

    return orfs

def find_restriction_sites(sequence):
    restriction_enzymes = {
        'EcoRI': 'GAATTC',
        'BamHI': 'GGATCC',
        'HindIII': 'AAGCTT',
        'NotI': 'GCGGCCGC'
    }
    
    sites = {}
    for enzyme, site in restriction_enzymes.items():
        positions = [m.start() for m in re.finditer(f'(?={site})', sequence)]
        if positions:
            sites[enzyme] = positions
    
    return sites

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    sequence = data.get('sequence', '')
    
    if not is_valid_dna(sequence):
        return jsonify({"error": "Invalid DNA sequence. Please enter a valid sequence containing only A, T, C, and G."}), 400
    
    results = analyze_dna(sequence)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
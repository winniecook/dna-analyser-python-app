document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const dnaInput = document.getElementById('dna-input');
    const errorMessage = document.getElementById('error-message');
    const results = document.getElementById('results');
    const textResults = document.getElementById('text-results');

    let nucleotideChart, gcContentChart;

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.style.display = 'block';
        results.style.display = 'none';
    }

    function hideError() {
        errorMessage.style.display = 'none';
        results.style.display = 'block';
    }

    analyzeBtn.addEventListener('click', async () => {
        const sequence = dnaInput.value.trim();
        if (sequence === '') {
            showError('Please enter a DNA sequence.');
            return;
        }

        try {
            const response = await fetch('http://localhost:5000/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ sequence })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            hideError();
            displayResults(data);
        } catch (error) {
            showError(`An error occurred: ${error.message}`);
        }
    });

    function displayResults(data) {
        updateNucleotideChart(data.nucleotide_count);
        updateGCContentChart(data.gc_content);
        displayTextResults(data);
    }

    function updateNucleotideChart(nucleotideCount) {
        const ctx = document.getElementById('nucleotide-chart').getContext('2d');
        
        if (nucleotideChart) {
            nucleotideChart.destroy();
        }

        nucleotideChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels:
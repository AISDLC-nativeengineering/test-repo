// Citizen Crime Reporting

function CrimeReport() {
    // Render form and submission logic
    const submitReport = async (reportData) => {
        try {
            const response = await fetch('/api/crime', {
                method: 'POST',
                body: JSON.stringify(reportData),
                headers: { 'Content-Type': 'application/json' }
            });

            if (!response.ok) {
                throw new Error('Submission failure');
            }

            const confirmation = await response.json();
            alert(`Report submitted successfully: ${confirmation.message}`);
        } catch (error) {
            alert(`Error: ${error.message}`);
        }
    };

    // Return UI components
    return (
        <div>
            <h1>Report a Crime</h1>
            <form onSubmit={(e) => {
                e.preventDefault();
                const reportData = { crime: e.target.elements.crime.value };
                submitReport(reportData);
            }}>
                <label>Crime: <input name="crime" /></label>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default CrimeReport;
import express from 'express';

const router = express.Router();

// Mock data for summary endpoint
const mockSummaryData = {
  passRate: 85,
  defectRate: 10,
  executionTime: { mean: 45, median: 40 },
};

/**
 * GET /api/reports/summary
 * Fetch summarized test execution metrics
 */
router.get('/api/reports/summary', (req, res) => {
  const { testSuiteId, dateRange } = req.query;

  if (!testSuiteId || !dateRange) {
    return res.status(400).json({ error: 'Missing required parameters: testSuiteId and dateRange' });
  }

  // Simulate a successful response with mocked data
  res.status(200).json(mockSummaryData);
});

/**
 * POST /api/reports/detailed
 * Generate a downloadable PDF report
 */
router.post('/api/reports/detailed', (req, res) => {
  const { testSuiteId, dateRange } = req.body;

  if (!testSuiteId || !dateRange) {
    return res.status(400).json({ error: 'Missing required body parameters: testSuiteId and dateRange' });
  }

  // Simulate PDF generation logic
  res.status(200).json({ message: 'PDF report generated and available for download' });
});

export default router;

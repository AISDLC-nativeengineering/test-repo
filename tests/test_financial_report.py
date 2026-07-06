import unittest
from unittest.mock import patch, mock_open
import os
import pandas as pd
from src.financial_report import FinancialReport

class TestFinancialReport(unittest.TestCase):
    def setUp(self):
        self.dataset_path = 'test_data.csv'
        self.report = FinancialReport(self.dataset_path)

    @patch('pandas.read_csv')
    def test_load_data(self, mock_read_csv):
        mock_data = pd.DataFrame({
            'Category': ['A', 'B'],
            'Actual': [100, 200],
            'Planned': [50, 150]
        })
        mock_read_csv.return_value = mock_data

        self.report.load_data()
        self.assertIsNotNone(self.report.data)
        self.assertEqual(list(self.report.data.columns), ['Category', 'Actual', 'Planned'])

    def test_compute_variance(self):
        self.report.data = pd.DataFrame({
            'Category': ['A', 'B'],
            'Actual': [100, 200],
            'Planned': [50, 150]
        })
        self.report.compute_variance()

        self.assertIn('Variance', self.report.data.columns)
        self.assertEqual(list(self.report.data['Variance']), [50, 50])

    @patch('matplotlib.pyplot.savefig')
    def test_generate_visualization(self, mock_savefig):
        self.report.data = pd.DataFrame({
            'Category': ['A', 'B'],
            'Actual': [100, 200],
            'Planned': [50, 150],
            'Variance': [50, 50]
        })

        output_path = 'test_visualization.png'
        self.report.generate_visualization(output_path)
        mock_savefig.assert_called_once_with(output_path)

    @patch('matplotlib.backends.backend_pdf.PdfPages')
    @patch('pandas.DataFrame.to_excel')
    def test_export_report_pdf(self, mock_to_excel, mock_pdf_pages):
        self.report.data = pd.DataFrame({
            'Category': ['A', 'B'],
            'Actual': [100, 200],
            'Planned': [50, 150],
            'Variance': [50, 50]
        })

        output_path_pdf = 'test_report.pdf'
        self.report.export_report(format='pdf', output_path=output_path_pdf)
        mock_pdf_pages.assert_called_once()

    def test_export_report_excel(self):
        self.report.data = pd.DataFrame({
            'Category': ['A', 'B'],
            'Actual': [100, 200],
            'Planned': [50, 150],
            'Variance': [50, 50]
        })

        with patch('pandas.DataFrame.to_excel') as mock_to_excel:
            output_path_excel = 'test_report.xlsx'
            self.report.export_report(format='excel', output_path=output_path_excel)
            mock_to_excel.assert_called_once_with(output_path_excel, index=False)

    def test_unsupported_export_format(self):
        self.report.data = pd.DataFrame()
        with self.assertRaises(ValueError):
            self.report.export_report(format='txt', output_path='unsupported.txt')

    def test_error_no_loaded_data(self):
        with self.assertRaises(ValueError):
            self.report.compute_variance()

        with self.assertRaises(ValueError):
            self.report.generate_visualization(output_path='test.png')

if __name__ == '__main__':
    unittest.main()
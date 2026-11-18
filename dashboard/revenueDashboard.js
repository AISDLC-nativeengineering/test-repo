// Revenue Dashboard

// Function to fetch mock revenue data
const fetchMockRevenueData = () => {
  return {
    totalRevenue: 1000000,
    revenueTrend: [
      { date: '2023-01-01', revenue: 50000 },
      { date: '2023-01-02', revenue: 55000 },
      { date: '2023-01-03', revenue: 60000 }
    ],
    growth: '5%',
    revenueStreams: [
      { stream: 'Product A', amount: 400000, share: '40%' },
      { stream: 'Product B', amount: 300000, share: '30%' },
      { stream: 'Service C', amount: 300000, share: '30%' }
    ]
  };
};

// Function to display total revenue
const displayTotalRevenue = (data) => {
  console.log(`Total Revenue: $${data.totalRevenue}`);
};

// Function to display revenue trend
const displayRevenueTrend = (data) => {
  console.log('Revenue Trend:');
  data.revenueTrend.forEach((item) => {
    console.log(`${item.date}: $${item.revenue}`);
  });
};

// Function to display growth metrics
const displayGrowthMetrics = (data) => {
  console.log(`Growth: ${data.growth}`);
};

// Function to display revenue breakdown by streams
const displayRevenueStreams = (data) => {
  console.log('Revenue Streams:');
  data.revenueStreams.forEach((stream) => {
    console.log(`${stream.stream}: $${stream.amount} (${stream.share})`);
  });
};

// Main function to render dashboard
const renderRevenueDashboard = () => {
  const revenueData = fetchMockRevenueData();

  displayTotalRevenue(revenueData);
  displayRevenueTrend(revenueData);
  displayGrowthMetrics(revenueData);
  displayRevenueStreams(revenueData);
};

// Render the dashboard
renderRevenueDashboard();
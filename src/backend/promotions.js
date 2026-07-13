const express = require('express');
const router = express.Router();

const promotionsData = [
  { id: 'promo1', title: 'Summer Sale', description: 'Discount on summer items', imageURL: 'promo_url_1', link: 'link_1' },
  { id: 'promo2', title: 'Back-to-School', description: 'Discount on educational items', imageURL: 'promo_url_2', link: 'link_2' }
];

router.get('/promotions', (req, res) => {
  res.json(promotionsData);
});

module.exports = router;
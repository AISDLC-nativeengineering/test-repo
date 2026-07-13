import React from 'react';
import { BrowserRouter as Router, Link } from 'react-router-dom';

const Homepage = () => {
  const collections = ['age', 'season', 'occasion'];
  const promotions = [
    { id: 'promo1', title: 'Summer Sale', description: 'Discount on summer items', imageURL: 'promo_url_1', link: 'link_1' },
    { id: 'promo2', title: 'Back-to-School', description: 'Discount on educational items', imageURL: 'promo_url_2', link: 'link_2' }
  ];

  return (
    <Router>
      <div>
        <h1>Homepage</h1>

        <section>
          <h2>Curated Collections</h2>
          <ul>
            {collections.map((category) => (
              <li key={category}>
                <Link to={`/collections/${category}`}>{category}</Link>
              </li>
            ))}
          </ul>
        </section>

        <section>
          <h2>Subscription Offers</h2>
          <div>
            {promotions.map((promo) => (
              <div key={promo.id}>
                <img src={promo.imageURL} alt={promo.title} />
                <h3>{promo.title}</h3>
                <p>{promo.description}</p>
                <a href={promo.link}>Learn More</a>
              </div>
            ))}
          </div>
        </section>
      </div>
    </Router>
  );
};

export default Homepage;
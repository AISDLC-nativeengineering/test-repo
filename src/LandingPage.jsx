import React from 'react';
import './LandingPage.scss';

const LandingPage = () => {
  return (
    <div className="landing-page">
      <header className="landing-page__header">
        <h1>Welcome to the Employee Discounts</h1>
      </header>
      <main className="landing-page__content">
        <section className="discount-highlights">
          <h2>Key Benefits</h2>
          <ul>
            <li>Amazing discounts on electronics</li>
            <li>Special offers on travel packages</li>
            <li>Seasonal sales on apparel</li>
          </ul>
        </section>
      </main>
    </div>
  );
};

export default LandingPage;

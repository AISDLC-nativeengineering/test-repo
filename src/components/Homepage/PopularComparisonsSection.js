import React from 'react';

const PopularComparisonsSection = ({ comparisons }) => {
  return (
    <div>
      <h2>Popular Comparisons</h2>
      <ul style={{
        listStyleType: 'none',
        padding: 0
      }}>
        {comparisons.map((comparison) => (
          <li key={comparison.id}>
            {comparison.title}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PopularComparisonsSection;
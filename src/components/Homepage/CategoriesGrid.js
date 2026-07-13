import React from 'react';

const CategoriesGrid = ({ categories }) => {
  return (
    <div style={{
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fill, minmax(100px, 1fr))',
      gap: '20px'
    }}>
      {categories.map((category) => (
        <div key={category.id} style={{
          padding: '10px',
          border: '1px solid lightgray',
          borderRadius: '5px'
        }}>
          {category.name}
        </div>
      ))}
    </div>
  );
};

export default CategoriesGrid;
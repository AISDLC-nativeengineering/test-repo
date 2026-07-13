import React from 'react';

const SearchBar = ({ placeholder }) => {
  return (
    <input 
      type="text" 
      placeholder={placeholder} 
      style={{
        padding: '10px',
        width: '100%',
        borderRadius: '5px',
      }}
    />
  );
};

export default SearchBar;
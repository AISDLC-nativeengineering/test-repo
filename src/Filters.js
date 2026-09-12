import React, { useState } from 'react';

const Filters = ({ onFilter }) => {
  const [filterCriteria, setFilterCriteria] = useState({
    type: '',
    riskScoreMin: '',
    riskScoreMax: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilterCriteria({ ...filterCriteria, [name]: value });
  };

  const applyFilters = () => {
    onFilter(filterCriteria);
  };

  return (
    <div>
      <h2>Filters</h2>
      <label>
        Type:
        <input
          type="text"
          name="type"
          value={filterCriteria.type}
          onChange={handleChange}
        />
      </label>
      <label>
        Risk Score Minimum:
        <input
          type="number"
          name="riskScoreMin"
          value={filterCriteria.riskScoreMin}
          onChange={handleChange}
        />
      </label>
      <label>
        Risk Score Maximum:
        <input
          type="number"
          name="riskScoreMax"
          value={filterCriteria.riskScoreMax}
          onChange={handleChange}
        />
      </label>
      <button onClick={applyFilters}>Apply Filters</button>
    </div>
  );
};

export default Filters;
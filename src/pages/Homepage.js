import React, { useState, useEffect } from 'react';
import SearchBar from '../components/Homepage/SearchBar';
import NavigationMenu from '../components/Homepage/NavigationMenu';
import PopularComparisonsSection from '../components/Homepage/PopularComparisonsSection';
import CategoriesGrid from '../components/Homepage/CategoriesGrid';

const Homepage = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    // Fetch homepage data
    fetch('/homepage-data')
      .then((response) => response.json())
      .then((json) => setData(json))
      .catch((error) => console.error('Failed to load homepage data', error));
  }, []);

  if (!data) {
    return <p>Loading...</p>;
  }

  return (
    <div style={{
      padding: '20px'
    }}>
      <SearchBar placeholder={data.searchPlaceholder} />
      <NavigationMenu links={[
        { label: 'Home', url: '/' },
        { label: 'About', url: '/about' }
      ]} />
      <PopularComparisonsSection comparisons={data.popularComparisons} />
      <CategoriesGrid categories={data.categories} />
    </div>
  );
};

export default Homepage;
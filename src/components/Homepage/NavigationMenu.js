import React from 'react';

const NavigationMenu = ({ links }) => {
  return (
    <nav>
      <ul style={{
        display: 'flex',
        listStyleType: 'none',
        gap: '15px'
      }}>
        {links.map((link, index) => (
          <li key={index}>
            <a href={link.url} style={{ textDecoration: 'none', color: 'blue' }}>
              {link.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default NavigationMenu;
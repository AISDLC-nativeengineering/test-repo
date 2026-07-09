// cacheService.js

/**
 * Caching service to manage local translations.
 * Uses in-browser localStorage for persistence.
 */

const cacheKeyPrefix = 'translationCache:';

/**
 * Save translation to cache.
 * @param {string} text - Text to save.
 * @param {string} language - Language code.
 * @param {string} translation - Translated text.
 */
function saveToCache(text, language, translation) {
  const key = `${cacheKeyPrefix}${text}:${language}`;
  localStorage.setItem(key, translation);
}

/**
 * Retrieve translation from cache.
 * @param {string} text - Text.
 * @param {string} language - Language code.
 * @returns {string|null} Cached translation or null.
 */
function getFromCache(text, language) {
  const key = `${cacheKeyPrefix}${text}:${language}`;
  return localStorage.getItem(key);
}

module.exports = {
  saveToCache,
  getFromCache,
};
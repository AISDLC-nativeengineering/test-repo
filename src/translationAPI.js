// translationAPI.js

/**
 * This module provides runtime translation using Google Translate API.
 * Implements support for caching and fallback mechanisms.
 */

const axios = require('axios');

const TRANSLATION_API_URL = 'https://translation.googleapis.com/language/translate/v2';
const API_KEY = 'your-api-key';

// In-memory cache for translations
const translationCache = new Map();

/**
 * Fetch translation for the given text.
 * @param {string} text - Text to translate.
 * @param {string} targetLanguage - Target language code.
 * @returns {Promise<string>} Translated text.
 */
async function getTranslation(text, targetLanguage) {
  const cacheKey = `${text}:${targetLanguage}`;

  if (translationCache.has(cacheKey)) {
    return translationCache.get(cacheKey);
  }

  try {
    const response = await axios.post(`${TRANSLATION_API_URL}`, {
      q: text,
      target: targetLanguage,
      key: API_KEY,
    });

    const translatedText = response.data.data.translations[0].translatedText;

    // Cache the result
    translationCache.set(cacheKey, translatedText);

    return translatedText;
  } catch (error) {
    console.error('Translation API error:', error);

    // Fallback to original text
    return text;
  }
}

module.exports = {
  getTranslation,
};
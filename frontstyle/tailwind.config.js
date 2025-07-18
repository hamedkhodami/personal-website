/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      "../src/templates/**/*.html",
      "../src/static/assets/public/js/*.js",
  ],
  theme: {
    extend: {
      colors: {
        primary: '#6366F1',
        secondary: '#E2E8F0',
        accountForm: '#F9FFF1',
        errorRed: '#FF0000',
      },
      backgroundImage: {
        'gradient-blue-gray': 'linear-gradient(to right, #4A90E2, #E2E8F0)',
        'gradient-green-blue': 'linear-gradient(to right, #43AA8B, #577590)',
        'gradient-red-yellow': 'linear-gradient(to right, #FF686B, #FFD166)',
      },
    },
  },
  plugins: [],
};



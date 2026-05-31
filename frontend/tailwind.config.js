/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', 'sans-serif']
      },
      colors: {
        ink: '#101828',
        cloud: '#f7f8fb',
        brand: {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#2f80ed',
          600: '#1f6bd1',
          900: '#12325c'
        },
        mint: '#22c55e',
        coral: '#fb7185',
        amber: '#f59e0b'
      },
      boxShadow: {
        soft: '0 18px 55px rgba(16, 24, 40, 0.09)',
        glass: '0 20px 70px rgba(15, 23, 42, 0.13)'
      }
    }
  },
  plugins: []
};

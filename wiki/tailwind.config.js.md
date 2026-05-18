# tailwind.config.js

Source: junk_drawer/github/PersonalWebsite/tailwind.config.js.txt

Category: [[github-code]]

## Summary
/** @type {import('tailwindcss').Config} */ module.exports = { darkMode: ['class'], content: [ './src/pages/**/*.{js,ts,jsx,tsx,mdx}', './src/components/**/*.{js,ts,jsx,tsx,mdx}', './src/app/**/*.{js,ts,jsx,tsx,mdx}', ], theme: { extend: {

## Full Content
/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ['class'],
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        // Add your custom colors here
        gray: {
          50: '#f9fafb',
          100: '#f3f4f6',
          200: '#e5e7eb',
          300: '#d1d5db',
          400: '#9ca3af',
          500: '#6b7280',
          600: '#4b5563',
          700: '#374151',
          800: '#1f2937',
          900: '#111827',
        },
      },
      backgroundColor: {
        dark: '#0a0a0a',
      },
      textColor: {
        dark: '#ededed',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/tailwind.config.js.txt
- Extracted: 2026-05-18
- Category: github-code

# layout.js

Source: junk_drawer/github/PersonalWebsite/src/app/layout.js.txt

Category: [[github-code]]

## Summary
import './globals.css'; export const metadata = { title: 'Jose Maria Barbeito', description: 'Personal website of Jose Maria Barbeito', icons: { icon: '/favicon.ico', }, };

## Full Content
import './globals.css';

export const metadata = {
  title: 'Jose Maria Barbeito',
  description: 'Personal website of Jose Maria Barbeito',
  icons: {
    icon: '/favicon.ico',
  },
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <meta charSet="utf-8" />
      </head>
      <body>
        {children}
      </body>
    </html>
  );
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/app/layout.js.txt
- Extracted: 2026-05-18
- Category: github-code

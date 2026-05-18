# copy-assets.js

Source: junk_drawer/github/PersonalWebsite/scripts/copy-assets.js.txt

Category: [[github-code]]

## Summary
const fs = require('fs-extra'); const path = require('path'); // Define source and destination paths const srcDir = path.join(__dirname, '..', 'public'); const outDir = path.join(__dirname, '..', 'out'); // Ensure the output directory exists fs.ensureDirSync(outDir);

## Full Content
const fs = require('fs-extra');
const path = require('path');

// Define source and destination paths
const srcDir = path.join(__dirname, '..', 'public');
const outDir = path.join(__dirname, '..', 'out');

// Ensure the output directory exists
fs.ensureDirSync(outDir);

// Create .nojekyll file in the out directory
const noJekyllPath = path.join(outDir, '.nojekyll');
fs.writeFileSync(noJekyllPath, '');
console.log('Created .nojekyll file in the out directory');

// Copy public directory to out directory
fs.copySync(srcDir, outDir, {
  dereference: true,
  filter: (src) => {
    // Skip node_modules and other unnecessary files
    return !src.includes('node_modules') && 
           !src.endsWith('.DS_Store') &&
           !src.endsWith('Thumbs.db');
  }
});

console.log('Successfully copied public assets to out directory');


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/scripts/copy-assets.js.txt
- Extracted: 2026-05-18
- Category: github-code

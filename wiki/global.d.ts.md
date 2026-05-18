# global.d.ts

Source: junk_drawer/github/PersonalWebsite/src/types/global.d.ts.txt

Category: [[github-code]]

## Summary
// Extend the Window interface to include the gc property declare global { interface Window { gc?: () => void; } } export {}; // This file needs to be a module

## Full Content
// Extend the Window interface to include the gc property
declare global {
  interface Window {
    gc?: () => void;
  }
}

export {}; // This file needs to be a module


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/types/global.d.ts.txt
- Extracted: 2026-05-18
- Category: github-code

# updates.ts

Source: junk_drawer/github/PersonalWebsite/src/app/side-quests/foodtree/utils/updates.ts.txt

Category: [[github-code]]

## Summary
import { updates } from '../updates/page'; export function getLatestUpdate() { if (!updates || updates.length === 0) { return { version: '1.0.0', date: new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }) }; }

## Full Content
import { updates } from '../updates/page';

export function getLatestUpdate() {
  if (!updates || updates.length === 0) {
    return {
      version: '1.0.0',
      date: new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    };
  }
  
  // Sort by version number in descending order to get the latest
  const sortedUpdates = [...updates].sort((a, b) => {
    const [aMajor, aMinor, aPatch] = a.version.split('.').map(Number);
    const [bMajor, bMinor, bPatch] = b.version.split('.').map(Number);
    
    if (bMajor !== aMajor) return bMajor - aMajor;
    if (bMinor !== aMinor) return bMinor - aMinor;
    return bPatch - aPatch;
  });

  const latest = sortedUpdates[0];
  return {
    version: latest.version,
    date: latest.date,
    title: latest.title
  };
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/app/side-quests/foodtree/utils/updates.ts.txt
- Extracted: 2026-05-18
- Category: github-code

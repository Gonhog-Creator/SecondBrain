# run.ts

Source: junk_drawer/github/PersonalWebsite/scripts/run.ts.txt

Category: [[github-code]]

## Summary
import { cleanupSubmissions } from './cleanupSubmissions'; async function main() { console.log('Starting submission cleanup...'); await cleanupSubmissions(); console.log('Cleanup completed!'); process.exit(0); } main().catch(console.error);

## Full Content
import { cleanupSubmissions } from './cleanupSubmissions';

async function main() {
  console.log('Starting submission cleanup...');
  await cleanupSubmissions();
  console.log('Cleanup completed!');
  process.exit(0);
}

main().catch(console.error);


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/scripts/run.ts.txt
- Extracted: 2026-05-18
- Category: github-code

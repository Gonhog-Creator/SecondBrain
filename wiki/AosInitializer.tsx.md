# AosInitializer.tsx

Source: junk_drawer/github/PersonalWebsite/src/components/AosInitializer.tsx.txt

Category: [[github-code]]

## Summary
'use client'; import { useEffect } from 'react'; export default function AosInitializer() { useEffect(() => { const initAos = async () => { const AOS = (await import('aos')).default; AOS.init({ duration: 800,

## Full Content
'use client';

import { useEffect } from 'react';

export default function AosInitializer() {
  useEffect(() => {
    const initAos = async () => {
      const AOS = (await import('aos')).default;
      AOS.init({
        duration: 800,
        easing: 'ease-in-out',
        once: true,
      });
    };

    initAos();
  }, []);

  return null;
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/components/AosInitializer.tsx.txt
- Extracted: 2026-05-18
- Category: github-code

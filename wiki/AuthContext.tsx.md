# AuthContext.tsx

Source: junk_drawer/github/PersonalWebsite/src/contexts/AuthContext.tsx.txt

Category: [[github-code]]

## Summary
'use client'; import { SessionProvider } from 'next-auth/react'; import { ReactNode } from 'react'; export function AuthProvider({ children }: { children: ReactNode }) { return <SessionProvider>{children}</SessionProvider>; }

## Full Content
'use client';

import { SessionProvider } from 'next-auth/react';
import { ReactNode } from 'react';

export function AuthProvider({ children }: { children: ReactNode }) {
  return <SessionProvider>{children}</SessionProvider>;
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/contexts/AuthContext.tsx.txt
- Extracted: 2026-05-18
- Category: github-code

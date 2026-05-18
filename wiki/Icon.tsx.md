# Icon.tsx

Source: junk_drawer/github/PersonalWebsite/src/components/ui/Icon.tsx.txt

Category: [[github-code]]

## Summary
'use client'; import { Icon as IconifyIcon } from '@iconify/react'; import { ComponentProps } from 'react'; type IconProps = ComponentProps<typeof IconifyIcon>; export function Icon(props: IconProps) { return <IconifyIcon {...props} />; }

## Full Content
'use client';

import { Icon as IconifyIcon } from '@iconify/react';
import { ComponentProps } from 'react';

type IconProps = ComponentProps<typeof IconifyIcon>;

export function Icon(props: IconProps) {
  return <IconifyIcon {...props} />;
}


## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/components/ui/Icon.tsx.txt
- Extracted: 2026-05-18
- Category: github-code

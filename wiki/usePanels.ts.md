# usePanels.ts

Source: junk_drawer/github/DeltaDash/frontend/src/hooks/usePanels.ts.txt

Category: [[github-code]]

## Summary
import { useQuery } from '@tanstack/react-query'; import { panelsApi } from '../api/panels'; export function usePanels(params?: { skip?: number; limit?: number }) { return useQuery({ queryKey: ['panels', params], queryFn: () => panelsApi.list(params), }); }

## Full Content
import { useQuery } from '@tanstack/react-query';
import { panelsApi } from '../api/panels';

export function usePanels(params?: { skip?: number; limit?: number }) {
  return useQuery({
    queryKey: ['panels', params],
    queryFn: () => panelsApi.list(params),
  });
}


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/hooks/usePanels.ts.txt
- Extracted: 2026-05-18
- Category: github-code

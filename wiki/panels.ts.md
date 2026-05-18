# panels.ts

Source: junk_drawer/github/DeltaDash/frontend/src/api/panels.ts.txt

Category: [[github-code]]

## Summary
import { apiClient } from './client'; export interface Panel { id: string; name: string; vest_type: string | null; created_at: string; updated_at: string; }

## Full Content
import { apiClient } from './client';

export interface Panel {
  id: string;
  name: string;
  vest_type: string | null;
  created_at: string;
  updated_at: string;
}

export const panelsApi = {
  list: (params?: { skip?: number; limit?: number }) => {
    const searchParams = new URLSearchParams();
    if (params?.skip) searchParams.append('skip', params.skip.toString());
    if (params?.limit) searchParams.append('limit', params.limit.toString());
    const query = searchParams.toString();
    return apiClient.get<Panel[]>(`/api/v1/panels${query ? `?${query}` : ''}`);
  },
};


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/api/panels.ts.txt
- Extracted: 2026-05-18
- Category: github-code

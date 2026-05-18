# protocols.ts

Source: junk_drawer/github/DeltaDash/frontend/src/api/protocols.ts.txt

Category: [[github-code]]

## Summary
import { apiClient } from './client'; export interface Protocol { id: string; name: string; description?: string; } export interface ProtocolCreate { name: string;

## Full Content
import { apiClient } from './client';

export interface Protocol {
  id: string;
  name: string;
  description?: string;
}

export interface ProtocolCreate {
  name: string;
  description?: string;
}

export const protocolsApi = {
  list: () => apiClient.get<Protocol[]>('/api/v1/protocols'),

  create: (protocol: ProtocolCreate) => apiClient.post<Protocol>('/api/v1/protocols', protocol),

  get: (id: string) => apiClient.get<Protocol>(`/api/v1/protocols/${id}`),

  update: (id: string, protocol: Partial<ProtocolCreate>) => apiClient.patch<Protocol>(`/api/v1/protocols/${id}`, protocol),

  delete: (id: string) => apiClient.delete<void>(`/api/v1/protocols/${id}`),
};


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/api/protocols.ts.txt
- Extracted: 2026-05-18
- Category: github-code

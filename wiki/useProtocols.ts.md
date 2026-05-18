# useProtocols.ts

Source: junk_drawer/github/DeltaDash/frontend/src/hooks/useProtocols.ts.txt

Category: [[github-code]]

## Summary
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'; import { protocolsApi, ProtocolCreate } from '../api/protocols'; export function useProtocols() { return useQuery({ queryKey: ['protocols'], queryFn: () => protocolsApi.list(), }); }

## Full Content
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { protocolsApi, ProtocolCreate } from '../api/protocols';

export function useProtocols() {
  return useQuery({
    queryKey: ['protocols'],
    queryFn: () => protocolsApi.list(),
  });
}

export function useCreateProtocol() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (protocol: ProtocolCreate) => protocolsApi.create(protocol),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['protocols'] });
    },
  });
}

export function useDeleteProtocol() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: string) => protocolsApi.delete(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['protocols'] });
    },
  });
}

export function useUpdateProtocol() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, protocol }: { id: string; protocol: Partial<ProtocolCreate> }) => 
      protocolsApi.update(id, protocol),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['protocols'] });
    },
  });
}


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/hooks/useProtocols.ts.txt
- Extracted: 2026-05-18
- Category: github-code

# useLocations.ts

Source: junk_drawer/github/DeltaDash/frontend/src/hooks/useLocations.ts.txt

Category: [[github-code]]

## Summary
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'; import { locationsApi, LocationCreate } from '../api/locations'; export function useLocations() { return useQuery({ queryKey: ['locations'], queryFn: () => locationsApi.list(), }); }

## Full Content
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { locationsApi, LocationCreate } from '../api/locations';

export function useLocations() {
  return useQuery({
    queryKey: ['locations'],
    queryFn: () => locationsApi.list(),
  });
}

export function useCreateLocation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (location: LocationCreate) => locationsApi.create(location),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['locations'] });
    },
  });
}

export function useDeleteLocation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: string) => locationsApi.delete(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['locations'] });
    },
  });
}

export function useUpdateLocation() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, location }: { id: string; location: Partial<LocationCreate> }) => 
      locationsApi.update(id, location),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['locations'] });
    },
  });
}


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/hooks/useLocations.ts.txt
- Extracted: 2026-05-18
- Category: github-code

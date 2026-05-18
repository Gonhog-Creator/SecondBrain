# useShotData.ts

Source: junk_drawer/github/DeltaDash/frontend/src/hooks/useShotData.ts.txt

Category: [[github-code]]

## Summary
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'; import { shotDataApi } from '../api/shot_data'; export function useShotData(params?: { skip?: number; limit?: number }) { return useQuery({ queryKey: ['shot_data', params], queryFn: () => shotDataApi.list(params), }); }

## Full Content
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { shotDataApi } from '../api/shot_data';

export function useShotData(params?: { skip?: number; limit?: number }) {
  return useQuery({
    queryKey: ['shot_data', params],
    queryFn: () => shotDataApi.list(params),
  });
}

export function useShotDataByTestSession(testSessionId: string | null) {
  return useQuery({
    queryKey: ['shot_data', 'test_session', testSessionId],
    queryFn: () => shotDataApi.list({ test_session_id: testSessionId || undefined }),
    enabled: !!testSessionId,
  });
}

export function useUpdateShotData() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, shotData }: { id: string; shotData: import('../api/shot_data').ShotDataUpdate }) =>
      shotDataApi.update(id, shotData),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['shot_data'] });
    },
  });
}


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/hooks/useShotData.ts.txt
- Extracted: 2026-05-18
- Category: github-code

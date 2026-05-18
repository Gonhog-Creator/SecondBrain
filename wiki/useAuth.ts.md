# useAuth.ts

Source: junk_drawer/github/DeltaDash/frontend/src/hooks/useAuth.ts.txt

Category: [[github-code]]

## Summary
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'; import { authApi } from '../api/auth'; export function useAuth() { const queryClient = useQueryClient(); const { data: user, isLoading, error } = useQuery({ queryKey: ['currentUser'], queryFn: authApi.getCurrentUser, retry: false,

## Full Content
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { authApi } from '../api/auth';

export function useAuth() {
  const queryClient = useQueryClient();

  const { data: user, isLoading, error } = useQuery({
    queryKey: ['currentUser'],
    queryFn: authApi.getCurrentUser,
    retry: false,
    refetchOnWindowFocus: false,
    refetchOnReconnect: false,
  });

  const loginMutation = useMutation({
    mutationFn: authApi.login,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['currentUser'] });
    },
  });

  const logoutMutation = useMutation({
    mutationFn: authApi.logout,
    onSuccess: () => {
      queryClient.setQueryData(['currentUser'], null);
      queryClient.removeQueries({ queryKey: ['currentUser'] });
    },
  });

  const changePasswordMutation = useMutation({
    mutationFn: ({ oldPassword, newPassword }: { oldPassword: string; newPassword: string }) =>
      authApi.changePassword(oldPassword, newPassword),
  });

  return {
    user,
    isLoading,
    isAuthenticated: !!user,
    isAdmin: user?.is_admin || false,
    error,
    login: loginMutation.mutateAsync,
    logout: logoutMutation.mutateAsync,
    changePassword: changePasswordMutation.mutateAsync,
    isLoggingIn: loginMutation.isPending,
    isLoggingOut: logoutMutation.isPending,
  };
}


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/hooks/useAuth.ts.txt
- Extracted: 2026-05-18
- Category: github-code

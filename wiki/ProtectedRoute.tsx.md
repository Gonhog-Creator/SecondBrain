# ProtectedRoute.tsx

Source: junk_drawer/github/DeltaDash/frontend/src/components/ProtectedRoute.tsx.txt

Category: [[github-code]]

## Summary
import { Navigate } from 'react-router-dom'; import { useAuth } from '../hooks/useAuth'; interface ProtectedRouteProps { children: React.ReactNode; } export function ProtectedRoute({ children }: ProtectedRouteProps) { const { isAuthenticated, isLoading } = useAuth();

## Full Content
import { Navigate } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

interface ProtectedRouteProps {
  children: React.ReactNode;
}

export function ProtectedRoute({ children }: ProtectedRouteProps) {
  const { isAuthenticated, isLoading } = useAuth();

  if (isLoading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="text-lg">Loading...</div>
      </div>
    );
  }

  if (!isAuthenticated) {
    return <Navigate to="/login" replace />;
  }

  return <>{children}</>;
}


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/components/ProtectedRoute.tsx.txt
- Extracted: 2026-05-18
- Category: github-code

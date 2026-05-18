# client.ts

Source: junk_drawer/github/DeltaDash/frontend/src/api/client.ts.txt

Category: [[github-code]]

## Summary
// Force HTTPS for production backend URLs // Build timestamp: 2026-05-17T20:30:00Z const getApiBaseUrl = () => { const envUrl = import.meta.env.VITE_API_URL; if (envUrl) { // If it's a Railway production URL, force HTTPS if (envUrl.includes('railway.app') && envUrl.startsWith('http:')) { return envUrl.replace('http:', 'https:'); } // Otherwise, use same protocol as current page for HTTP URLs

## Full Content
// Force HTTPS for production backend URLs
// Build timestamp: 2026-05-17T20:30:00Z
const getApiBaseUrl = () => {
  const envUrl = import.meta.env.VITE_API_URL;
  if (envUrl) {
    // If it's a Railway production URL, force HTTPS
    if (envUrl.includes('railway.app') && envUrl.startsWith('http:')) {
      return envUrl.replace('http:', 'https:');
    }
    // Otherwise, use same protocol as current page for HTTP URLs
    if (window.location.protocol === 'https:' && envUrl.startsWith('http:')) {
      return envUrl.replace('http:', 'https:');
    }
    return envUrl;
  }
  // Fallback: use same protocol as current page
  const protocol = window.location.protocol === 'https:' ? 'https:' : 'http:';
  return `${protocol}//localhost:8000`;
};

const API_BASE_URL = getApiBaseUrl();

class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseUrl}${endpoint}`;
    const token = localStorage.getItem('token');
    const isFormData = options.body instanceof FormData;
    const config: RequestInit = {
      ...options,
      credentials: 'include',
      headers: isFormData
        ? {
            ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
            ...options.headers,
          }
        : {
            'Content-Type': 'application/json',
            ...(token ? { 'Authorization': `Bearer ${token}` } : {}),
            ...options.headers,
          },
    };

    const response = await fetch(url, config);

    if (!response.ok) {
      if (response.status === 401) {
        // Only redirect to login if not already on login page or checking auth
        if (!window.location.pathname.includes('/login') && !endpoint.includes('/auth/me')) {
          window.location.href = '/login';
        }
        // Suppress console error for auth/me endpoint to clean up console
        if (!endpoint.includes('/auth/me')) {
          console.error('Unauthorized request to', endpoint);
        }
        throw new Error('Unauthorized');
      }
      const error = await response.json().catch(() => ({ detail: 'An error occurred' }));
      throw new Error(error.detail || 'An error occurred');
    }

    if (response.status === 204 || response.headers.get('content-length') === '0') {
      return undefined as T;
    }
    return response.json();
  }

  async get<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'GET' });
  }

  async post<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'POST',
      body: data instanceof FormData ? data : (data ? JSON.stringify(data) : undefined),
    });
  }

  async patch<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'PATCH',
      body: data ? JSON.stringify(data) : undefined,
    });
  }

  async delete<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'DELETE' });
  }

  async put<T>(endpoint: string, data?: unknown): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'PUT',
      body: data ? JSON.stringify(data) : undefined,
    });
  }
}

export const apiClient = new ApiClient(API_BASE_URL);


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/src/api/client.ts.txt
- Extracted: 2026-05-18
- Category: github-code

import { apiClient } from './client';

export interface LoginCredentials {
  username: string;
  password: string;
}

export interface Token {
  access_token: string;
  token_type: string;
}

export interface User {
  id: string;
  username: string;
  email: string;
  full_name: string | null;
  role: string;
  is_active: boolean;
  is_admin: boolean;
  created_at: string;
  updated_at: string;
}

export const authApi = {
  login: async (credentials: LoginCredentials): Promise<Token> => {
    const formData = new FormData();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);

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
      const protocol = window.location.protocol === 'https:' ? 'https:' : 'http:';
      return `${protocol}//localhost:8000`;
    };

    const response = await fetch(`${getApiBaseUrl()}/api/v1/auth/login`, {
      method: 'POST',
      body: formData,
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Login failed');
    }

    const tokenData = await response.json();
    
    // Store the token in localStorage for the apiClient to use
    localStorage.setItem('token', tokenData.access_token);
    
    return tokenData;
  },

  logout: async (): Promise<{ message: string }> => {
    localStorage.removeItem('token');
    return apiClient.post<{ message: string }>('/api/v1/auth/logout');
  },

  getCurrentUser: async (): Promise<User> => {
    return apiClient.get<User>('/api/v1/auth/me');
  },

  changePassword: async (oldPassword: string, newPassword: string): Promise<{ message: string }> => {
    return apiClient.post<{ message: string }>('/api/v1/auth/change-password', {
      old_password: oldPassword,
      new_password: newPassword,
    });
  },
};

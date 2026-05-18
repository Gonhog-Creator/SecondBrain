# categories.ts

Source: junk_drawer/github/BudgetTool/frontend/src/api/categories.ts.txt

Category: [[github-code]]

## Summary
import api from './client' import { Category } from '../types' export const categoriesApi = { getAll: async (userId: number) => { const response = await api.get<Category[]>('/categories', { params: { user_id: userId } }) return response.data },

## Full Content
import api from './client'
import { Category } from '../types'

export const categoriesApi = {
  getAll: async (userId: number) => {
    const response = await api.get<Category[]>('/categories', {
      params: { user_id: userId }
    })
    return response.data
  },
  
  create: async (category: Partial<Category>, userId: number) => {
    const response = await api.post<Category>('/categories', category, {
      params: { user_id: userId }
    })
    return response.data
  },
  
  update: async (id: number, category: Partial<Category>, userId: number) => {
    const response = await api.put<Category>(`/categories/${id}`, category, {
      params: { user_id: userId }
    })
    return response.data
  },
  
  delete: async (id: number, userId: number) => {
    await api.delete(`/categories/${id}`, {
      params: { user_id: userId }
    })
  },

  autoCategorize: async (userId: number) => {
    const response = await api.post('/categories/auto-categorize', null, {
      params: { user_id: userId }
    })
    return response.data
  },
  reAutoCategorize: async (userId: number) => {
    const response = await api.post('/categories/re-auto-categorize', null, {
      params: { user_id: userId }
    })
    return response.data
  },
}


## Metadata
- Source file: junk_drawer/github/BudgetTool/frontend/src/api/categories.ts.txt
- Extracted: 2026-05-18
- Category: github-code

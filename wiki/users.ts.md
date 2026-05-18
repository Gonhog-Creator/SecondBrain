# users.ts

Source: junk_drawer/github/BudgetTool/frontend/src/api/users.ts.txt

Category: [[github-code]]

## Summary
import api from './client' import { User } from '../types' export const usersApi = { getAll: async () => { const response = await api.get<User[]>('/users') return response.data }, create: async (user: { name: string; email?: string }) => {

## Full Content
import api from './client'
import { User } from '../types'

export const usersApi = {
  getAll: async () => {
    const response = await api.get<User[]>('/users')
    return response.data
  },
  
  create: async (user: { name: string; email?: string }) => {
    const response = await api.post<User>('/users/', user)
    return response.data
  },
  
  update: async (id: number, user: { name?: string; email?: string }) => {
    const response = await api.put<User>(`/users/${id}`, user)
    return response.data
  },
  
  delete: async (id: number) => {
    await api.delete(`/users/${id}`)
  },
  
  getPreferences: async (userId: number) => {
    const response = await api.get(`/users/${userId}/preferences`)
    return response.data
  },
  
  addMapping: async (userId: number, mappingType: string, key: string, categoryId: number) => {
    const response = await api.post(`/users/${userId}/preferences/mapping`, null, {
      params: { mapping_type: mappingType, key, category_id: categoryId }
    })
    return response.data
  },
  
  deleteMapping: async (userId: number, mappingType: string, key: string) => {
    const response = await api.delete(`/users/${userId}/preferences/mapping`, {
      params: { mapping_type: mappingType, key }
    })
    return response.data
  },
}


## Metadata
- Source file: junk_drawer/github/BudgetTool/frontend/src/api/users.ts.txt
- Extracted: 2026-05-18
- Category: github-code

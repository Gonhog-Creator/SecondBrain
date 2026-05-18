# analytics.ts

Source: junk_drawer/github/BudgetTool/frontend/src/api/analytics.ts.txt

Category: [[github-code]]

## Summary
import api from './client' import { AnalyticsSummary, CategorySpending, SpendingOverTime, RecurringPaymentSummary } from '../types' export const analyticsApi = { getSummary: async (userId: number, startDate?: string, endDate?: string) => { const params: any = { user_id: userId } if (startDate) params.start_date = startDate if (endDate) params.end_date = endDate const response = await api.get<AnalyticsSummary>('/analytics/summary', { params }) return response.data

## Full Content
import api from './client'
import { AnalyticsSummary, CategorySpending, SpendingOverTime, RecurringPaymentSummary } from '../types'

export const analyticsApi = {
  getSummary: async (userId: number, startDate?: string, endDate?: string) => {
    const params: any = { user_id: userId }
    if (startDate) params.start_date = startDate
    if (endDate) params.end_date = endDate
    const response = await api.get<AnalyticsSummary>('/analytics/summary', { params })
    return response.data
  },
  
  getByCategory: async (userId: number, startDate?: string, endDate?: string) => {
    const params: any = { user_id: userId }
    if (startDate) params.start_date = startDate
    if (endDate) params.end_date = endDate
    const response = await api.get<CategorySpending[]>('/analytics/by-category', { params })
    return response.data
  },
  
  getOverTime: async (userId: number, startDate?: string, endDate?: string, groupBy?: string) => {
    const params: any = { user_id: userId }
    if (startDate) params.start_date = startDate
    if (endDate) params.end_date = endDate
    if (groupBy) params.group_by = groupBy
    const response = await api.get<SpendingOverTime[]>('/analytics/over-time', { params })
    return response.data
  },

  getIncomeOverTime: async (userId: number, startDate?: string, endDate?: string, groupBy?: string) => {
    const params: any = { user_id: userId }
    if (startDate) params.start_date = startDate
    if (endDate) params.end_date = endDate
    if (groupBy) params.group_by = groupBy
    const response = await api.get<SpendingOverTime[]>('/analytics/income-over-time', { params })
    return response.data
  },

  getRecurring: async (userId: number) => {
    const response = await api.get<RecurringPaymentSummary[]>('/analytics/recurring', {
      params: { user_id: userId }
    })
    return response.data
  },
}


## Metadata
- Source file: junk_drawer/github/BudgetTool/frontend/src/api/analytics.ts.txt
- Extracted: 2026-05-18
- Category: github-code

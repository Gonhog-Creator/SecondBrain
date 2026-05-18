# vite.config.ts

Source: junk_drawer/github/DeltaDash/frontend/vite.config.ts.txt

Category: [[github-code]]

## Summary
import { defineConfig } from 'vite' import react from '@vitejs/plugin-react' import path from 'path' // https://vitejs.dev/config/ export default defineConfig({ plugins: [react()], resolve: { alias: { '@': path.resolve(__dirname, './src'),

## Full Content
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})


## Metadata
- Source file: junk_drawer/github/DeltaDash/frontend/vite.config.ts.txt
- Extracted: 2026-05-18
- Category: github-code

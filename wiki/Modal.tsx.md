# Modal.tsx

Source: junk_drawer/github/BudgetTool/frontend/src/components/Modal.tsx.txt

Category: [[github-code]]

## Summary
import { ReactNode } from 'react' interface ModalProps { isOpen: boolean onClose: () => void title: string children: ReactNode } export default function Modal({ isOpen, onClose, title, children }: ModalProps) {

## Full Content
import { ReactNode } from 'react'

interface ModalProps {
  isOpen: boolean
  onClose: () => void
  title: string
  children: ReactNode
}

export default function Modal({ isOpen, onClose, title, children }: ModalProps) {
  if (!isOpen) return null

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-lg p-6 max-w-md w-full mx-4">
        <h3 className="text-lg font-semibold mb-4">{title}</h3>
        {children}
      </div>
    </div>
  )
}


## Metadata
- Source file: junk_drawer/github/BudgetTool/frontend/src/components/Modal.tsx.txt
- Extracted: 2026-05-18
- Category: github-code

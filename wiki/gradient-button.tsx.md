# gradient-button.tsx

Source: junk_drawer/github/PersonalWebsite/src/components/ui/gradient-button.tsx.txt

Category: [[github-code]]

## Summary
import * as React from "react" import { Slot } from "@radix-ui/react-slot" import { cva, type VariantProps } from "class-variance-authority" import { cn } from "@/lib/utils" const gradientButtonVariants = cva( [ "gradient-button", "inline-flex items-center justify-center", "rounded-[11px] min-w-[132px] px-9 py-4",

## Full Content
import * as React from "react"
import { Slot } from "@radix-ui/react-slot"
import { cva, type VariantProps } from "class-variance-authority"
import { cn } from "@/lib/utils"

const gradientButtonVariants = cva(
  [
    "gradient-button",
    "inline-flex items-center justify-center",
    "rounded-[11px] min-w-[132px] px-9 py-4",
    "text-base leading-[19px] font-[500] text-white",
    "font-sans font-bold",
    "focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-ring",
    "disabled:pointer-events-none disabled:opacity-50",
  ],
  {
    variants: {
      variant: {
        default: "",
        variant: "gradient-button-variant",
      },
    },
    defaultVariants: {
      variant: "default",
    },
  }
)

export interface GradientButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof gradientButtonVariants> {
  asChild?: boolean
}

const GradientButton = React.forwardRef<HTMLButtonElement, GradientButtonProps>(
  ({ className, variant, asChild = false, ...props }, ref) => {
    const Comp = asChild ? Slot : "button"
    return (
      <Comp
        className={cn(gradientButtonVariants({ variant, className }))}
        ref={ref}
        {...props}
      />
    )
  }
)
GradientButton.displayName = "GradientButton"

export { GradientButton, gradientButtonVariants }

## Metadata
- Source file: junk_drawer/github/PersonalWebsite/src/components/ui/gradient-button.tsx.txt
- Extracted: 2026-05-18
- Category: github-code

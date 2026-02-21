# Project Structure

## Directory Layout

```
project-root/
├── src/                    # Source code
│   ├── components/         # UI components
│   ├── lib/                # Utility functions
│   ├── services/           # API/service layer
│   └── types/              # TypeScript types
│
├── tests/                  # Test files
│   ├── unit/
│   └── integration/
│
├── docs/                   # Documentation
│
├── open-agents/            # Open Agent System
│   ├── agents/             # Agent definitions
│   ├── memory/             # Persistent agent memory
│   ├── source/             # Input materials
│   └── output-*/           # Processing stages
│
├── .kiro/                  # Kiro configuration
│   └── steering/           # Steering files
│
├── .claude/commands/       # Claude Code commands
├── .gemini/commands/       # Gemini CLI commands
│
└── [config files]          # package.json, tsconfig.json, etc.
```

## Naming Conventions

### Files
- **Components**: PascalCase (`Button.tsx`, `UserProfile.tsx`)
- **Utilities**: camelCase (`formatDate.ts`, `apiClient.ts`)
- **Types**: PascalCase with suffix (`UserTypes.ts`, `ApiResponse.ts`)
- **Tests**: Same as source with `.test` suffix (`Button.test.tsx`)

### Directories
- All lowercase with hyphens (`user-profile/`, `api-helpers/`)

### Variables and Functions
- **Variables**: camelCase (`userName`, `isLoading`)
- **Constants**: SCREAMING_SNAKE_CASE (`MAX_RETRIES`, `API_URL`)
- **Functions**: camelCase, verb-first (`getUserById`, `formatCurrency`)
- **Types/Interfaces**: PascalCase (`UserProfile`, `ApiResponse`)

## Import Patterns

### Order
1. External libraries (React, lodash, etc.)
2. Internal modules (absolute paths)
3. Relative imports (same feature/component)
4. Types and interfaces
5. Styles

### Example
```typescript
// External
import React from 'react';
import { useQuery } from '@tanstack/react-query';

// Internal (absolute)
import { apiClient } from '@/lib/api';
import { Button } from '@/components/ui';

// Relative
import { useLocalState } from './hooks';
import { formatData } from './utils';

// Types
import type { UserProfile } from './types';

// Styles
import styles from './Component.module.css';
```

## Architectural Decisions

### [Decision 1 - e.g., State Management]
We use [approach] because [reasoning].

### [Decision 2 - e.g., API Layer]
We use [approach] because [reasoning].

### [Decision 3 - e.g., Component Structure]
We use [approach] because [reasoning].

## Key Files

- **Entry point**: `src/index.tsx`
- **Main config**: `package.json`, `tsconfig.json`
- **Environment**: `.env.example` (template for local env)

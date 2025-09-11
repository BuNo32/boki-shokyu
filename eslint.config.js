// @ts-check
import js from '@eslint/js';
import tseslint from 'typescript-eslint';
import prettier from 'eslint-config-prettier';
import globals from 'globals';

export default tseslint.config(
  // Ignore common folders and config files
  { ignores: ['dist/**', 'node_modules/**', '.husky/**', '**/*.config.*', '**/*.cjs'] },

  // JavaScript baseline (apply to JS files)
  { files: ['**/*.js'], ...js.configs.recommended },
  { files: ['**/*.js'], rules: { '@typescript-eslint/no-unused-vars': 'off' } },

  // TypeScript recommended rules
  ...tseslint.configs.recommended,
  {
    files: ['**/*.ts', '**/*.tsx'],
    rules: {
      '@typescript-eslint/no-unused-vars': [
        'error',
        { argsIgnorePattern: '^_', ignoreRestSiblings: true },
      ],
    },
  },

  // Browser globals for client-side JS
  {
    files: ['assets/js/**/*.js'],
    languageOptions: { globals: globals.browser },
  },

  // Turn off TS-specific unused-vars on plain browser JS
  {
    files: ['assets/js/**/*.js'],
    rules: { '@typescript-eslint/no-unused-vars': 'off' },
  },

  // Prettier compatibility
  prettier,
);

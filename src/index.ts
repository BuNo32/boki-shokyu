import { t, type Lang } from './i18n';

export function greet(name: string, lang: Lang = 'ja'): string {
  return t(lang, 'greeting', { name });
}

export type { Lang } from './i18n';


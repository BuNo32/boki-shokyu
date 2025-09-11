import ja from './ja';
import en from './en';

export type Lang = 'ja' | 'en';

type Messages = typeof ja;

const dicts: Record<Lang, Messages> = {
  ja,
  en,
};

export function t(lang: Lang, key: keyof Messages, params?: Record<string, string>): string {
  let template = dicts[lang][key];
  if (!template) return '';
  if (params) {
    for (const [k, v] of Object.entries(params)) {
      template = template.replaceAll(`{${k}}`, v);
    }
  }
  return template;
}

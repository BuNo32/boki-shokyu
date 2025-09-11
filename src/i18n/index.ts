import ja from './ja';
import en from './en';

export type Lang = 'ja' | 'en';

type Dict = typeof ja & typeof en;

const dicts: Record<Lang, { [K in keyof Dict]: string }> = {
  ja,
  en
};

export function t(lang: Lang, key: keyof Dict, params?: Record<string, string>): string {
  let template = dicts[lang][key];
  if (!template) return '';
  if (params) {
    for (const [k, v] of Object.entries(params)) {
      template = template.replaceAll(`{${k}}`, v);
    }
  }
  return template;
}


import { describe, it, expect } from 'vitest';
import { greet } from '../src/index';

describe('greet', () => {
  it('greets in Japanese by default', () => {
    expect(greet('太郎')).toBe('こんにちは、太郎！');
  });

  it('greets in English when specified', () => {
    expect(greet('Taro', 'en')).toBe('Hello, Taro!');
  });
});


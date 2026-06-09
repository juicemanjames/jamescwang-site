// @ts-check
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://jamescwang.com',
  trailingSlash: 'never',
  build: {
    format: 'directory',
  },
});

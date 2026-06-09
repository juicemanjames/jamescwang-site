import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    category: z.string(),
    tags: z.string(),
    date: z.string(),
    summary: z.string(),
    thumbnail: z.string(),
    featured: z.boolean().optional().default(false),
    order: z.number().optional(),
    ogImage: z.string().optional(),
  }),
});

const career = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/career' }),
  schema: z.object({
    title: z.string(),
    category: z.string(),
    date: z.string(),
    summary: z.string(),
    thumbnail: z.string(),
  }),
});

export const collections = { posts, career };

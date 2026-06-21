import fs from 'node:fs';
import path from 'node:path';
import * as yaml from 'js-yaml';

const dataDir = path.join(process.cwd(), 'src', 'data');

function loadYaml<T>(filename: string): T {
  const raw = fs.readFileSync(path.join(dataDir, filename), 'utf-8');
  return yaml.load(raw) as T;
}

export interface SocialLink {
  label: string;
  url: string;
  icon: string;
}

export interface SiteConfig {
  name: string;
  logo: string;
  profilePic: string;
  email: string;
  resumePath: string;
  bio: string[];
  beliefs: { title: string; items: string[] };
  socialLinks: SocialLink[];
}

export interface AboutImage {
  src: string;
  alt: string;
  caption?: string;
  fullWidth?: boolean;
}

export interface AboutSection {
  text: string;
  image?: string;
  imageAlt?: string;
  caption?: string;
  imageMaxWidth?: string;
  images?: AboutImage[];
  video?: { youtubeId: string; caption: string };
}

export interface AboutConfig {
  title: string;
  heroBanner: string;
  linkedinUrl: string;
  sections: AboutSection[];
}

export interface Video {
  title: string;
  youtubeId: string;
  youtubeParams?: string;
  link?: string;
}

export interface VideoPage {
  title: string;
  videos: Video[];
}

export interface VideosConfig {
  life: VideoPage;
  projects: VideoPage;
}

export const site = loadYaml<SiteConfig>('site.yaml');
export const about = loadYaml<AboutConfig>('about.yaml');
export const videos = loadYaml<VideosConfig>('videos.yaml');

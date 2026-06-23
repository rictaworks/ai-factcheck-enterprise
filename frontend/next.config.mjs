/** @type {import('next').NextConfig} */

const isDeployment =
  process.env.VERCEL === "1" || process.env.RAILWAY_ENVIRONMENT !== undefined;

if (isDeployment && !process.env.NEXT_PUBLIC_API_URL) {
  throw new Error("NEXT_PUBLIC_API_URL is required in deployment");
}

const nextConfig = {};

export default nextConfig;

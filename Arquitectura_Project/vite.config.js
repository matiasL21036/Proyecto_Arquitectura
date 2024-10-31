import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000', // Cambia esto al puerto de tu API Flask
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''), // Opcional: reescribe la ruta si es necesario
      },
    },
  },
});

# Frontend

Next.js App Router приложение. UI-компоненты планируется добавлять через [shadcn/ui](https://ui.shadcn.com/).

## Требования

- Node.js 20.9 или новее
- npm

## Установка и запуск

Из папки `frontend` выполните:

```powershell
npm install
Copy-Item .env.example .env.local
npx shadcn@latest init
npm run dev
```

Откройте `http://localhost:3000`. Адрес API настраивается через `NEXT_PUBLIC_API_URL` в `.env.local`.

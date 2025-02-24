FROM node:lts

WORKDIR /app

# Install dependencies based on the preferred package manager
COPY package.json yarn.lock* package-lock.json* pnpm-lock.yaml* ./
COPY . .

RUN \
  if [ -f yarn.lock ]; then yarn --frozen-lockfile; \
  elif [ -f package-lock.json ]; then npm i; \
  elif [ -f pnpm-lock.yaml ]; then yarn global add pnpm && pnpm i; \
  # Allow install without lockfile, so example works even without Node.js installed locally
  else echo "Warning: Lockfile not found. It is recommended to commit lockfiles to version control." && yarn install; \
  fi

# Note: Don't expose ports here, Compose will handle that for us
RUN yarn --version || echo "yarn not installed"

# Start vue.js based on the environment (development or production)
CMD if [ "$ENV" = "production" ]; then \
    if [ -f yarn.lock ]; then \
      yarn build; \
    elif [ -f package-lock.json ]; then \
      npm run build; \
    elif [ -f pnpm-lock.yaml ]; then \
      pnpm run build; \
    else \
      yarn build; \
    fi; \
  else \
    if [ -f yarn.lock ]; then \
      yarn dev --host; \
    elif [ -f package-lock.json ]; then \
      npm run dev -- --host; \
    elif [ -f pnpm-lock.yaml ]; then \
      pnpm dev --host; \
    else \
      yarn dev --host; \
    fi; \
  fi



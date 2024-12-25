# Fitness app

## Roadmap

- [ ] define current program
- [ ] plot stats for current program
 
## Development

```bash
uv run fastapi dev
```

### Docker 

```bash
docker build -t fitness:dev .
```

```bash
docker run -p 8080:80 fitness:dev
```
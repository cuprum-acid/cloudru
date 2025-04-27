FROM python:3.12.10-alpine3.21

WORKDIR /app

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY app.py .

RUN chown -R appuser:appgroup /app

USER appuser

EXPOSE 8000

ENV AUTHOR="Default Author"

CMD ["python", "app.py"]

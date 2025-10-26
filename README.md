# FastAPI ARQ Integration

This project is a demonstration of integrating FastAPI with ARQ (Asynchronous Redis Queue) for handling background tasks in a Python web application. It uses Redis as the message broker for queuing tasks and PostgreSQL as the database, accessed via asyncpg without an ORM.

## Key Components

- **API Layer**: Built with FastAPI, includes endpoints for enqueuing tasks and querying the database synchronously.
- **Worker**: ARQ worker that processes queued tasks (currently logs the task description, can be extended for database operations or other logic).
- **Database Interactions**: Raw SQL queries for inserting and selecting operations from a PostgreSQL table.
- **Load Testing**: Locust script provided for simulating load on the API endpoints.

The project showcases how to enqueue asynchronous jobs from FastAPI routes, allowing for non-blocking operations such as database inserts.

## Purpose

Ideal for learning or prototyping applications that require background task processing, like sending emails, processing data, or any long-running operations without blocking the main API response.

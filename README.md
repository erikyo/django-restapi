# Django RestApi + Docker 

This project provides a Django-based RESTful API template bundled with Docker for easy setup and deployment. It's designed to streamline the development process and ensure a consistent environment across different systems.

## Usage

### Prerequisites

- [Docker](https://www.docker.com/) installed on your machine.

### Getting Started

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create Environment Variables:**

    Create a `.env` file in the root of the project and configure your environment variables. You can use the provided `.env` file as a template.

3. **Start the Application:**

    ```bash
    docker-compose up -d --no-deps --build
    ```

    This command will build the Docker containers and start the Django application. The `-d` flag runs the containers in the background.

4. **Access the API:**

    Once the containers are running, you can access the Django API at [http://localhost:8000](http://localhost:8000).

5. **Stop and Remove Containers:**

    ```bash
    docker-compose down -v
    ```

    This command will stop and remove the running containers, along with associated volumes.

### Testing

Run Django tests to ensure the API functionalities:

```bash
docker-compose exec web python manage.py test
```

## Inspiration

This project drew inspiration from [earthcomfy/django-docker-template](https://github.com/earthcomfy/django-docker-template).

## Contributing

Contributions are welcome! Feel free to submit issues, suggest improvements, or open pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

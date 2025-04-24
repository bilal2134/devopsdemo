terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.2"
    }
  }
}

provider "docker" {}

resource "docker_image" "flask_app" {
  name         = "python:3.10-slim"
  keep_locally = false
}

resource "docker_container" "flask_app" {
  name  = "flask_app"
  image = docker_image.flask_app.name  # Reference the 'name' attribute
  ports {
    internal = 5000
    external = 5000
  }
  command = [
    "sh", "-c", "pip install flask && python -m flask run --host=0.0.0.0"
  ]
  volumes {
  host_path      = "/home/bilal/Coding/flask-webapp/devops-demo"
  container_path = "/app"
}
  working_dir = "/app"
  env = [
    "FLASK_APP=app.py"
  ]
}

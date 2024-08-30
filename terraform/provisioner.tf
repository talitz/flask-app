resource "digitalocean_droplet" "web" {
  # ...

  provisioner "file" {
    source      = "/docker-compose.yml"
    destination = "/app"
  }

  provisioner "remote-exec" {
    inline = [
      "docker-compose up --build",
    ]
  }
}
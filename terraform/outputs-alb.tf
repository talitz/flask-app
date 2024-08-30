output "alb_dns" {
  value = aws_lb.development.dns_name
}
output "alb_zone" {
  value = aws_lb.development.zone_id
}
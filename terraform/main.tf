# このdirに移動してterraform initをする

provider "aws" {
  region = "us-east-2" # ap-northeast-1
}

resource "aws_instance" "example" {
  ami                    = "ami-0fb653ca2d3203ac1"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.instance.id] # 下で作成したsg（instanceという名前）のidを指定

  # heredoc文法
  user_data = <<-EOF
            #!/bin/bash
            echo "Hello World" > index.html
            nohup busybox httpd -f -p 8080 &
            EOF

  # user_dataに新しいパラメータを渡してapplyした時下のインスタンスをターミネートして新しいものを起動する（ユーザーデータは最初の起動時しか実行されない）
  user_data_replace_on_change = true

  tags = {
    Name = "terraform-example"
  }
}

resource "aws_security_group" "instance" {
  name = "terraform-example-instance"

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

import { CfnOutput, RemovalPolicy, Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as ec2 from "aws-cdk-lib/aws-ec2";
import { readFileSync } from "fs";

export class AwsCdkStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // vpc
    const vpc = new ec2.Vpc(this, "TestVpc", {
      ipAddresses: ec2.IpAddresses.cidr('10.0.0.0/16'),
      maxAzs: 1,
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'public',
          subnetType: ec2.SubnetType.PUBLIC,
        },
        {
          cidrMask: 24,
          name: 'private',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
      ],
    })

    // key pair
    const cfnKeyPair = new ec2.CfnKeyPair(this, 'CfnKeyPair', {
      keyName: 'key-pair-by-cdk',
    })
    cfnKeyPair.applyRemovalPolicy(RemovalPolicy.DESTROY)

    // EC2
    const webServer1 = new ec2.Instance(this, "WebServer1", {
      vpc,
      instanceType: ec2.InstanceType.of(ec2.InstanceClass.T2, ec2.InstanceSize.MICRO),
      machineImage: new ec2.AmazonLinuxImage({ generation: ec2.AmazonLinuxGeneration.AMAZON_LINUX_2023 }),
      vpcSubnets: { subnetType: ec2.SubnetType.PUBLIC }, // EC2インスタンスを配置するサブネットを指定、デフォルトはprivate
      keyName: cfnKeyPair.keyName,
    });

    // user data
    // ec2 instanceが作成される時に実行される(更新では実行されない)
    const script = readFileSync("./lib/resources/user-data.sh", "utf8");
    webServer1.addUserData(script);

    // security group
    webServer1.connections.allowFromAnyIpv4(ec2.Port.tcp(80));
    webServer1.connections.allowFromAnyIpv4(ec2.Port.tcp(22));

    // キーペア出力
    new CfnOutput(this, 'GetSSHKeyCommand', {
      value: `aws ssm get-parameter --name /ec2/keypair/${cfnKeyPair.getAtt('KeyPairId')} --region ${this.region} --with-decryption --query Parameter.Value --output text`,
    })

    // EC2インスタンスアクセス用のIPアドレスを出力
    new CfnOutput(this, "WebServer1PublicIPAddress", {
      value: `http://${webServer1.instancePublicIp}`,
    });
  }
}

Connect to your EC2 instance via SSH

Run the following commands to change the user and home directory:

```
sudo su -l ec2-user
pwd
```

Run the configure command to update the AWS CLI software with credentials.

```
aws configure
```

At the prompt, configure the following:

* **AWS Access Key ID** : Enter the value for **AccessKey**
* **AWS Secret Access Key** : Enter the value for **SecretKey**
* **Default region name** : Enter `region`
* **Default output format** : Enter `json/yaml`

Here is a [document](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) to review when trying to create a bucket
